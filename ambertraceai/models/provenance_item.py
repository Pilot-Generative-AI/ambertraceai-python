from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.provenance_item_edge import ProvenanceItemEdge
    from ..models.provenance_item_node import ProvenanceItemNode


T = TypeVar("T", bound="ProvenanceItem")


@_attrs_define
class ProvenanceItem:
    """A single provenance item (node + edge) in a decision's provenance tree.

    Attributes:
        edge (ProvenanceItemEdge):
        node (ProvenanceItemNode):
        relation_type (str):
    """

    edge: ProvenanceItemEdge
    node: ProvenanceItemNode
    relation_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edge = self.edge.to_dict()

        node = self.node.to_dict()

        relation_type = self.relation_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edge": edge,
                "node": node,
                "relation_type": relation_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provenance_item_edge import ProvenanceItemEdge
        from ..models.provenance_item_node import ProvenanceItemNode

        d = dict(src_dict)
        edge = ProvenanceItemEdge.from_dict(d.pop("edge"))

        node = ProvenanceItemNode.from_dict(d.pop("node"))

        relation_type = d.pop("relation_type")

        provenance_item = cls(
            edge=edge,
            node=node,
            relation_type=relation_type,
        )

        provenance_item.additional_properties = d
        return provenance_item

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
