import json
from datetime import datetime
from enum import Enum
from typing import cast


class RuleInputType(Enum):
    VALUE = 1
    REFERENCE = 2


class UtilityType(Enum):
    WATER = 1
    ELECTRICITY = 2
    OIL = 3
    GAS = 4


class ConsumptionIntervalType(Enum):
    HOURLY = 1
    DAILY = 2
    WEEKLY = 3
    MONTHLY = 4


class RuleInput:
    type: RuleInputType
    value: None

    def __init__(self, value, input_type=RuleInputType.VALUE):
        self.type = input_type
        self.value = value


class RuleOutput:
    def __init__(self, value):
        self.value = value


class Variable:
    name: str = ''
    value = ''


class Rule:

    def __init__(self, function):
        self.function = function
        self.inputs: list[RuleInput] = []
        self.outputs: list[RuleOutput] = []


class RuleSet:

    # @staticmethod
    # def from_json(document):
    #     data = json.loads(document)
    #     instance = MyClass(data['value'])
    #     return instance

    def __init__(self):
        self.rules: list[Rule] = []


class ConsumptionData:
    def __init__(self, date: datetime, value: float):
        self.date = date
        self.value = value

    date: datetime
    value: float


class Methods:
    @staticmethod
    def load_consumption_range(building_id: int, utility_type: UtilityType, start_date: datetime, end_date: datetime,
                               interval: ConsumptionIntervalType) -> list[ConsumptionData]:
        return [ConsumptionData(datetime.now(), 10), ConsumptionData(datetime.now(), 40),
                ConsumptionData(datetime.now(), 20), ConsumptionData(datetime.now(), 30)]

    @staticmethod
    def find_max_consumption(values: list[ConsumptionData]) -> ConsumptionData:
        max_value = None
        for value in values:
            if max_value is None or value.value > max_value.value:
                max_value = value
        return max_value

    @staticmethod
    def greater_than(v1, v2) -> bool:
        if isinstance(v1, ConsumptionData):
            cd = cast(ConsumptionData, v1)
            value1 = cd.value
        else:
            value1 = v1

        if isinstance(v2, ConsumptionData):
            cd = cast(ConsumptionData, v2)
            value2 = cd.value
        else:
            value2 = v2

        return value1 > value2

    @staticmethod
    def smaller_than(v1, v2) -> bool:
        if isinstance(v1, ConsumptionData):
            cd = cast(ConsumptionData, v1)
            value1 = cd.value
        else:
            value1 = v1

        if isinstance(v2, ConsumptionData):
            cd = cast(ConsumptionData, v2)
            value2 = cd.value
        else:
            value2 = v2

        return value1 < value2

    @staticmethod
    def evaluate_result(result: bool):
        if result:
            print('ALERT: add alert to table or something')
