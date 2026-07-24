from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedDatasetOut")


@_attrs_define
class LinkedDatasetOut:
    """A dataset linked to an entity.

    Attributes:
        name (str):
        join_key (str | Unset):  Default: ''.
        relation_name (str | Unset):  Default: ''.
        relation_type (str | Unset):  Default: ''.
    """

    name: str
    join_key: str | Unset = ""
    relation_name: str | Unset = ""
    relation_type: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        join_key = self.join_key

        relation_name = self.relation_name

        relation_type = self.relation_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if join_key is not UNSET:
            field_dict["join_key"] = join_key
        if relation_name is not UNSET:
            field_dict["relation_name"] = relation_name
        if relation_type is not UNSET:
            field_dict["relation_type"] = relation_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        join_key = d.pop("join_key", UNSET)

        relation_name = d.pop("relation_name", UNSET)

        relation_type = d.pop("relation_type", UNSET)

        linked_dataset_out = cls(
            name=name,
            join_key=join_key,
            relation_name=relation_name,
            relation_type=relation_type,
        )

        linked_dataset_out.additional_properties = d
        return linked_dataset_out

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
