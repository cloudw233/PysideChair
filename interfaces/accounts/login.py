from PIL.ImageQt import QPixmap
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtWidgets import (QVBoxLayout, QWidget, QFrame, QHBoxLayout)

from qfluentwidgets import (AvatarWidget, LineEdit, PasswordLineEdit, PrimaryPushButton, PushButton,
                            SimpleCardWidget, SubtitleLabel)

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
        self.UsrnameXD = SubtitleLabel(self.layoutWidget)
        self.UsrnameXD.setObjectName("UsrnameXD")
        self.UsrnameXD.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.UsrnameXD)

        self.Username = LineEdit(self.layoutWidget)
        self.Username.setObjectName("Username")

        self.verticalLayout.addWidget(self.Username)

        self.PasswordXD = SubtitleLabel(self.layoutWidget)
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
        self.hBoxLayout.addWidget(self.card, Qt.AlignCenter)
