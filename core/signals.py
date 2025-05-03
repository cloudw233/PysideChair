# core/signals.py
from PySide6.QtCore import QObject, Signal
from core.builtins.message_constructors import MessageChainInstance

class Signals(QObject):
    _instance = None
    _initialized = False

    message_received = Signal(MessageChainInstance)
    message_sent = Signal(MessageChainInstance)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Signals, cls).__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        if not self._initialized:
            super().__init__()
            self._initialized = True