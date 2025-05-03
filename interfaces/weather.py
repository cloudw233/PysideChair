from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt, QRectF)
from PySide6.QtGui import (QIcon, QLinearGradient, QColor, QBrush, QPainterPath, QPainter, QPixmap)
from PySide6.QtWidgets import (QFrame, QGridLayout, QLayout,
                               QSizePolicy, QVBoxLayout, QWidget, QStackedWidget,
                               QLabel)
from qasync import asyncSlot

from qfluentwidgets import (CaptionLabel, CardWidget, ElevatedCardWidget, IconWidget,
                            SmoothScrollArea, SubtitleLabel, TitleLabel,
                            Pivot, qrouter, SegmentedWidget, ScrollArea, FluentIcon)
from assets.chair import qtchair_rc
from assets.weather import weather_rc
from components.cards.link import LinkCardView
from components.cards.sample import SampleCardView
from core.builtins.elements import WeatherElements, WeatherInfoElements
from core.builtins.message_constructors import MessageChainInstance
from core.signals import Signals
from core.utils import is_daytime


qss = """
SettingInterface,
#view {
    background-color: transparent;
}

QScrollArea {
    border: none;
    background-color: transparent;
}


BannerWidget > #galleryLabel {
    font: 42px 'Segoe UI SemiBold', 'Microsoft YaHei SemiBold';
    background-color: transparent;
    color: black;
    padding-left: 28px;
}
"""


class Banner(QWidget):
    """ Banner widget """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(336)
        self.setObjectName("weatherInterface")

        self.vBoxLayout = QVBoxLayout(self)
        self.banner = QPixmap('./assets/chair/weather_background.jpeg')
        self.linkCardView = LinkCardView(self)
        self.weather7dLabel = SubtitleLabel('七日天气', self)
        self.weather7dLabel.setObjectName('weather7d')

        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(36, 20, 0, 0)
        self.vBoxLayout.addWidget(self.weather7dLabel)
        self.vBoxLayout.addWidget(self.linkCardView)
        self.vBoxLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

    @asyncSlot(MessageChainInstance)
    async def setup(self, message: MessageChainInstance):
        _message: WeatherInfoElements = [i for i in message.serialize() if i.Meta.type == 'WeatherInfoElement'][0]
        for icon, title, content, url, index in zip(
                [f"./assets/weather/{_.get("iconDay") if is_daytime() else _.get("iconNight")}.svg" for _ in _message.daily],
                [_.get("textDay") if is_daytime() else _.get("textNight") for _ in _message.daily],
                [f"{_.get("tempMin")}℃-{_.get("tempMax")}℃" for _ in _message.daily],
                ["https://www.qweather.com/"]*7,
                [i for i in range(7)]
        ):
            self.linkCardView.addCard(icon, title, content, url)

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(
            QPainter.SmoothPixmapTransform | QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        w, h = self.width(), self.height()
        path.addRoundedRect(QRectF(0, 0, w, h), 10, 10)
        path.addRect(QRectF(0, h - 50, 50, 50))
        path.addRect(QRectF(w - 50, 0, 50, 50))
        path.addRect(QRectF(w - 50, h - 50, 50, 50))
        path = path.simplified()

        # init linear gradient effect
        gradient = QLinearGradient(0, 0, 0, h)

        # draw background color
        gradient.setColorAt(0, QColor(207, 216, 228, 255))
        gradient.setColorAt(1, QColor(207, 216, 228, 0))

        painter.fillPath(path, QBrush(gradient))

        # draw banner image
        pixmap = self.banner.scaled(
            self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        painter.fillPath(path, QBrush(pixmap))


class Weather(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.banner = Banner(self)
        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)
        signals_ = Signals()
        signals_.message_received.connect(self.loadSamples)
        signals_.message_received.connect(self.banner.setup)

        self.__initWidget()

    def __initWidget(self):
        self.view.setObjectName('view')
        self.setObjectName('homeInterface')
        self.setStyleSheet(qss)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 36)
        self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.addWidget(self.banner)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

    @asyncSlot(MessageChainInstance)
    async def loadSamples(self, message: MessageChainInstance):
        """ load samples """
        # basic input samples
        indicesView = SampleCardView(
            "天气指数", self.view)
        _message: WeatherInfoElements = [i for i in message.serialize() if i.Meta.type == 'WeatherInfoElement'][0]
        indices = _message.indices
        for icon, title, content, url, index in zip(
                ["./assets/weather/qweather.svg"] * len(indices),
                [_.get("name") for _ in indices],
                [f"{_.get('level')} {_.get('text')}" for _ in indices],
                ["https://www.qweather.com/"]* len(indices),
                [i for i in range(len(indices))]
        ):
            indicesView.addSampleCard(icon, title, content, index, url)
        self.vBoxLayout.addWidget(indicesView)
