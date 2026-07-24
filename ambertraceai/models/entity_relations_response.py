from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_relations_response_relations_item import EntityRelationsResponseRelationsItem


T = TypeVar("T", bound="EntityRelationsResponse")


@_attrs_define
class EntityRelationsResponse:
    """Relations derived from entity-linked datasets (the declared_relations shape).

    Attributes:
        relations (list[EntityRelationsResponseRelationsItem] | Unset):
    """

    relations: list[EntityRelationsResponseRelationsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.relations, Unset):
            relations = []
            for relations_item_data in self.relations:
                relations_item = relations_item_data.to_dict()
                relations.append(relations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if relations is not UNSET:
            field_dict["relations"] = relations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_relations_response_relations_item import EntityRelationsResponseRelationsItem

        d = dict(src_dict)
        _relations = d.pop("relations", UNSET)
        relations: list[EntityRelationsResponseRelationsItem] | Unset = UNSET
        if _relations is not UNSET:
            relations = []
            for relations_item_data in _relations:
                relations_item = EntityRelationsResponseRelationsItem.from_dict(relations_item_data)

                relations.append(relations_item)

        entity_relations_response = cls(
            relations=relations,
        )

        entity_relations_response.additional_properties = d
        return entity_relations_response

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
