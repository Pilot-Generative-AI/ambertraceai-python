from enum import Enum


class DatasetDeriveRequestOp(str, Enum):
    ADD = "add"
    DIVIDE = "divide"
    MULTIPLY = "multiply"
    SUBTRACT = "subtract"

    def __str__(self) -> str:
        return str(self.value)
