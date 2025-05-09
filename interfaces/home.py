from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt, QTimer)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QSizePolicy,
                               QSlider, QWidget, QHBoxLayout, QVBoxLayout)

from qfluentwidgets import (BodyLabel, ElevatedCardWidget, IconWidget,
                            ProgressBar, ScrollArea, Slider,
                            StrongBodyLabel, SubtitleLabel, TitleLabel)
from assets.chair import qtchair_rc

from datetime import datetime


class Home(QFrame):
    def __init__(self, parent=None):
        super(Home, self).__init__(parent=parent)
        self.setObjectName('Home')
        self.setup_ui(self)
        self.timer = QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.update_datetime)

    def setup_ui(self, Frame):
        Frame.resize(741, 683)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ScrollArea = ScrollArea(Frame)
        self.ScrollArea.setObjectName(u"ScrollArea")
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 721, 663))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ElevatedCardWidget_2 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_2.setObjectName(u"ElevatedCardWidget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.ElevatedCardWidget_2.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget_2.setSizePolicy(sizePolicy1)
        self.IconWidget = IconWidget(self.ElevatedCardWidget_2)
        self.IconWidget.setObjectName(u"IconWidget")
        self.IconWidget.setGeometry(QRect(20, 20, 71, 71))
        icon = QIcon()
        icon.addFile(u":/\u65b0\u524d\u7f00/time.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget.setIcon(icon)
        self.SubtitleLabel_3 = SubtitleLabel(self.ElevatedCardWidget_2)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        self.SubtitleLabel_3.setGeometry(QRect(110, 10, 120, 27))
        self.TimeDate = SubtitleLabel(self.ElevatedCardWidget_2)
        self.TimeDate.setObjectName(u"TimeDate")
        self.TimeDate.setGeometry(QRect(110, 40, 161, 27))
        self.Time = SubtitleLabel(self.ElevatedCardWidget_2)
        self.Time.setObjectName(u"Time")
        self.Time.setGeometry(QRect(110, 60, 161, 27))

        self.gridLayout_2.addWidget(self.ElevatedCardWidget_2, 1, 0, 1, 1)

        self.ElevatedCardWidget_5 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_5.setObjectName(u"ElevatedCardWidget_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(15)
        sizePolicy2.setHeightForWidth(self.ElevatedCardWidget_5.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget_5.setSizePolicy(sizePolicy2)
        self.ElevatedCardWidget_5.setMinimumSize(QSize(0, 180))
        self.IconWidget_2 = IconWidget(self.ElevatedCardWidget_5)
        self.IconWidget_2.setObjectName(u"IconWidget_2")
        self.IconWidget_2.setGeometry(QRect(20, 20, 71, 71))
        icon1 = QIcon()
        icon1.addFile(u":/\u65b0\u524d\u7f00/\u8f6e\u6905info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget_2.setIcon(icon1)
        self.TitleLabel = TitleLabel(self.ElevatedCardWidget_5)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setGeometry(QRect(110, 20, 341, 38))
        self.SubtitleLabel = SubtitleLabel(self.ElevatedCardWidget_5)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setGeometry(QRect(110, 60, 181, 27))
        self.IconWidget_7 = IconWidget(self.ElevatedCardWidget_5)
        self.IconWidget_7.setObjectName(u"IconWidget_7")
        self.IconWidget_7.setGeometry(QRect(20, 90, 71, 71))
        icon2 = QIcon()
        icon2.addFile(u":/\u65b0\u524d\u7f00/\u7528\u6237\u4fe1\u606f.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget_7.setIcon(icon2)
        self.SubtitleLabel_2 = SubtitleLabel(self.ElevatedCardWidget_5)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        self.SubtitleLabel_2.setGeometry(QRect(110, 100, 120, 27))
        self.StrongBodyLabel = StrongBodyLabel(self.ElevatedCardWidget_5)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setGeometry(QRect(110, 130, 51, 19))
        self.Username = StrongBodyLabel(self.ElevatedCardWidget_5)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(170, 130, 113, 19))

        self.gridLayout_2.addWidget(self.ElevatedCardWidget_5, 0, 0, 1, 2)

        self.ElevatedCardWidget_4 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_4.setObjectName(u"ElevatedCardWidget_4")
        sizePolicy1.setHeightForWidth(self.ElevatedCardWidget_4.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget_4.setSizePolicy(sizePolicy1)
        self.IconWidget_5 = IconWidget(self.ElevatedCardWidget_4)
        self.IconWidget_5.setObjectName(u"IconWidget_5")
        self.IconWidget_5.setGeometry(QRect(20, 20, 61, 61))
        icon3 = QIcon()
        icon3.addFile(u":/\u65b0\u524d\u7f00/\u6e29\u5ea6\u8ba1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget_5.setIcon(icon3)
        self.IconWidget_6 = IconWidget(self.ElevatedCardWidget_4)
        self.IconWidget_6.setObjectName(u"IconWidget_6")
        self.IconWidget_6.setGeometry(QRect(160, 20, 61, 61))
        icon4 = QIcon()
        icon4.addFile(u":/\u65b0\u524d\u7f00/\u7a7a\u6c14\u6e7f\u5ea6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget_6.setIcon(icon4)
        self.DhtText = SubtitleLabel(self.ElevatedCardWidget_4)
        self.DhtText.setObjectName(u"DhtText")
        self.DhtText.setGeometry(QRect(70, 20, 221, 27))
        self.Temperature = StrongBodyLabel(self.ElevatedCardWidget_4)
        self.Temperature.setObjectName(u"Temperature")
        self.Temperature.setGeometry(QRect(70, 50, 113, 19))
        self.Humidity = StrongBodyLabel(self.ElevatedCardWidget_4)
        self.Humidity.setObjectName(u"Humidity")
        self.Humidity.setGeometry(QRect(220, 50, 113, 19))

        self.gridLayout_2.addWidget(self.ElevatedCardWidget_4, 3, 1, 1, 1)

        self.ElevatedCardWidget = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        sizePolicy1.setHeightForWidth(self.ElevatedCardWidget.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget.setSizePolicy(sizePolicy1)
        self.IconWidget_4 = IconWidget(self.ElevatedCardWidget)
        self.IconWidget_4.setObjectName(u"IconWidget_4")
        self.IconWidget_4.setGeometry(QRect(20, 20, 71, 71))
        icon5 = QIcon()
        icon5.addFile(u":/\u65b0\u524d\u7f00/\u5730\u70b9.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget_4.setIcon(icon5)
        self.SubtitleLabel_5 = SubtitleLabel(self.ElevatedCardWidget)
        self.SubtitleLabel_5.setObjectName(u"SubtitleLabel_5")
        self.SubtitleLabel_5.setGeometry(QRect(110, 20, 120, 27))
        self.GPS = StrongBodyLabel(self.ElevatedCardWidget)
        self.GPS.setObjectName(u"GPS")
        self.GPS.setGeometry(QRect(110, 50, 111, 21))

        self.gridLayout_2.addWidget(self.ElevatedCardWidget, 3, 0, 1, 1)

        self.ElevatedCardWidget_3 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_3.setObjectName(u"ElevatedCardWidget_3")
        sizePolicy1.setHeightForWidth(self.ElevatedCardWidget_3.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget_3.setSizePolicy(sizePolicy1)
        self.IconWidget_3 = IconWidget(self.ElevatedCardWidget_3)
        self.IconWidget_3.setObjectName(u"IconWidget_3")
        self.IconWidget_3.setGeometry(QRect(20, 20, 71, 71))
        icon6 = QIcon()
        icon6.addFile(u":/\u65b0\u524d\u7f00/\u5ea7\u6905\u8c03\u8282.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget_3.setIcon(icon6)
        self.ChairSeat = Slider(self.ElevatedCardWidget_3)
        self.ChairSeat.setObjectName(u"ChairSeat")
        self.ChairSeat.setGeometry(QRect(90, 70, 200, 21))
        self.ChairSeat.setTracking(True)
        self.ChairSeat.setOrientation(Qt.Horizontal)
        self.ChairSeat.setTickPosition(QSlider.TicksAbove)
        self.SubtitleLabel_4 = SubtitleLabel(self.ElevatedCardWidget_3)
        self.SubtitleLabel_4.setObjectName(u"SubtitleLabel_4")
        self.SubtitleLabel_4.setGeometry(QRect(100, 10, 120, 27))

        self.gridLayout_2.addWidget(self.ElevatedCardWidget_3, 1, 1, 1, 1)

        self.ElevatedCardWidget_6 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_6.setObjectName(u"ElevatedCardWidget_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(10)
        sizePolicy3.setHeightForWidth(self.ElevatedCardWidget_6.sizePolicy().hasHeightForWidth())
        self.ElevatedCardWidget_6.setSizePolicy(sizePolicy3)
        self.IconWidget_8 = IconWidget(self.ElevatedCardWidget_6)
        self.IconWidget_8.setObjectName(u"IconWidget_8")
        self.IconWidget_8.setGeometry(QRect(20, 20, 71, 71))
        icon7 = QIcon()
        icon7.addFile(u":/\u65b0\u524d\u7f00/\u7535\u91cf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget_8.setIcon(icon7)
        self.Battery = ProgressBar(self.ElevatedCardWidget_6)
        self.Battery.setObjectName(u"Battery")
        self.Battery.setGeometry(QRect(120, 60, 451, 8))
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Battery.sizePolicy().hasHeightForWidth())
        self.Battery.setSizePolicy(sizePolicy4)
        self.Battery.setMinimumSize(QSize(0, 8))
        self.Battery.setVal(0.000000000000000)
        self.BatteryVal = BodyLabel(self.ElevatedCardWidget_6)
        self.BatteryVal.setObjectName(u"BatteryVal")
        self.BatteryVal.setGeometry(QRect(190, 30, 21, 19))
        self.BatteryVal.setFrameShape(QFrame.NoFrame)
        self.BatteryVal.setFrameShadow(QFrame.Plain)
        self.BodyLabel_2 = BodyLabel(self.ElevatedCardWidget_6)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        self.BodyLabel_2.setGeometry(QRect(220, 30, 65, 19))
        self.BodyLabel_3 = BodyLabel(self.ElevatedCardWidget_6)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        self.BodyLabel_3.setGeometry(QRect(120, 30, 65, 19))

        self.gridLayout_2.addWidget(self.ElevatedCardWidget_6, 4, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.ScrollArea)


        self.retranslate_ui(Frame)

        QMetaObject.connectSlotsByName(Frame)

    def retranslate_ui(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Frame", "时间", None))
        self.TimeDate.setText(QCoreApplication.translate("Frame", datetime.now().strftime("%Y年 %m月 %d日"), None))
        self.Time.setText(QCoreApplication.translate("Frame", datetime.now().strftime("%H:%M:%S"), None))
        self.TitleLabel.setText(QCoreApplication.translate("Frame", "健康守望者  智能颐养椅", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Frame", "轮椅序列号： 00001", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Frame", "用户信息", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Frame", "用户名", None))
        self.Username.setText(QCoreApplication.translate("Frame", "None", None))
        self.DhtText.setText(QCoreApplication.translate("Frame", "温度                    湿度", None))
        self.Temperature.setText(QCoreApplication.translate("Frame", "20℃", None))
        self.Humidity.setText(QCoreApplication.translate("Frame", "20%", None))
        self.SubtitleLabel_5.setText(QCoreApplication.translate("Frame", "GPS", None))
        self.GPS.setText(QCoreApplication.translate("Frame", "35.59, 116.95", None))
        self.SubtitleLabel_4.setText(QCoreApplication.translate("Frame", "座椅", None))
        self.BatteryVal.setText(QCoreApplication.translate("Frame", "30", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Frame", "%", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Frame", "电源电量", None))

    def update_datetime(self):
        self.TimeDate.setText(QCoreApplication.translate("Frame", datetime.now().strftime("%Y年 %m月 %d日"), None))
        self.Time.setText(QCoreApplication.translate("Frame", datetime.now().strftime("%H:%M:%S"), None))