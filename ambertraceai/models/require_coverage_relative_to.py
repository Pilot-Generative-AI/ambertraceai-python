from enum import Enum


class RequireCoverageRelativeTo(str, Enum):
    CORE = "core"
    PANEL = "panel"

    def __str__(self) -> str:
        return str(self.value)
