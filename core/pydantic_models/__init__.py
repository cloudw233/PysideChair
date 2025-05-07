from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict
from typing import Literal, Union, TypedDict

class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(strict=True)


class Account(BaseModel):
    username: str
    action: Literal["login", "register", "data"]
    password: Union[str, int] = None
    device_id: str = ' '
    key: str = ' '
    face_recognition_data: str = None

class Smoke(TypedDict):
    MQ_2: bool
    MQ_4: bool
    MQ_5: bool
    MQ_7: bool
    MQ_9: bool
    MQ_135: bool

class Sensor(BaseModel):
    temp: float = None
    humidity: float = None
    power: float = None
    urgent_button: bool = None
    tilt: bool = None
    heart_data: int = None
    smoke: Smoke = None
    seat: int = None


class Weather(BaseModel):
    city: str

class Indices(TypedDict):
    date: str
    type: str
    name: str
    level: str
    category: str
    text: str

class WeatherDaily(TypedDict):
    fxDate: str
    sunrise: str
    sunset: str
    moonrise: str
    moonset: str
    moonPhase: str
    moonPhaseIcon: str
    tempMax: str
    tempMin: str
    iconDay: str
    textDay: str
    iconNight: str
    textNight: str
    wind360Day: str
    windDirDay: str
    windScaleDay: str
    windSpeedDay: str
    wind360Night: str
    windDirNight: str
    windScaleNight: str
    windSpeedNight: str
    humidity: str
    precip: str
    pressure: str
    vis: str
    cloud: str
    uvIndex: str

class WeatherInfo(BaseModel):
    indices: list[Indices]
    daily: list[WeatherDaily]
    city: str
    city_id: str
    lat: str
    lon: str


class UI(BaseModel):
    seat: float | int

class Heart(BaseModel):
    bpm: int

class DeepSeek(BaseModel):
    question: str

class DeepSeekAnswer(BaseModel):
    question: str
    answer: str

__all__ = [
    'Account',
    'Sensor',
    'Smoke',
    'Indices',
    'WeatherDaily',
    'Weather',
    'WeatherInfo',
    'UI',
    'Heart',
    'DeepSeek',
    'DeepSeekAnswer'
]
