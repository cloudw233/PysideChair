import websockets
import asyncio

import orjson as json

from PySide6.QtCore import Signal, QObject, Slot

from config import config
from core.builtins.message_constructors import MessageChain, MessageChainInstance, MessageChainD
from core.signals import Signals


class WebSocketClient(QObject):
    def __init__(self):
        super().__init__()
        self.url = config("ws_server")
        self.websocket = None
        self.running = False
        self._loop = asyncio.get_event_loop()
        self.signals = Signals()

    async def connect_ws(self):
        try:
            self.websocket = await websockets.connect(self.url)
            self.running = True
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    async def send_message(self, message: MessageChainInstance):
        if self.websocket and self.running:
            try:
                data = message.deserialize()
                # 使用 orjson 处理序列化
                json_str = str(json.dumps(data))
                await self.websocket.send(json_str)
                return True
            except Exception as e:
                print(f"Error sending message: {e}")
                return False
        return False

    async def receive_messages(self):
        while self.running:
            try:
                if self.websocket:
                    message = await self.websocket.recv()
                    self.signals.message_received.emit(MessageChainD(json.loads(message)))
            except Exception as e:
                print(f"Error receiving message: {e}")
                await asyncio.sleep(1)

    async def send_message(self, message: MessageChainInstance):
        if self.websocket and self.running:
            await self.websocket.send(json.dumps(message.deserialize()))
            return True
        return False

    async def close(self):
        self.running = False
        if self.websocket:
            await self.websocket.close()

