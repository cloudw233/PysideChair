from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget, QFrame, QHBoxLayout)

from qfluentwidgets import (BodyLabel, CardWidget, ElevatedCardWidget, LineEdit,
    PasswordLineEdit, PrimaryPushButton, PushButton, SimpleCardWidget)

class RegisterCard(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("registerCard")
        self.resize(612, 683)
        self.RegisterB = PrimaryPushButton(self)
        self.RegisterB.setObjectName(u"RegisterB")
        self.RegisterB.setGeometry(QRect(370, 370, 153, 32))
        self.RegisterB.setAutoDefault(False)
        self.RegisterB.setFlat(False)
        self.RegisterB.setProperty("hasIcon", False)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 170, 421, 188))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.BodyLabel = BodyLabel(self.layoutWidget)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.verticalLayout.addWidget(self.BodyLabel)

        self.Username = LineEdit(self.layoutWidget)
        self.Username.setObjectName(u"Username")

        self.verticalLayout.addWidget(self.Username)

        self.BodyLabel_2 = BodyLabel(self.layoutWidget)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.verticalLayout.addWidget(self.BodyLabel_2)

        self.Password = PasswordLineEdit(self.layoutWidget)
        self.Password.setObjectName(u"Password")

        self.verticalLayout.addWidget(self.Password)

        self.BodyLabel_3 = BodyLabel(self.layoutWidget)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.verticalLayout.addWidget(self.BodyLabel_3)

        self.PasswordLineEdit = PasswordLineEdit(self.layoutWidget)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")

        self.verticalLayout.addWidget(self.PasswordLineEdit)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.RegisterB.setText(QCoreApplication.translate("self", "注册", None))
        self.BodyLabel.setText(QCoreApplication.translate("self", "用户名", None))
        self.Username.setInputMask("")
        self.Username.setText("")
        self.BodyLabel_2.setText(QCoreApplication.translate("self", "密码", None))
        self.Password.setInputMask("")
        self.Password.setText("")
        self.BodyLabel_3.setText(QCoreApplication.translate("self", "确认密码", None))
