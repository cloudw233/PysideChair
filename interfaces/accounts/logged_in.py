from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, IconWidget, PrimaryPushButton, PushButton,
    SimpleCardWidget, SubtitleLabel)

class LoggedIn(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(641, 645)
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 90, 491, 301))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.IconWidget = IconWidget(self.widget)
        self.IconWidget.setObjectName(u"IconWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy)
        icon = QIcon('./assets/chair/account.png')
        self.IconWidget.setIcon(icon)

        self.verticalLayout.addWidget(self.IconWidget)

        self.UsernameShow = SubtitleLabel(self.widget)
        self.UsernameShow.setObjectName(u"UsernameShow")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.UsernameShow.sizePolicy().hasHeightForWidth())
        self.UsernameShow.setSizePolicy(sizePolicy1)
        self.UsernameShow.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.UsernameShow)

        self.Exit = PrimaryPushButton(self.widget)
        self.Exit.setObjectName(u"Exit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Exit.sizePolicy().hasHeightForWidth())
        self.Exit.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.Exit)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("self", u"self", None))
        self.UsernameShow.setText(QCoreApplication.translate("self", u"None", None))
        self.Exit.setText(QCoreApplication.translate("self", u"\u9000\u51fa\u767b\u5f55", None))
    # retranslateUi