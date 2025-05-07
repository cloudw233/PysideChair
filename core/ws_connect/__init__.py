import websockets
import asyncio

import orjson as json

from PySide6.QtCore import Signal, QObject, Slot
from loguru import logger

from config import config
from core.builtins.message_constructors import MessageChain, MessageChainInstance, MessageChainD
from core.signals import Signals


# core/ws_connect/__init__.py
class WebSocketClient(QObject):
    def __init__(self):
        super().__init__()
        self.url = config("ws_server")
        self.websocket = None
        self.running = False
        self._loop = asyncio.get_event_loop()
        self.signals = Signals()
        self._receive_lock = asyncio.Lock()
        self._receiver_task = None
        self._reconnect_delay = 1  # 初始重连延迟(秒)
        self._max_reconnect_delay = 60  # 最大重连延迟(秒)
        self._is_reconnecting = False

    async def connect_ws(self):
        while True:
            try:
                if not self.websocket or not self.running:
                    self.websocket = await websockets.connect(self.url)
                    self.running = True
                    self._reconnect_delay = 1  # 连接成功后重置重连延迟
                    logger.success("WebSocket连接成功")

                    # 启动消息接收任务
                    if not self._receiver_task:
                        self._receiver_task = asyncio.create_task(self.receive_messages())
                    return True

            except Exception as e:
                logger.error(f"连接失败: {e}, {self._reconnect_delay}秒后重试")
                await asyncio.sleep(self._reconnect_delay)
                self._reconnect_delay = min(self._reconnect_delay * 2, self._max_reconnect_delay)
                continue

    async def receive_messages(self):
        while self.running:
            try:
                if self.websocket:
                    async with self._receive_lock:
                        message = await self.websocket.recv()
                        logger.info(f"收到消息: {message}")
                        self.signals.message_received.emit(MessageChainD(json.loads(message)))

            except websockets.ConnectionClosed:
                logger.info("连接已断开,准备重连...")
                self.running = False
                if self.websocket:
                    await self.websocket.close()
                    self.websocket = None
                if not self._is_reconnecting:
                    self._is_reconnecting = True
                    await self.reconnect()
                break

            except Exception as e:
                logger.error(f"接收消息错误: {e}")
                await asyncio.sleep(1)

    async def reconnect(self):
        """处理重连逻辑"""
        try:
            logger.info("开始重连...")
            await self.connect_ws()
            self._is_reconnecting = False
        except Exception as e:
            logger.error(f"重连失败: {e}")
            self._is_reconnecting = False

    async def send_message(self, message: MessageChainInstance):
        while True:
            if self.websocket and self.running:
                try:
                    await self.websocket.send(json.dumps(message.deserialize()))
                    return True
                except websockets.ConnectionClosed:
                    logger.error("发送消息时发现连接断开,准备重连...")
                    self.running = False
                    if not self._is_reconnecting:
                        self._is_reconnecting = True
                        await self.reconnect()
                except Exception as e:
                    logger.error(f"发送消息错误: {e}")
                    return False
            else:
                logger.info("连接未就绪,等待重连...")
                await asyncio.sleep(1)

    async def close(self):
        """关闭连接"""
        self.running = False
        if self._receiver_task:
            self._receiver_task.cancel()
            self._receiver_task = None
        if self.websocket:
            await self.websocket.close()
            self.websocket = None

