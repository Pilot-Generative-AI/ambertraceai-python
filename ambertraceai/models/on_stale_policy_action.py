from enum import Enum


class OnStalePolicyAction(str, Enum):
    DROP_COLUMNS = "drop_columns"
    ERROR = "error"
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
