import websockets

import orjson as json

from PySide6.QtCore import Signal, QObject

from core.builtins.message_constructors import MessageChain, MessageChainInstance, MessageChainD


class WebSocketClient(QObject):
    message_received = Signal(MessageChainInstance)

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.websocket = None
        self.running = False

    async def connect_ws(self):
        try:
            self.websocket = await websockets.connect(self.url)
            self.running = True
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    async def receive_messages(self):
        while self.running:
            try:
                message = await self.websocket.recv()
                self.message_received.emit(MessageChainD(json.loads(message)))
            except websockets.ConnectionClosed:
                print("Connection closed")
                self.running = False
                break
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    async def send_message(self, message: MessageChainInstance):
        if self.websocket and self.running:
            try:
                await self.websocket.send(json.dumps(message.deserialize()))
                return True
            except Exception as e:
                print(f"Error sending message: {e}")
                return False
        return False

    async def close(self):
        self.running = False
        if self.websocket:
            await self.websocket.close()
