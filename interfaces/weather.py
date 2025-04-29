from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt, QRectF)
from PySide6.QtGui import (QIcon, QLinearGradient, QColor, QBrush, QPainterPath, QPainter, QPixmap)
from PySide6.QtWidgets import (QFrame, QGridLayout, QLayout,
                               QSizePolicy, QVBoxLayout, QWidget, QStackedWidget,
                               QLabel)

from qfluentwidgets import (CaptionLabel, CardWidget, ElevatedCardWidget, IconWidget,
                            SmoothScrollArea, SubtitleLabel, TitleLabel,
                            Pivot, qrouter, SegmentedWidget, ScrollArea, FluentIcon)
from assets.chair import qtchair_rc
from assets.weather import weather_rc
from components.cards.link import LinkCardView
from components.cards.sample import SampleCardView

from core.ws_connect import WebSocketClient

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
        self.client = WebSocketClient
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
        self.vBoxLayout.addWidget(self.linkCardView, 1, Qt.AlignBottom)
        self.vBoxLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)


        for icon, title, content, url, index in zip(
            ["./assets/weather/100.svg"]*7,
            ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Windy', 'Foggy', 'Thunderstorm'],
            ['Clear sky', 'Partly cloudy', 'Light rain', 'Heavy snow', 'Strong winds', 'Low visibility', 'Lightning storm'],
            ['https://example.com/sunny',
             'https://example.com/cloudy',
             'https://example.com/rainy',
             'https://example.com/snowy',
             'https://example.com/windy',
             'https://example.com/foggy',
             'https://example.com/thunderstorm'],
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
        path.addRect(QRectF(0, h-50, 50, 50))
        path.addRect(QRectF(w-50, 0, 50, 50))
        path.addRect(QRectF(w-50, h-50, 50, 50))
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

        self.__initWidget()
        self.loadSamples()

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

    def loadSamples(self):
        """ load samples """
        # basic input samples
        indicesView = SampleCardView(
            "天气指数", self.view)
        for icon, title, content, url, index in zip(
                ["./assets/weather/100.svg"] * 7,
                ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Windy', 'Foggy', 'Thunderstorm'],
                ['Clear sky', 'Partly cloudy', 'Light rain', 'Heavy snow', 'Strong winds', 'Low visibility',
                 'Lightning storm'],
                ['https://example.com/sunny',
                 'https://example.com/cloudy',
                 'https://example.com/rainy',
                 'https://example.com/snowy',
                 'https://example.com/windy',
                 'https://example.com/foggy',
                 'https://example.com/thunderstorm'],
                [i for i in range(7)]
        ):
            indicesView.addSampleCard(icon, title, content, index, url)
        self.vBoxLayout.addWidget(indicesView)
