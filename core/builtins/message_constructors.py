from copy import deepcopy
from typing import Union, Literal, List
from .assigned_element import *
from ..pydantic_models import Indices, WeatherDaily


class MessageChainInstance:
    messages: list = None
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
        for _ in self.messages:
            meta = _.get("meta")
            data = _.get("data")
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
                case "MachineryElement":
                    msg_chain_lst.append(MachineryElement(**data))
                case "StepperMotorElement":
                    msg_chain_lst.append(StepperMotorElement(**data))
                case "ResponseElement":
                    msg_chain_lst.append(ResponseElement(**data))
                case _:
                    assert False, f"Unknown message type: {meta}"
        self.messages = msg_chain_lst
        self.serialized = True
        return self.messages

    @classmethod
    def assign(cls,
               elements: List[
                   AccountElement,
                   SensorElement,
                   WeatherElement,
                   WeatherInfoElement,
                   UIElement,
                   HeartElement,
                   DeepSeekElement,
                   DeepSeekAnswerElement,
                   MachineryElement,
                   ResponseElement]) -> "MessageChain":
        cls.serialized = True
        cls.messages = elements
        return deepcopy(cls())

    @classmethod
    def assign_deserialized(cls, elements: list[dict]) -> "MessageChainD":
        cls.serialized = False
        cls.messages = elements
        return deepcopy(cls())


MessageChain = MessageChainInstance.assign
MessageChainD = MessageChainInstance.assign_deserialized

__all__ = ["MessageChain", "MessageChainD"]
