from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

from qfluentwidgets import (CardWidget, ElevatedCardWidget, IconWidget, IndeterminateProgressRing,
    LargeTitleLabel, PushButton, SimpleCardWidget)

import assets.chair.qtchair_rc

class HeartCard(ElevatedCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(653, 410)
        self.StartRecording = PushButton(self)
        self.StartRecording.setObjectName(u"StartRecording")
        self.StartRecording.setGeometry(QRect(150, 180, 151, 51))
        self.HeartIcon = IconWidget(self)
        self.HeartIcon.setObjectName(u"HeartIcon")
        self.HeartIcon.setGeometry(QRect(150, 90, 71, 71))
        icon = QIcon()
        icon.addFile(":/新前缀/i-心率.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HeartIcon.setIcon(icon)
        self.LargeTitleLabel = LargeTitleLabel(self)
        self.LargeTitleLabel.setObjectName(u"LargeTitleLabel")
        self.LargeTitleLabel.setGeometry(QRect(240, 100, 311, 54))
        self.IndeterminateProgressRing = IndeterminateProgressRing(self, False)
        self.IndeterminateProgressRing.setObjectName(u"IndeterminateProgressRing")
        self.IndeterminateProgressRing.setGeometry(QRect(320, 180, 41, 41))
        self.IndeterminateProgressRing.setMinimumSize(QSize(0, 0))

        self.retranslateUi(self)
        self.StartRecording.released.connect(self.on_StartRecording_released)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.StartRecording.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u6d4b\u91cf", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u5fc3\u7387 - NaN\u6b21/\u5206", None))

    @Slot()
    def on_StartRecording_released(self):
        self.IndeterminateProgressRing.start()
        self.StartRecording.setEnabled(False)