from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DecisionLogicSummary")


@_attrs_define
class DecisionLogicSummary:
    """Summary counts for the decision-logic map.

    Attributes:
        classifier_count (int | Unset):  Default: 0.
        declared_outcome_count (int | Unset):  Default: 0.
        unreachable_outcome_count (int | Unset):  Default: 0.
        verdict_count (int | Unset):  Default: 0.
    """

    classifier_count: int | Unset = 0
    declared_outcome_count: int | Unset = 0
    unreachable_outcome_count: int | Unset = 0
    verdict_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        classifier_count = self.classifier_count

        declared_outcome_count = self.declared_outcome_count

        unreachable_outcome_count = self.unreachable_outcome_count

        verdict_count = self.verdict_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classifier_count is not UNSET:
            field_dict["classifier_count"] = classifier_count
        if declared_outcome_count is not UNSET:
            field_dict["declared_outcome_count"] = declared_outcome_count
        if unreachable_outcome_count is not UNSET:
            field_dict["unreachable_outcome_count"] = unreachable_outcome_count
        if verdict_count is not UNSET:
            field_dict["verdict_count"] = verdict_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        classifier_count = d.pop("classifier_count", UNSET)

        declared_outcome_count = d.pop("declared_outcome_count", UNSET)

        unreachable_outcome_count = d.pop("unreachable_outcome_count", UNSET)

        verdict_count = d.pop("verdict_count", UNSET)

        decision_logic_summary = cls(
            classifier_count=classifier_count,
            declared_outcome_count=declared_outcome_count,
            unreachable_outcome_count=unreachable_outcome_count,
            verdict_count=verdict_count,
        )

        decision_logic_summary.additional_properties = d
        return decision_logic_summary

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
