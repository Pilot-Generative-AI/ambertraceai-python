from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.eval_calculation_aggregate_type_0 import EvalCalculationAggregateType0
from ..models.eval_calculation_type_type_0 import EvalCalculationTypeType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="EvalCalculation")


@_attrs_define
class EvalCalculation:
    """How the target metric is computed from the customer's columns.

    Attributes:
        aggregate (EvalCalculationAggregateType0 | None | Unset): Aggregate over 'field' (type=field_aggregate);
            defaults to 'mean'.
        expression (None | str | Unset): SQL expression (type=sql_expression).
        field (None | str | Unset): Column to aggregate (type=field_aggregate).
        notes (None | str | Unset): Required for type=custom — how the metric is computed.
        type_ (EvalCalculationTypeType0 | None | Unset): Defaults to 'field_aggregate' when omitted.
    """

    aggregate: EvalCalculationAggregateType0 | None | Unset = UNSET
    expression: None | str | Unset = UNSET
    field: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    type_: EvalCalculationTypeType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregate: None | str | Unset
        if isinstance(self.aggregate, Unset):
            aggregate = UNSET
        elif isinstance(self.aggregate, EvalCalculationAggregateType0):
            aggregate = self.aggregate.value
        else:
            aggregate = self.aggregate

        expression: None | str | Unset
        if isinstance(self.expression, Unset):
            expression = UNSET
        else:
            expression = self.expression

        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, EvalCalculationTypeType0):
            type_ = self.type_.value
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregate is not UNSET:
            field_dict["aggregate"] = aggregate
        if expression is not UNSET:
            field_dict["expression"] = expression
        if field is not UNSET:
            field_dict["field"] = field
        if notes is not UNSET:
            field_dict["notes"] = notes
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_aggregate(data: object) -> EvalCalculationAggregateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                aggregate_type_0 = EvalCalculationAggregateType0(data)

                return aggregate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EvalCalculationAggregateType0 | None | Unset, data)

        aggregate = _parse_aggregate(d.pop("aggregate", UNSET))

        def _parse_expression(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expression = _parse_expression(d.pop("expression", UNSET))

        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_type_(data: object) -> EvalCalculationTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = EvalCalculationTypeType0(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EvalCalculationTypeType0 | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        eval_calculation = cls(
            aggregate=aggregate,
            expression=expression,
            field=field,
            notes=notes,
            type_=type_,
        )

        eval_calculation.additional_properties = d
        return eval_calculation

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
