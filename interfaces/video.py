from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt, QRectF)
from PySide6.QtGui import (QIcon, QLinearGradient, QColor, QBrush, QPainterPath, QPainter, QPixmap)
from PySide6.QtWidgets import (QFrame, QGridLayout, QLayout,
                               QSizePolicy, QVBoxLayout, QWidget, QStackedWidget,
                               QLabel)

from qfluentwidgets import (CaptionLabel, CardWidget, ElevatedCardWidget, IconWidget,
                            SmoothScrollArea, SubtitleLabel, TitleLabel,
                            Pivot, qrouter, SegmentedWidget, ScrollArea, FluentIcon)
from assets.chair import qtchair_rc
from assets.weather import weather_rc
from components.cards.link import LinkCardView
from components.cards.sample import SampleCardView

qss = """
SettingInterface,
#view {
    background-color: transparent;
}

QScrollArea {
    border: none;
    background-color: transparent;
}


BannerWidget > #galleryLabel {
    font: 42px 'Segoe UI SemiBold', 'Microsoft YaHei SemiBold';
    background-color: transparent;
    color: black;
    padding-left: 28px;
}
"""

class Banner(QWidget):
    """ Banner widget """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(336)
        self.setObjectName("videoInterface")

        self.vBoxLayout = QVBoxLayout(self)
        self.banner = QPixmap('./assets/chair/Home_Background.png')
        self.linkCardView = LinkCardView(self)
        self.videoLabel = SubtitleLabel('关于阿尔兹海默病', self)
        self.videoLabel.setObjectName('videoLabel')


        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(36, 20, 0, 0)
        self.vBoxLayout.addWidget(self.videoLabel)
        self.vBoxLayout.addWidget(self.linkCardView, 1, Qt.AlignBottom)
        self.vBoxLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)


        for icon, title, content, url, index in zip(
            ["./assets/chair/大脑.png","./assets/chair/大脑2.png"],
            ["TED科普动画", "【科普】"],
            ['什么是阿尔兹海默症', '你了解阿尔兹海默症吗'],
            ['https://www.bilibili.com/video/BV13q4y1i7x2/',
             'https://www.bilibili.com/video/BV1Tx411Y7i1/'],
            [i for i in range(2)]
        ):
            self.linkCardView.addCard(icon, title, content, url)


    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(
            QPainter.SmoothPixmapTransform | QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        w, h = self.width(), self.height()
        path.addRoundedRect(QRectF(0, 0, w, h), 10, 10)
        path.addRect(QRectF(0, h-50, 50, 50))
        path.addRect(QRectF(w-50, 0, 50, 50))
        path.addRect(QRectF(w-50, h-50, 50, 50))
        path = path.simplified()

        # init linear gradient effect
        gradient = QLinearGradient(0, 0, 0, h)

        # draw background color
        gradient.setColorAt(0, QColor(207, 216, 228, 255))
        gradient.setColorAt(1, QColor(207, 216, 228, 0))

        painter.fillPath(path, QBrush(gradient))

        # draw banner image
        pixmap = self.banner.scaled(
            self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        painter.fillPath(path, QBrush(pixmap))

class Video(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.banner = Banner(self)
        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)

        self.__initWidget()
        self.loadSamples()

    def __initWidget(self):
        self.view.setObjectName('view')
        self.setObjectName('2homeInterface')
        self.setStyleSheet(qss)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 36)
        self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.addWidget(self.banner)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

    def loadSamples(self):
        """ load samples """
        # basic input samples
        indicesView = SampleCardView(
            "防阿尔兹海默病训练", self.view)
        for icon, title, content, url, index in zip(
                ["./assets/chair/知识库.png", "./assets/chair/R-医学.png",
                 "./assets/chair/记忆.png", "./assets/chair/摇手.png"],
                ['怎么吃、动、训练', '大脑健康警告信号和抗衰老技术', '阿尔兹海默病的防与治', '如何预防阿尔兹海默病'],
                ["5.0⭐"+_ for _ in ['防治阿尔兹海默病', '预防阿尔兹海默病', '徐俊：守住记忆', '脑健康与脑寿命']],
                ['https://www.bilibili.com/video/BV1zj411K7ue/',
                 'https://www.bilibili.com/video/BV14m421G76A/',
                 'https://www.bilibili.com/video/BV1S3411H7gt/',
                 'https://www.bilibili.com/video/BV1Gy42187ZA/'],
                [i for i in range(4)]
        ):
            indicesView.addSampleCard(icon, title, content, index, url)
        self.vBoxLayout.addWidget(indicesView)
