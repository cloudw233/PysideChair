from loguru import logger
from qasync import asyncSlot
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt, Slot)
from PySide6.QtWidgets import (QVBoxLayout, QWidget, QFrame, QHBoxLayout)

from qfluentwidgets import (AvatarWidget, LineEdit, PasswordLineEdit, PrimaryPushButton, PushButton,
                            SimpleCardWidget, BodyLabel, InfoBar, InfoBarPosition)

from core.builtins.assigned_element import AccountElement
from core.builtins.elements import AccountElements, ResponseElements
from core.builtins.message_constructors import MessageChain, MessageChainInstance
from core.security import get_computer_id
from core.signals import Signals
from core.ws_connect import WebSocketClient
from .register import RegisterCard
from .logged_in import LoggedIn


class LoginCard(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(612, 683)
        self.Login = PrimaryPushButton(self)
        self.Login.setObjectName("Login")
        self.Login.setGeometry(QRect(370, 370, 153, 32))
        self.Register = PushButton(self)
        self.Register.setObjectName("Register")
        self.Register.setGeometry(QRect(210, 370, 141, 31))
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 200, 421, 131))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.UsrnameXD = BodyLabel(self.layoutWidget)
        self.UsrnameXD.setObjectName("UsrnameXD")
        self.UsrnameXD.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.UsrnameXD)

        self.Username = LineEdit(self.layoutWidget)
        self.Username.setObjectName("Username")

        self.verticalLayout.addWidget(self.Username)

        self.PasswordXD = BodyLabel(self.layoutWidget)
        self.PasswordXD.setObjectName("PasswordXD")
        self.PasswordXD.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.PasswordXD)

        self.Password = PasswordLineEdit(self.layoutWidget)
        self.Password.setObjectName("Password")

        self.verticalLayout.addWidget(self.Password)

        self.retranslateUi()


        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("self", "self", None))
        self.Login.setText(QCoreApplication.translate("self", "登录", None))
        self.Register.setText(QCoreApplication.translate("self", "注册", None))
        self.UsrnameXD.setText(QCoreApplication.translate("self", "用户名", None))
        self.PasswordXD.setText(QCoreApplication.translate("self", "密码", None))
    
class LoginI(QFrame):

    def __init__(self, parent=None):
        super(LoginI,self).__init__(parent=parent)
        self.setObjectName("loginInterface")
        self.hBoxLayout = QHBoxLayout(self)
        self.card = LoginCard(self)
        self.r_card = RegisterCard(self)
        self.l_card = LoggedIn(self)
        self.hBoxLayout.addWidget(self.card, Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.r_card, Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.l_card, Qt.AlignCenter)
        self.r_card.setVisible(False)
        self.l_card.setVisible(False)
        self.card.Register.clicked.connect(self.on_register_switched)
        self.r_card.RegisterB.clicked.connect(self.on_register_button_clicked)
        self.card.Login.clicked.connect(self.on_login_clicked)
        self.signals = Signals()
        self.signals.message_received.connect(self.on_server_responded)

    @Slot()
    def on_register_switched(self):
        username = self.card.Username.text()
        password = self.card.Password.text()
        self.r_card.Username.setText(username)
        self.r_card.Password.setText(password)
        self.card.setVisible(False)
        self.r_card.setVisible(True)

    @asyncSlot()
    async def on_register_button_clicked(self):
        username = self.r_card.Username.text()
        password = self.r_card.Password.text()
        password2 = self.r_card.PasswordLineEdit.text()
        if password2 == password:
            self.signals.message_sent.emit(
                MessageChain(
                    [AccountElement(username, 'register', password, get_computer_id())]
                )
            )
        else:
            InfoBar.error(
                title='错误',
                content="两次密码不一致",
                orient=Qt.Vertical,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=-1,
                parent=self.r_card,
            )
            self.r_card.PasswordLineEdit.clear()
            self.r_card.Password.clear()

    @Slot()
    def on_login_clicked(self):
        username = self.card.Username.text()
        password = self.card.Password.text()
        self.signals.message_sent.emit(
            MessageChain(
                [AccountElement(username, 'login', password, get_computer_id())]
            )
        )

    @Slot(MessageChainInstance)
    def on_server_responded(self, msg: MessageChainInstance):
        logger.debug(msg.serialize())
        resp = [_ for _ in msg.serialize() if isinstance(_, ResponseElements)]
        if len(resp) == 1:
            status = resp[0]
            ret_code = status.ret_code
            if status.flag == "login":
                if ret_code == 0:
                    logger.info("Login successfully "+status.msg)
                    self.card.setVisible(False)
                    self.l_card.setVisible(True)
                    InfoBar.success(
                        title='成功',
                        content="登录成功"+status.msg,
                        orient=Qt.Vertical,
                        isClosable=True,
                        position=InfoBarPosition.TOP,
                        duration=-1,
                        parent=self.l_card,
                    )
                else:
                    logger.error("Login failed "+status.msg)
                    InfoBar.error(
                        title='错误',
                        content="登录失败"+status.msg,
                        orient=Qt.Vertical,
                        isClosable=True,
                        position=InfoBarPosition.TOP,
                        duration=-1,
                        parent=self.card,
                    )
                    self.card.Password.clear()
            if status.flag == "register":
                if ret_code == 0:
                    self.r_card.setVisible(False)
                    self.l_card.setVisible(True)
                    InfoBar.success(
                        title='成功',
                        content="注册成功, 已为您登录"+status.msg,
                        orient=Qt.Vertical,
                        isClosable=True,
                        position=InfoBarPosition.TOP,
                        duration=-1,
                        parent=self.l_card,
                    )
                else:
                    InfoBar.error(
                        title='错误',
                        content="注册失败,"+status.msg,
                        orient=Qt.Vertical,
                        isClosable=True,
                        position=InfoBarPosition.TOP,
                        duration=-1,
                        parent=self.r_card,
                    )
                    self.r_card.PasswordLineEdit.clear()
                    self.r_card.Password.clear()
