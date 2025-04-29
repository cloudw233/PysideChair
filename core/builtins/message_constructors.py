from copy import deepcopy
from typing import Union

from extensions.deepseek import get_deepseek_anwser
from extensions.weather import QWeather
from .assigned_element import *


class MessageChainInstance:
    messages: Union[list[Union[
        AccountElement,
        SensorElement,
        WeatherElement,
        WeatherInfoElement,
        UIElement,
        HeartElement,
        DeepSeekElement,
        DeepSeekAnswerElement,
        ResponseElement]], list[dict]
    ] = None
    serialized: bool = None

    def deserialize(self):
        if not self.serialized:
            return self.messages
        self.messages = [{"meta": element.Meta.type, "data": element.dump()} for element in self.messages]
        self.serialized = False
        return self.messages

    def serialize(self):
        if self.serialized:
            return self.messages
        msg_chain_lst = []
        for meta, data in enumerate(self.messages):
            match meta:
                case "AccountElement":
                    msg_chain_lst.append(AccountElement(**data))
                case "SensorElement":
                    msg_chain_lst.append(SensorElement(**data))
                case "WeatherElement":
                    msg_chain_lst.append(WeatherElement(**data))
                case "WeatherInfoElement":
                    msg_chain_lst.append(WeatherInfoElement(**data))
                case "UIElement":
                    msg_chain_lst.append(UIElement(**data))
                case "HeartElement":
                    msg_chain_lst.append(HeartElement(**data))
                case "DeepSeekElement":
                    msg_chain_lst.append(DeepSeekElement(**data))
                case "DeepSeekAnswerElement":
                    msg_chain_lst.append(DeepSeekAnswerElement(**data))
                case "ResponseElement":
                    msg_chain_lst.append(ResponseElement(**data))
                case _:
                    assert False, "Unknown message type: {meta}"

    @classmethod
    def assign(cls,
               elements: list[Union[
                   AccountElement,
                   SensorElement,
                   WeatherElement,
                   WeatherInfoElement,
                   UIElement,
                   HeartElement,
                   DeepSeekElement,
                   DeepSeekAnswerElement,
                   ResponseElement]]) -> "MessageChain":
        cls.serialized = True
        cls.messages = elements
        return deepcopy(cls())

    @classmethod
    def assign_deserialized(cls, elements: list[dict]) -> "MessageChain":
        cls.serialized = False
        cls.messages = elements
        return deepcopy(cls())


async def process_message(httpx_client, message_lst, msgchain):
    for element in msgchain.messages:
        match element.Meta.type:
            case "WeatherElement":
                message_lst.append(QWeather(httpx_client).get_weather_element(element))
            case "DeepSeekElement":
                __answer = await get_deepseek_anwser(element.question)
                message_lst.append(
                    DeepSeekAnswerElement(
                        answer=__answer,
                        question=element.question,
                    ))
            case _:
                message_lst.append(element)
    message_lst.append(ResponseElement(ret_code=0, msg="Data received"))

MessageChain = MessageChainInstance.assign
MessageChainD = MessageChainInstance.assign_deserialized

__all__ = ["MessageChain", "MessageChainD", "process_message"]