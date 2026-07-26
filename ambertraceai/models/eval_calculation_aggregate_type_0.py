from enum import Enum


class EvalCalculationAggregateType0(str, Enum):
    COUNT = "count"
    MAX = "max"
    MEAN = "mean"
    MEDIAN = "median"
    MIN = "min"
    RATIO = "ratio"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
