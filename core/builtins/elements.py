import attrs
import orjson as json
from typing import Literal, Union

from core.pydantic_models import *
from copy import deepcopy
from attrs import define


@define
class AccountElements:
    """
    账号元素
    """
    username: str
    action: Literal["login", "register", "data"]
    password: Union[str, int] = 0
    face_recognition_data: str = ' '

    class Meta:
        type = "AccountElement"

    @classmethod
    def assign(
            cls,
            username: str,
            action: Literal["login", "register", "data"],
            password: Union[str, int] = 0,
            face_recognition_data: str = ' '
    ):
        """
        账户元素
        :param username: 用户名
        :param action: 操作
        :param password: 密码
        :param face_recognition_data: 人脸验证数据
        :return: AccountElement类
        """
        model = Account(
            username=username,
            action=action,
            password=password,
            face_recognition_data=face_recognition_data
        )
        return deepcopy(cls(
            username=model.username,
            action=model.action,
            password=model.password,
            face_recognition_data=model.face_recognition_data
        ))

    def dump(self):
        return {
            field.name: getattr(self, field.name)
            for field in attrs.fields(self.__class__)
        }


@define
class SensorElements:
    """
    传感器元素
    """
    temp: float = None
    humidity: float = None
    power: float = None
    urgent_button: bool = None
    tilt: bool = None
    heart_data: int = None
    smoke: Smoke = None
    seat: int = None

    class Meta:
        type = "SensorElement"

    @classmethod
    def assign(
            cls,
            temp: float = None,
            humidity: float = None,
            power: float = None,
            urgent_button: bool = None,
            tilt: bool = None,
            heart_data: int = None,
            smoke: Smoke = None,
            seat: int = None
    ):
        """
        传感器元素
        :param temp: 温度
        :param humidity: 湿度
        :param power: 电量
        :param urgent_button: 紧急按钮
        :param tilt: 倾斜角度
        :param heart_data: 心率数据
        :param smoke: 烟雾数据
        :param seat: 座位角度
        :return:
        """
        model = Sensor(
            temp=temp,
            humidity=humidity,
            power=power,
            urgent_button=urgent_button,
            tilt=tilt,
            heart_data=heart_data,
            smoke=smoke,
            seat=seat
        )
        return deepcopy(cls(
            temp=model.temp,
            humidity=model.humidity,
            power=model.power,
            urgent_button=model.urgent_button,
            tilt=model.tilt,
            heart_data=model.heart_data,
            smoke=model.smoke,
            seat=model.seat
        ))

    def dump(self):
        return {
            field.name: getattr(self, field.name)
            for field in attrs.fields(self.__class__)
        }


@define
class WeatherElements:
    """
    天气元素
    """
    city: str

    class Meta:
        type = "WeatherElement"

    @classmethod
    def assign(
            cls,
            city: str
    ):
        """
        天气元素
        :param city: 城市
        :return:
        """
        model = Weather(city=city)
        return deepcopy(cls(
            city=model.city
        ))

    def dump(self):
        return {
            field.name: getattr(self, field.name)
            for field in attrs.fields(self.__class__)
        }


@define
class WeatherInfoElements:
    """
    天气信息元素
    """
    indices: list[Indices]
    daily: list[WeatherDaily]
    city: str
    city_id: str
    lat: str
    lon: str

    class Meta:
        type = "WeatherInfoElement"

    @classmethod
    def assign(
            cls,
            indices: list[Indices],
            daily: list[WeatherDaily],
            city: str,
            city_id: str,
            lat: str,
            lon: str
    ):
        """
        天气信息元素
        :param indices: 生活指数
        :param daily: 未来7天天气预报
        :param city: 城市
        :param city_id: 城市ID
        :param lat: 纬度
        :param lon: 经度
        :return:
        """
        model = WeatherInfo(
            indices=indices,
            daily=daily,
            city=city,
            city_id=city_id,
            lat=lat,
            lon=lon
        )
        return deepcopy(cls(
            indices=model.indices,
            daily=model.daily,
            city=model.city,
            city_id=model.city_id,
            lat=model.lat,
            lon=model.lon
        ))

    def dump(self):
        return {
            field.name: getattr(self, field.name)
            for field in attrs.fields(self.__class__)
        }


@define
class UIElements:
    """
    UI元素
    """
    seat: float | int

    class Meta:
        type = "UIElement"

    @classmethod
    def assign(
            cls,
            seat: float | int
    ):
        """
        UI元素
        :param seat: 座位角度
        :return:
        """
        model = UI(seat=seat)
        return deepcopy(cls(
            seat=model.seat
        ))

    def dump(self):
        return {
            field.name: getattr(self, field.name)
            for field in attrs.fields(self.__class__)
        }


@define
class HeartElements:
    """
    心率元素
    """
    bpm: int

    class Meta:
        type = "HeartElement"

    @classmethod
    def assign(
            cls,
            bpm: int
    ):
        """
        心率元素
        :param bpm: 心率
        :return:
        """
        model = Heart(bpm=bpm)
        return deepcopy(cls(
            bpm=model.bpm
        ))

    def dump(self):
        return {
            field.name: getattr(self, field.name)
            for field in attrs.fields(self.__class__)
        }


@define
class DeepSeekElements:
    """
    深度求索元素
    """
    question: str

    class Meta:
        type = "DeepSeekElement"

    @classmethod
    def assign(
            cls,
            question: str
    ):
        """
        深度学习元素
        :param question: 问题
        :return:
        """
        model = DeepSeek(question=question)
        return deepcopy(cls(
            question=model.question
        ))

    def dump(self):
        return {
            field.name: getattr(self, field.name)
            for field in attrs.fields(self.__class__)
        }


@define
class DeepSeekAnswerElements:
    """
    深度求索答案元素
    """
    question: str
    answer: str

    class Meta:
        type = "DeepSeekAnswerElement"

    @classmethod
    def assign(
            cls,
            question: str,
            answer: str
    ):
        """
        深度学习答案元素
        :param question: 问题
        :param answer: 答案
        :return:
        """
        model = DeepSeekAnswer(question=question, answer=answer)
        return deepcopy(cls(
            question=model.question,
            answer=model.answer
        ))

    def dump(self):
        return {
            field.name: getattr(self, field.name)
            for field in attrs.fields(self.__class__)
        }


@define
class ResponseElements:
    """
    响应元素
    """
    ret_code: int
    msg: str

    class Meta:
        type = "ResponseElement"

    mapping = {
        0: "Success",
        1: "Warning",
        2: "Error",
    }

    @classmethod
    def assign(
            cls,
            ret_code: Literal[0, 1, 2],
            msg: str = None
    ):
        """
        响应元素
        :param ret_code: 返回码，0:成功，1:警告，2:错误
        :param msg: 详细
        :return:
        """
        return deepcopy(cls(
            ret_code=ret_code,
            msg=f"[{cls.mapping[ret_code]}] {msg}"
        ))

    def dump(self):
        return {
            field.name: getattr(self, field.name)
            for field in attrs.fields(self.__class__)
        }


__all__ = [
    'AccountElements',
    'SensorElements',
    'WeatherElements',
    'WeatherInfoElements',
    'UIElements',
    'HeartElements',
    'DeepSeekElements',
    'DeepSeekAnswerElements',
    'ResponseElements'
]
