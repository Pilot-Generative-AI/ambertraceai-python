from enum import Enum


class EvalCalculationTypeType0(str, Enum):
    CUSTOM = "custom"
    FIELD_AGGREGATE = "field_aggregate"
    SQL_EXPRESSION = "sql_expression"

    def __str__(self) -> str:
        return str(self.value)
