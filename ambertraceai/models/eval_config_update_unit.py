from enum import Enum


class EvalConfigUpdateUnit(str, Enum):
    COUNT = "count"
    CURRENCY = "currency"
    OTHER = "other"
    PERCENTAGE = "percentage"
    RATE = "rate"
    RATIO = "ratio"
    SCORE = "score"

    def __str__(self) -> str:
        return str(self.value)
