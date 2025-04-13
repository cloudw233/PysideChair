from qfluentwidgets import ScrollArea

from components.cards.heart import HeartCard

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget, QFrame, QHBoxLayout)

class HeartRate(QFrame):

    def __init__(self, parent=None):
        super(HeartRate,self).__init__(parent=parent)
        self.setObjectName("heartRateInterface")
        self.hBoxLayout = QHBoxLayout(self)
        self.card = HeartCard(self)
        self.hBoxLayout.addWidget(self.card, Qt.AlignCenter)