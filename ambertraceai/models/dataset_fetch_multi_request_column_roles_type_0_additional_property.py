from enum import Enum


class DatasetFetchMultiRequestColumnRolesType0AdditionalProperty(str, Enum):
    AUXILIARY = "auxiliary"
    CORE = "core"

    def __str__(self) -> str:
        return str(self.value)
