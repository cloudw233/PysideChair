from PySide6.QtCore import Qt

from components.cards.heart import HeartCard

from PySide6.QtWidgets import (QFrame, QHBoxLayout)

from components.cards.heart import HeartCard


class HeartRate(QFrame):

    def __init__(self, parent=None):
        super(HeartRate,self).__init__(parent=parent)
        self.setObjectName("heartRateInterface")
        self.hBoxLayout = QHBoxLayout(self)
        self.card = HeartCard(self)
        self.hBoxLayout.addWidget(self.card, Qt.AlignCenter)