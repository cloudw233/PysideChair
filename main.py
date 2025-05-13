# coding:utf-8
import asyncio
import sys

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout
from qasync import QEventLoop, QApplication, asyncSlot
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, FluentBackgroundTheme, TextBrowser)
from qfluentwidgets import FluentIcon as FIF
from loguru import logger

from config import init_config
from core.builtins.assigned_element import AccountElement, WeatherElement
from core.builtins.message_constructors import MessageChain, MessageChainInstance
from core.security import get_computer_id
from core.signals import Signals
from interfaces.accounts import LoginI
from interfaces.home import Home
from interfaces.video import Video
from interfaces.weather import Weather
from interfaces.heart import HeartRate
from interfaces.settings import SettingsCard
from core.ws_connect import WebSocketClient

init_config()

ascii_art = r'''
  _   _                  _   _     _        ____                          ____   _               _        
 | | | |   ___    __ _  | | | |_  | |__    / ___|   __ _   _ __    ___   / ___| | |__     __ _  (_)  _ __ 
 | |_| |  / _ \  / _` | | | | __| | '_ \  | |      / _` | | '__|  / _ \ | |     | '_ \   / _` | | | | '__|
 |  _  | |  __/ | (_| | | | | |_  | | | | | |___  | (_| | | |    |  __/ | |___  | | | | | (_| | | | | |   
 |_| |_|  \___|  \__,_| |_|  \__| |_| |_|  \____|  \__,_| |_|     \___|  \____| |_| |_|  \__,_| |_| |_|   
                                                                                                          
                                                                                                          '''


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.homeInterface = Home(self) # 主界面
        self.weatherInterface = Weather(self)
        self.heartRateInterface = HeartRate(self)
        self.videoInterface = Video(self)
        self.accountInterface = LoginI(self)
        self.settingInterface = SettingsCard(self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, '主页')
        self.addSubInterface(self.weatherInterface, QIcon("./assets/weather/102.svg"), '天气')
        self.addSubInterface(self.heartRateInterface, QIcon("./assets/chair/heartbeat.png"), '心率')
        self.addSubInterface(self.videoInterface, QIcon("./assets/chair/doctor-bag.png"), '康复视频')

        self.navigationInterface.addSeparator()

        # add custom widget to bottom
        # self.navigationInterface.addWidget(
        #     routeKey='avatar',
        #     widget=NavigationAvatarWidget('zhiyiYo', 'resource/shoko.png'),
        #     onClick=self.showMessageBox,
        #     position=NavigationItemPosition.BOTTOM,
        # )

        self.addSubInterface(self.accountInterface, FIF.PEOPLE, '账号', NavigationItemPosition.BOTTOM)

        self.addSubInterface(self.settingInterface, FIF.SETTING, '设置', NavigationItemPosition.BOTTOM)

        # add badge to navigation item

        # NOTE: enable acrylic effect
        # self.navigationInterface.setAcrylicEnabled(True)

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon('./assets/chair/轮椅.png'))
        self.setWindowTitle('健康守望者 智能颐养椅')

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)


if __name__ == '__main__':
    try:
        logger.info(ascii_art)
        logger.info("Here we go!")
        app = QApplication(sys.argv)
        loop = QEventLoop(app)
        asyncio.set_event_loop(loop)

        client = WebSocketClient()
        signals = Signals()

        # 只启动连接，receive_messages会在连接成功后自动启动
        asyncio.ensure_future(client.connect_ws(), loop=loop)


        @asyncSlot(MessageChainInstance)
        async def send_msg(msg: MessageChainInstance):
            await client.send_message(msg)


        signals.message_sent.connect(send_msg)
        w = Window()
        w.show()

        with loop:
            loop.run_forever()

    except KeyboardInterrupt:
        w.close()
        app.quit()
        loop.run_until_complete(client.close())