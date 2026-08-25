from enum import Enum


class GetJobTypeType0(str, Enum):
    BUILD = "build"
    CLEANING = "cleaning"

    def __str__(self) -> str:
        return str(self.value)
