from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QHBoxLayout
from loguru import logger
from qfluentwidgets import GroupHeaderCardWidget, PushButton, IconWidget, InfoBarIcon, \
    BodyLabel, PrimaryPushButton, FluentIcon, LineEdit, InfoBar, InfoBarPosition

from config import set_config, config


class SettingsCard(GroupHeaderCardWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("settingsInterface")
        self.setTitle("基本设置")
        self.setBorderRadius(8)

        self.lineEdit = LineEdit(self)
        self.lineEdit2 = LineEdit(self)
        self.lineEdit.setText(config("city"))
        self.lineEdit2.setText(config("ws_server"))

        self.hintIcon = IconWidget(InfoBarIcon.INFORMATION)
        self.hintLabel = BodyLabel("点击保存👉")
        self.saveButton = PrimaryPushButton(FluentIcon.SAVE, "保存")
        self.resetButton = PushButton(FluentIcon.CANCEL, "重置")
        self.bottomLayout = QHBoxLayout()

        self.lineEdit.setFixedWidth(320)
        self.lineEdit2.setFixedWidth(320)
        self.lineEdit.setPlaceholderText("城市名，支持中文和英文")
        self.lineEdit2.setPlaceholderText("ws://<example.com>:<port>/client")

        # 设置底部工具栏布局
        self.hintIcon.setFixedSize(16, 16)
        self.bottomLayout.setSpacing(10)
        self.bottomLayout.setContentsMargins(24, 15, 24, 20)
        self.bottomLayout.addWidget(self.hintIcon, 0, Qt.AlignLeft)
        self.bottomLayout.addWidget(self.hintLabel, 0, Qt.AlignLeft)
        self.bottomLayout.addStretch(1)
        self.bottomLayout.addWidget(self.resetButton, 0, Qt.AlignRight)
        self.bottomLayout.addWidget(self.saveButton, 0, Qt.AlignRight)
        self.bottomLayout.setAlignment(Qt.AlignVCenter)

        # 添加组件到分组中
        self.addGroup("./assets/weather/100.svg", "城市名", "设置天气使用的城市，若没有则尝试使用GPS模块数据获取", self.lineEdit)
        group = self.addGroup(FluentIcon.CLOUD_DOWNLOAD, "远程服务器地址", "设置远程服务器地址", self.lineEdit2)
        group.setSeparatorVisible(True)

        # 添加底部工具栏
        self.vBoxLayout.addLayout(self.bottomLayout)

        # 连接信号
        self.saveButton.clicked.connect(self.save_config)

    @Slot()
    def save_config(self):
        city = self.lineEdit.text()
        ws_server = self.lineEdit2.text()
        set_config("city",city)
        set_config("ws_server", ws_server)
        InfoBar.success(
            "成功",
            "配置保存成功",
            orient=Qt.Vertical,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=-1,
            parent=self
        )
        logger.success("配置保存成功")
