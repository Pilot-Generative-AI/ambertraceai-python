from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DecisionLogicEdge")


@_attrs_define
class DecisionLogicEdge:
    """An edge in the decision-logic DAG.

    Attributes:
        relation (str): Edge type (e.g. 'certifies' for verdict->outcome).
        source (str): Source node ID.
        target (str): Target node ID.
    """

    relation: str
    source: str
    target: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relation = self.relation

        source = self.source

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relation": relation,
                "source": source,
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        relation = d.pop("relation")

        source = d.pop("source")

        target = d.pop("target")

        decision_logic_edge = cls(
            relation=relation,
            source=source,
            target=target,
        )

        decision_logic_edge.additional_properties = d
        return decision_logic_edge

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
