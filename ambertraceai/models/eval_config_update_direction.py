from enum import Enum


class EvalConfigUpdateDirection(str, Enum):
    MAXIMIZE = "maximize"
    MINIMIZE = "minimize"
    SEPARATE = "separate"

    def __str__(self) -> str:
        return str(self.value)
