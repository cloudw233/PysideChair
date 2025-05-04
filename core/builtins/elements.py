import attrs
import orjson as json
from typing import Literal, Union

from core.pydantic_models import *
from copy import deepcopy
from attrs import define

class BaseElements:
    def dump(self):
        return {
            field.name: getattr(self, field.name)
            for field in attrs.fields(self.__class__)
        }

@define
class AccountElements(BaseElements):
    """
    账号元素
    """
    username: str
    action: Literal["login", "register", "data"]
    password: Union[str, int] = 0
    device_id: str = ' '
    key: str = ' '
    face_recognition_data: str = ' '

    class Meta:
        type = "AccountElement"

    @classmethod
    def assign(
            cls,
            username: str,
            action: Literal["login", "register", "data"],
            password: Union[str, int] = 0,
            device_id: str = ' ',
            key: str = ' ',
            face_recognition_data: str = ' '
    ):
        """
        账户元素
        :param username: 用户名
        :param action: 操作
        :param password: 密码
        :param device_id: 设备ID
        :param key: 密钥
        :param face_recognition_data: 人脸验证数据
        :return: AccountElement类
        """
        model = Account(
            username=username,
            action=action,
            password=password,
            device_id=device_id,
            key=key,
            face_recognition_data=face_recognition_data
        )
        return deepcopy(cls(
            username=model.username,
            action=model.action,
            password=model.password,
            device_id=model.device_id,
            key=model.key,
            face_recognition_data=model.face_recognition_data
        ))


@define
class SensorElements(BaseElements):
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


@define
class WeatherElements(BaseElements):
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


@define
class WeatherInfoElements(BaseElements):
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


@define
class UIElements(BaseElements):
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


@define
class HeartElements(BaseElements):
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


@define
class DeepSeekElements(BaseElements):
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


@define
class DeepSeekAnswerElements(BaseElements):
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


@define
class ResponseElements(BaseElements):
    """
    响应元素
    """
    ret_code: int
    msg: str

    class Meta:
        type = "ResponseElement"
        flag = None

    mapping = {
        0: "Success",
        1: "Warning",
        2: "Error",
    }

    @classmethod
    def assign(
            cls,
            ret_code: Literal[0, 1, 2],
            msg: str = None,
            flag: str = None
    ):
        """
        响应元素
        :param ret_code: 返回码，0:成功，1:警告，2:错误
        :param msg: 消息
        :param flag: 标志
        :return:
        """
        tempcls = deepcopy(cls(
            ret_code=ret_code,
            msg=f"[{cls.mapping[ret_code]}] {msg}"
        ))
        tempcls.Meta.flag = flag
        return tempcls


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
