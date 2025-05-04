from Demos.security.lsaregevent import ret_code
from PIL.ImageQt import QPixmap
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
        self.card = LoginCard()
        self.r_card = RegisterCard()
        self.l_card = LoggedIn()
        self.hBoxLayout.addWidget(self.card, Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.r_card, Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.l_card, Qt.AlignCenter)
        self.r_card.setVisible(False)
        self.l_card.setVisible(False)
        self.card.Register.clicked.connect(self.on_register_switched)
        self.r_card.RegisterB.clicked.connect(self.on_register_button_clicked)
        self.signals = Signals()
        self.signals.message_received.connect(self.on_server_responded)
        self.client = WebSocketClient()

    @Slot()
    def on_register_switched(self):
        self.card.setVisible(False)
        self.r_card.setVisible(True)

    @Slot()
    def on_register_button_clicked(self):
        username = self.r_card.Username.text()
        password = self.r_card.Password.text()
        password2 = self.r_card.PasswordLineEdit.text()
        if password2 == password:
            self.client.send_message(MessageChain([AccountElement(username, 'register', password, get_computer_id())]))
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
        self.client.send_message(MessageChain([AccountElement(username, 'login', password, get_computer_id())]))

    @Slot()
    def on_server_responded(self, msg: MessageChainInstance):
        msg.serialize()
        if ResponseElements in msg.messages:
            status = [_ for _ in msg.messages if isinstance(_, ResponseElements)][0]
            ret_code = status.ret_code
            if status.Meta.flag == "login":
                if ret_code == 0:
                    InfoBar.success(
                        title='成功',
                        content="登录成功"+status.msg,
                        orient=Qt.Vertical,
                        isClosable=True,
                        position=InfoBarPosition.TOP,
                        duration=-1,
                        parent=self.l_card,
                    )
                    self.card.setVisible(False)
                    self.l_card.setVisible(True)
                else:
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
            if status.Meta.flag == "register":
                if ret_code == 0:
                    InfoBar.success(
                        title='成功',
                        content="注册成功, 已为您登录"+status.msg,
                        orient=Qt.Vertical,
                        isClosable=True,
                        position=InfoBarPosition.TOP,
                        duration=-1,
                        parent=self.l_card,
                    )
                    self.r_card.setVisible(False)
                    self.l_card.setVisible(True)
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




