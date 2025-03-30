from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLayout,
                               QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (CaptionLabel, CardWidget, ElevatedCardWidget, IconWidget,
                            SimpleCardWidget, SmoothScrollArea, SubtitleLabel, TitleLabel)
from assets.chair import qtchair_rc
from assets.weather import weather_rc

class Weather(QWidget):

    def __init__(self):
        super().__init__()
        self.pivot = Pivot(self)
        self.stackedWidget = QStackedWidget(self)
        self.vBoxLayout = QVBoxLayout(self)

        self.songInterface = QLabel('Song Interface', self)
        self.albumInterface = QLabel('Album Interface', self)
        self.artistInterface = QLabel('Artist Interface', self)

        # 添加标签页
        self.addSubInterface(self.songInterface, 'songInterface', 'Song')
        self.addSubInterface(self.albumInterface, 'albumInterface', 'Album')
        self.addSubInterface(self.artistInterface, 'artistInterface', 'Artist')

        # 连接信号并初始化当前标签页
        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        self.stackedWidget.setCurrentWidget(self.songInterface)
        self.pivot.setCurrentItem(self.songInterface.objectName())

        self.vBoxLayout.setContentsMargins(30, 0, 30, 30)
        self.vBoxLayout.addWidget(self.pivot, 0, Qt.AlignHCenter)
        self.vBoxLayout.addWidget(self.stackedWidget)
        self.resize(400, 400)

    def addSubInterface(self, widget: QLabel, objectName: str, text: str):
        widget.setObjectName(objectName)
        widget.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(widget)

        # 使用全局唯一的 objectName 作为路由键
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget)
        )

    def onCurrentIndexChanged(self, index):
        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(735, 721)
        Frame.setFrameShape(QFrame.NoFrame)
        Frame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.SmoothScrollArea = SmoothScrollArea(Frame)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.SmoothScrollArea.sizePolicy().hasHeightForWidth())
        self.SmoothScrollArea.setSizePolicy(sizePolicy)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 713, 699))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.CardWidget_17 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_17.setObjectName(u"CardWidget_17")
        self.gridLayout_5 = QGridLayout(self.CardWidget_17)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Day4 = TitleLabel(self.CardWidget_17)
        self.Day4.setObjectName(u"Day4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Day4.sizePolicy().hasHeightForWidth())
        self.Day4.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.Day4, 0, 3, 1, 1)

        self.IconWidget_14 = IconWidget(self.CardWidget_17)
        self.IconWidget_14.setObjectName(u"IconWidget_14")
        sizePolicy1.setHeightForWidth(self.IconWidget_14.sizePolicy().hasHeightForWidth())
        self.IconWidget_14.setSizePolicy(sizePolicy1)
        self.IconWidget_14.setMaximumSize(QSize(80, 80))
        icon = QIcon()
        icon.addFile(u":/Qweather/999.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget_14.setIcon(icon)

        self.gridLayout_5.addWidget(self.IconWidget_14, 0, 2, 1, 1)

        self.IconWidget_15 = IconWidget(self.CardWidget_17)
        self.IconWidget_15.setObjectName(u"IconWidget_15")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.IconWidget_15.sizePolicy().hasHeightForWidth())
        self.IconWidget_15.setSizePolicy(sizePolicy2)
        self.IconWidget_15.setSizeIncrement(QSize(1, 1))

        self.gridLayout_5.addWidget(self.IconWidget_15, 0, 1, 1, 1)

        self.ElevatedCardWidget_3 = ElevatedCardWidget(self.CardWidget_17)
        self.ElevatedCardWidget_3.setObjectName(u"ElevatedCardWidget_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ElevatedCardWidget_3.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget_3.setSizePolicy(sizePolicy3)
        self.Desc4 = CaptionLabel(self.ElevatedCardWidget_3)
        self.Desc4.setObjectName(u"Desc4")
        self.Desc4.setGeometry(QRect(10, 10, 311, 51))
        self.Desc4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Desc4.setWordWrap(True)

        self.gridLayout_5.addWidget(self.ElevatedCardWidget_3, 0, 5, 1, 1)

        self.Date4 = SubtitleLabel(self.CardWidget_17)
        self.Date4.setObjectName(u"Date4")
        sizePolicy1.setHeightForWidth(self.Date4.sizePolicy().hasHeightForWidth())
        self.Date4.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.Date4, 0, 4, 1, 1)


        self.gridLayout_2.addWidget(self.CardWidget_17, 3, 0, 1, 1)

        self.CardWidget_21 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_21.setObjectName(u"CardWidget_21")
        self.gridLayout_9 = QGridLayout(self.CardWidget_21)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.Date7 = SubtitleLabel(self.CardWidget_21)
        self.Date7.setObjectName(u"Date7")
        sizePolicy1.setHeightForWidth(self.Date7.sizePolicy().hasHeightForWidth())
        self.Date7.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.Date7, 0, 5, 1, 1)

        self.IconWidget_22 = IconWidget(self.CardWidget_21)
        self.IconWidget_22.setObjectName(u"IconWidget_22")
        sizePolicy1.setHeightForWidth(self.IconWidget_22.sizePolicy().hasHeightForWidth())
        self.IconWidget_22.setSizePolicy(sizePolicy1)
        self.IconWidget_22.setMaximumSize(QSize(80, 80))
        self.IconWidget_22.setIcon(icon)

        self.gridLayout_9.addWidget(self.IconWidget_22, 0, 2, 1, 1)

        self.ElevatedCardWidget_7 = ElevatedCardWidget(self.CardWidget_21)
        self.ElevatedCardWidget_7.setObjectName(u"ElevatedCardWidget_7")
        sizePolicy3.setHeightForWidth(self.ElevatedCardWidget_7.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget_7.setSizePolicy(sizePolicy3)
        self.Desc7 = CaptionLabel(self.ElevatedCardWidget_7)
        self.Desc7.setObjectName(u"Desc7")
        self.Desc7.setGeometry(QRect(10, 10, 311, 51))
        self.Desc7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Desc7.setWordWrap(True)

        self.gridLayout_9.addWidget(self.ElevatedCardWidget_7, 0, 6, 1, 1)

        self.IconWidget_23 = IconWidget(self.CardWidget_21)
        self.IconWidget_23.setObjectName(u"IconWidget_23")
        sizePolicy2.setHeightForWidth(self.IconWidget_23.sizePolicy().hasHeightForWidth())
        self.IconWidget_23.setSizePolicy(sizePolicy2)
        self.IconWidget_23.setSizeIncrement(QSize(1, 1))

        self.gridLayout_9.addWidget(self.IconWidget_23, 0, 1, 1, 1)

        self.Day7 = TitleLabel(self.CardWidget_21)
        self.Day7.setObjectName(u"Day7")
        sizePolicy1.setHeightForWidth(self.Day7.sizePolicy().hasHeightForWidth())
        self.Day7.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.Day7, 0, 4, 1, 1)


        self.gridLayout_2.addWidget(self.CardWidget_21, 6, 0, 1, 1)

        self.CardWidget_16 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_16.setObjectName(u"CardWidget_16")
        self.gridLayout_4 = QGridLayout(self.CardWidget_16)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Day2 = TitleLabel(self.CardWidget_16)
        self.Day2.setObjectName(u"Day2")
        sizePolicy1.setHeightForWidth(self.Day2.sizePolicy().hasHeightForWidth())
        self.Day2.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.Day2, 0, 3, 1, 1)

        self.IconWidget_13 = IconWidget(self.CardWidget_16)
        self.IconWidget_13.setObjectName(u"IconWidget_13")
        sizePolicy1.setHeightForWidth(self.IconWidget_13.sizePolicy().hasHeightForWidth())
        self.IconWidget_13.setSizePolicy(sizePolicy1)
        self.IconWidget_13.setMaximumSize(QSize(80, 80))
        self.IconWidget_13.setIcon(icon)

        self.gridLayout_4.addWidget(self.IconWidget_13, 0, 2, 1, 1)

        self.IconWidget_12 = IconWidget(self.CardWidget_16)
        self.IconWidget_12.setObjectName(u"IconWidget_12")
        sizePolicy2.setHeightForWidth(self.IconWidget_12.sizePolicy().hasHeightForWidth())
        self.IconWidget_12.setSizePolicy(sizePolicy2)
        self.IconWidget_12.setSizeIncrement(QSize(1, 1))

        self.gridLayout_4.addWidget(self.IconWidget_12, 0, 1, 1, 1)

        self.ElevatedCardWidget_2 = ElevatedCardWidget(self.CardWidget_16)
        self.ElevatedCardWidget_2.setObjectName(u"ElevatedCardWidget_2")
        sizePolicy3.setHeightForWidth(self.ElevatedCardWidget_2.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget_2.setSizePolicy(sizePolicy3)
        self.Desc2 = CaptionLabel(self.ElevatedCardWidget_2)
        self.Desc2.setObjectName(u"Desc2")
        self.Desc2.setGeometry(QRect(10, 10, 311, 51))
        self.Desc2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Desc2.setWordWrap(True)

        self.gridLayout_4.addWidget(self.ElevatedCardWidget_2, 0, 5, 1, 1)

        self.Date2 = SubtitleLabel(self.CardWidget_16)
        self.Date2.setObjectName(u"Date2")
        sizePolicy1.setHeightForWidth(self.Date2.sizePolicy().hasHeightForWidth())
        self.Date2.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.Date2, 0, 4, 1, 1)


        self.gridLayout_2.addWidget(self.CardWidget_16, 1, 0, 1, 1)

        self.CardWidget_18 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_18.setObjectName(u"CardWidget_18")
        self.gridLayout_6 = QGridLayout(self.CardWidget_18)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Day5 = TitleLabel(self.CardWidget_18)
        self.Day5.setObjectName(u"Day5")
        sizePolicy1.setHeightForWidth(self.Day5.sizePolicy().hasHeightForWidth())
        self.Day5.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.Day5, 0, 3, 1, 1)

        self.IconWidget_16 = IconWidget(self.CardWidget_18)
        self.IconWidget_16.setObjectName(u"IconWidget_16")
        sizePolicy1.setHeightForWidth(self.IconWidget_16.sizePolicy().hasHeightForWidth())
        self.IconWidget_16.setSizePolicy(sizePolicy1)
        self.IconWidget_16.setMaximumSize(QSize(80, 80))
        self.IconWidget_16.setIcon(icon)

        self.gridLayout_6.addWidget(self.IconWidget_16, 0, 2, 1, 1)

        self.IconWidget_17 = IconWidget(self.CardWidget_18)
        self.IconWidget_17.setObjectName(u"IconWidget_17")
        sizePolicy2.setHeightForWidth(self.IconWidget_17.sizePolicy().hasHeightForWidth())
        self.IconWidget_17.setSizePolicy(sizePolicy2)
        self.IconWidget_17.setSizeIncrement(QSize(1, 1))

        self.gridLayout_6.addWidget(self.IconWidget_17, 0, 1, 1, 1)

        self.ElevatedCardWidget_4 = ElevatedCardWidget(self.CardWidget_18)
        self.ElevatedCardWidget_4.setObjectName(u"ElevatedCardWidget_4")
        sizePolicy3.setHeightForWidth(self.ElevatedCardWidget_4.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget_4.setSizePolicy(sizePolicy3)
        self.Desc5 = CaptionLabel(self.ElevatedCardWidget_4)
        self.Desc5.setObjectName(u"Desc5")
        self.Desc5.setGeometry(QRect(10, 10, 311, 51))
        self.Desc5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Desc5.setWordWrap(True)

        self.gridLayout_6.addWidget(self.ElevatedCardWidget_4, 0, 5, 1, 1)

        self.Date5 = SubtitleLabel(self.CardWidget_18)
        self.Date5.setObjectName(u"Date5")
        sizePolicy1.setHeightForWidth(self.Date5.sizePolicy().hasHeightForWidth())
        self.Date5.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.Date5, 0, 4, 1, 1)


        self.gridLayout_2.addWidget(self.CardWidget_18, 4, 0, 1, 1)

        self.CardWidget_20 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_20.setObjectName(u"CardWidget_20")
        self.gridLayout_8 = QGridLayout(self.CardWidget_20)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.Day6 = TitleLabel(self.CardWidget_20)
        self.Day6.setObjectName(u"Day6")
        sizePolicy1.setHeightForWidth(self.Day6.sizePolicy().hasHeightForWidth())
        self.Day6.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.Day6, 0, 3, 1, 1)

        self.IconWidget_20 = IconWidget(self.CardWidget_20)
        self.IconWidget_20.setObjectName(u"IconWidget_20")
        sizePolicy1.setHeightForWidth(self.IconWidget_20.sizePolicy().hasHeightForWidth())
        self.IconWidget_20.setSizePolicy(sizePolicy1)
        self.IconWidget_20.setMaximumSize(QSize(80, 80))
        self.IconWidget_20.setIcon(icon)

        self.gridLayout_8.addWidget(self.IconWidget_20, 0, 2, 1, 1)

        self.IconWidget_21 = IconWidget(self.CardWidget_20)
        self.IconWidget_21.setObjectName(u"IconWidget_21")
        sizePolicy2.setHeightForWidth(self.IconWidget_21.sizePolicy().hasHeightForWidth())
        self.IconWidget_21.setSizePolicy(sizePolicy2)
        self.IconWidget_21.setSizeIncrement(QSize(1, 1))

        self.gridLayout_8.addWidget(self.IconWidget_21, 0, 1, 1, 1)

        self.ElevatedCardWidget_6 = ElevatedCardWidget(self.CardWidget_20)
        self.ElevatedCardWidget_6.setObjectName(u"ElevatedCardWidget_6")
        sizePolicy3.setHeightForWidth(self.ElevatedCardWidget_6.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget_6.setSizePolicy(sizePolicy3)
        self.Desc6 = CaptionLabel(self.ElevatedCardWidget_6)
        self.Desc6.setObjectName(u"Desc6")
        self.Desc6.setGeometry(QRect(10, 10, 311, 51))
        self.Desc6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Desc6.setWordWrap(True)

        self.gridLayout_8.addWidget(self.ElevatedCardWidget_6, 0, 5, 1, 1)

        self.Date6 = SubtitleLabel(self.CardWidget_20)
        self.Date6.setObjectName(u"Date6")
        sizePolicy1.setHeightForWidth(self.Date6.sizePolicy().hasHeightForWidth())
        self.Date6.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.Date6, 0, 4, 1, 1)


        self.gridLayout_2.addWidget(self.CardWidget_20, 5, 0, 1, 1)

        self.CardWidget = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget.setObjectName(u"CardWidget")
        self.gridLayout_3 = QGridLayout(self.CardWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ElevatedCardWidget = ElevatedCardWidget(self.CardWidget)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        sizePolicy3.setHeightForWidth(self.ElevatedCardWidget.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget.setSizePolicy(sizePolicy3)
        self.Desc1 = CaptionLabel(self.ElevatedCardWidget)
        self.Desc1.setObjectName(u"Desc1")
        self.Desc1.setGeometry(QRect(10, 10, 311, 51))
        self.Desc1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Desc1.setWordWrap(True)

        self.gridLayout_3.addWidget(self.ElevatedCardWidget, 0, 5, 1, 1)

        self.Date1 = SubtitleLabel(self.CardWidget)
        self.Date1.setObjectName(u"Date1")
        sizePolicy1.setHeightForWidth(self.Date1.sizePolicy().hasHeightForWidth())
        self.Date1.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.Date1, 0, 4, 1, 1)

        self.IconWidget_10 = IconWidget(self.CardWidget)
        self.IconWidget_10.setObjectName(u"IconWidget_10")
        sizePolicy1.setHeightForWidth(self.IconWidget_10.sizePolicy().hasHeightForWidth())
        self.IconWidget_10.setSizePolicy(sizePolicy1)
        self.IconWidget_10.setMaximumSize(QSize(80, 80))
        self.IconWidget_10.setIcon(icon)

        self.gridLayout_3.addWidget(self.IconWidget_10, 0, 2, 1, 1)

        self.Day1 = TitleLabel(self.CardWidget)
        self.Day1.setObjectName(u"Day1")
        sizePolicy1.setHeightForWidth(self.Day1.sizePolicy().hasHeightForWidth())
        self.Day1.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.Day1, 0, 3, 1, 1)

        self.IconWidget = IconWidget(self.CardWidget)
        self.IconWidget.setObjectName(u"IconWidget")
        sizePolicy2.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy2)
        self.IconWidget.setSizeIncrement(QSize(1, 1))

        self.gridLayout_3.addWidget(self.IconWidget, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.CardWidget, 0, 0, 1, 1)

        self.CardWidget_19 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_19.setObjectName(u"CardWidget_19")
        self.gridLayout_7 = QGridLayout(self.CardWidget_19)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.Day3 = TitleLabel(self.CardWidget_19)
        self.Day3.setObjectName(u"Day3")
        sizePolicy1.setHeightForWidth(self.Day3.sizePolicy().hasHeightForWidth())
        self.Day3.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.Day3, 0, 3, 1, 1)

        self.IconWidget_18 = IconWidget(self.CardWidget_19)
        self.IconWidget_18.setObjectName(u"IconWidget_18")
        sizePolicy1.setHeightForWidth(self.IconWidget_18.sizePolicy().hasHeightForWidth())
        self.IconWidget_18.setSizePolicy(sizePolicy1)
        self.IconWidget_18.setMaximumSize(QSize(80, 80))
        self.IconWidget_18.setIcon(icon)

        self.gridLayout_7.addWidget(self.IconWidget_18, 0, 2, 1, 1)

        self.IconWidget_19 = IconWidget(self.CardWidget_19)
        self.IconWidget_19.setObjectName(u"IconWidget_19")
        sizePolicy2.setHeightForWidth(self.IconWidget_19.sizePolicy().hasHeightForWidth())
        self.IconWidget_19.setSizePolicy(sizePolicy2)
        self.IconWidget_19.setSizeIncrement(QSize(1, 1))

        self.gridLayout_7.addWidget(self.IconWidget_19, 0, 1, 1, 1)

        self.ElevatedCardWidget_5 = ElevatedCardWidget(self.CardWidget_19)
        self.ElevatedCardWidget_5.setObjectName(u"ElevatedCardWidget_5")
        sizePolicy3.setHeightForWidth(self.ElevatedCardWidget_5.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget_5.setSizePolicy(sizePolicy3)
        self.Desc3 = CaptionLabel(self.ElevatedCardWidget_5)
        self.Desc3.setObjectName(u"Desc3")
        self.Desc3.setGeometry(QRect(10, 10, 311, 51))
        self.Desc3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Desc3.setWordWrap(True)

        self.gridLayout_7.addWidget(self.ElevatedCardWidget_5, 0, 5, 1, 1)

        self.Date3 = SubtitleLabel(self.CardWidget_19)
        self.Date3.setObjectName(u"Date3")
        sizePolicy1.setHeightForWidth(self.Date3.sizePolicy().hasHeightForWidth())
        self.Date3.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.Date3, 0, 4, 1, 1)


        self.gridLayout_2.addWidget(self.CardWidget_19, 2, 0, 1, 1)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.SmoothScrollArea)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.Day4.setText(QCoreApplication.translate("Frame", u"Title label", None))
        self.Desc4.setText(QCoreApplication.translate("Frame", u"Caption label", None))
        self.Date4.setText(QCoreApplication.translate("Frame", u"Subtitle label", None))
        self.Date7.setText(QCoreApplication.translate("Frame", u"Subtitle label", None))
        self.Desc7.setText(QCoreApplication.translate("Frame", u"Caption label", None))
        self.Day7.setText(QCoreApplication.translate("Frame", u"Title label", None))
        self.Day2.setText(QCoreApplication.translate("Frame", u"Title label", None))
        self.Desc2.setText(QCoreApplication.translate("Frame", u"Caption label", None))
        self.Date2.setText(QCoreApplication.translate("Frame", u"Subtitle label", None))
        self.Day5.setText(QCoreApplication.translate("Frame", u"Title label", None))
        self.Desc5.setText(QCoreApplication.translate("Frame", u"Caption label", None))
        self.Date5.setText(QCoreApplication.translate("Frame", u"Subtitle label", None))
        self.Day6.setText(QCoreApplication.translate("Frame", u"Title label", None))
        self.Desc6.setText(QCoreApplication.translate("Frame", u"Caption label", None))
        self.Date6.setText(QCoreApplication.translate("Frame", u"Subtitle label", None))
#if QT_CONFIG(tooltip)
        self.ElevatedCardWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.ElevatedCardWidget.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.Desc1.setText(QCoreApplication.translate("Frame", u"Caption label", None))
        self.Date1.setText(QCoreApplication.translate("Frame", u"Subtitle label", None))
        self.Day1.setText(QCoreApplication.translate("Frame", u"Title label", None))
        self.Day3.setText(QCoreApplication.translate("Frame", u"Title label", None))
        self.Desc3.setText(QCoreApplication.translate("Frame", u"Caption label", None))
        self.Date3.setText(QCoreApplication.translate("Frame", u"Subtitle label", None))
    # retranslateUi
