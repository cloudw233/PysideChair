# coding:utf-8
from PySide6.QtCore import Qt, Signal, QUrl
from PySide6.QtGui import QPixmap, QDesktopServices
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget, QHBoxLayout

from qfluentwidgets import IconWidget, FluentIcon, TextWrap, SingleDirectionScrollArea, CardWidget, ElevatedCardWidget, \
    TitleLabel

qss = """

#contentLabel {
    font: 12px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
    color: rgb(93, 93, 93);
}LinkCard {
    border: 1px solid rgb(234, 234, 234);
    border-radius: 10px;
    background-color: rgba(249, 249, 249, 0.95);
}

LinkCard:hover {
    background-color: rgba(249, 249, 249, 0.93);
    border: 1px solid rgb(220, 220, 220);
}

#titleLabel {
    font: 18px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
    color: black;
}

#contentLabel {
    font: 12px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
    color: rgb(93, 93, 93);
}

LinkCardView {
    background-color: transparent;
    border: none;
}

#view {
    background-color: transparent;
}
"""


class LinkCard(CardWidget):

    def __init__(self, icon, title, content, url, parent=None):
        super().__init__(parent=parent)
        self.url = QUrl(url)
        self.setFixedSize(198, 220)
        self.iconWidget = IconWidget(icon, self)
        self.titleLabel = TitleLabel(title, self)
        self.titleLabel.setObjectName("titleLabel")
        self.contentLabel = QLabel(TextWrap.wrap(content, 28, False)[0], self)
        self.urlWidget = IconWidget(FluentIcon.LINK, self)

        self.__initWidget()

    def __initWidget(self):
        self.setCursor(Qt.PointingHandCursor)

        self.iconWidget.setFixedSize(54, 54)
        self.urlWidget.setFixedSize(16, 16)

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(24, 24, 0, 13)
        self.vBoxLayout.addWidget(self.iconWidget)
        self.vBoxLayout.addSpacing(16)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addSpacing(8)
        self.vBoxLayout.addWidget(self.contentLabel)
        self.vBoxLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.urlWidget.move(170, 192)
        self.setStyleSheet(qss)

        self.titleLabel.setObjectName('titleLabel')
        self.contentLabel.setObjectName('contentLabel')

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        QDesktopServices.openUrl(self.url)


class LinkCardView(SingleDirectionScrollArea):
    """ Link card view """

    def __init__(self, parent=None):
        super().__init__(parent, Qt.Horizontal)
        self.view = QWidget(self)
        self.hBoxLayout = QHBoxLayout(self.view)

        self.hBoxLayout.setContentsMargins(36, 0, 0, 20)
        self.hBoxLayout.setSpacing(12)
        self.hBoxLayout.setAlignment(Qt.AlignLeft)

        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.view.setObjectName('view')
        self.setStyleSheet(qss)

    def addCard(self, icon, title, content, url):
        """ add link card """
        card = LinkCard(icon, title, content, url, self.view)
        self.hBoxLayout.addWidget(card, 0, Qt.AlignLeft)
