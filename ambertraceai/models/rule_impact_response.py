from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rule_impact_response_decisions_item import RuleImpactResponseDecisionsItem


T = TypeVar("T", bound="RuleImpactResponse")


@_attrs_define
class RuleImpactResponse:
    """Response for rule impact analysis: decisions that depend on a rule.

    Attributes:
        rule_name (str):
        decisions (list[RuleImpactResponseDecisionsItem] | Unset):
        total (int | Unset):  Default: 0.
    """

    rule_name: str
    decisions: list[RuleImpactResponseDecisionsItem] | Unset = UNSET
    total: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_name = self.rule_name

        decisions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.decisions, Unset):
            decisions = []
            for decisions_item_data in self.decisions:
                decisions_item = decisions_item_data.to_dict()
                decisions.append(decisions_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_name": rule_name,
            }
        )
        if decisions is not UNSET:
            field_dict["decisions"] = decisions
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rule_impact_response_decisions_item import RuleImpactResponseDecisionsItem

        d = dict(src_dict)
        rule_name = d.pop("rule_name")

        _decisions = d.pop("decisions", UNSET)
        decisions: list[RuleImpactResponseDecisionsItem] | Unset = UNSET
        if _decisions is not UNSET:
            decisions = []
            for decisions_item_data in _decisions:
                decisions_item = RuleImpactResponseDecisionsItem.from_dict(decisions_item_data)

                decisions.append(decisions_item)

        total = d.pop("total", UNSET)

        rule_impact_response = cls(
            rule_name=rule_name,
            decisions=decisions,
            total=total,
        )

        rule_impact_response.additional_properties = d
        return rule_impact_response

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
