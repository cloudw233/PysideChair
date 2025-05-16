from PySide6.QtCore import Qt, Slot

from components.cards.heart import HeartCard

from PySide6.QtWidgets import (QFrame, QHBoxLayout)

from components.cards.heart import HeartCard
from config import config
from core.builtins.assigned_element import AccountElement, HeartElement
from core.builtins.elements import HeartElements
from core.builtins.message_constructors import MessageChainInstance, MessageChain
from core.security import get_computer_id
from core.signals import Signals


class HeartRate(QFrame):

    def __init__(self, parent=None):
        super(HeartRate,self).__init__(parent=parent)
        self.setObjectName("heartRateInterface")
        self.hBoxLayout = QHBoxLayout(self)
        self.card = HeartCard(self)
        self.hBoxLayout.addWidget(self.card, Qt.AlignCenter)
        self.signals = Signals()

        self.signals.message_received.connect(self.update_heart_rate)

    @Slot()
    def on_start_recording_released(self):
        self.card.IndeterminateProgressRing.start()
        self.card.StartRecording.setEnabled(False)
        self.signals.message_sent.emit(MessageChain([
            AccountElement(
                config("username"),
                "data",
                config("password"),
                get_computer_id()
            ),HeartElement(bpm=-1)]))

    @Slot(MessageChainInstance)
    def update_heart_rate(self, message: MessageChainInstance):
        messages = message.serialize()
        heart = [_ for _ in messages if isinstance(_,HeartElements)]
        if len(heart) > 0:
            self.card.update_heart_rate(heart[0].bpm)