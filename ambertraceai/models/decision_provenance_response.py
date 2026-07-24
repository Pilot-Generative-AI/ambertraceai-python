from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decision_provenance_response_decision import DecisionProvenanceResponseDecision
    from ..models.provenance_item import ProvenanceItem


T = TypeVar("T", bound="DecisionProvenanceResponse")


@_attrs_define
class DecisionProvenanceResponse:
    """Response for decision provenance navigation.

    Attributes:
        decision (DecisionProvenanceResponseDecision):
        provenance (list[ProvenanceItem] | Unset):
    """

    decision: DecisionProvenanceResponseDecision
    provenance: list[ProvenanceItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        decision = self.decision.to_dict()

        provenance: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.provenance, Unset):
            provenance = []
            for provenance_item_data in self.provenance:
                provenance_item = provenance_item_data.to_dict()
                provenance.append(provenance_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "decision": decision,
            }
        )
        if provenance is not UNSET:
            field_dict["provenance"] = provenance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.decision_provenance_response_decision import DecisionProvenanceResponseDecision
        from ..models.provenance_item import ProvenanceItem

        d = dict(src_dict)
        decision = DecisionProvenanceResponseDecision.from_dict(d.pop("decision"))

        _provenance = d.pop("provenance", UNSET)
        provenance: list[ProvenanceItem] | Unset = UNSET
        if _provenance is not UNSET:
            provenance = []
            for provenance_item_data in _provenance:
                provenance_item = ProvenanceItem.from_dict(provenance_item_data)

                provenance.append(provenance_item)

        decision_provenance_response = cls(
            decision=decision,
            provenance=provenance,
        )

        decision_provenance_response.additional_properties = d
        return decision_provenance_response

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
