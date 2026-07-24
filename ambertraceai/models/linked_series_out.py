from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedSeriesOut")


@_attrs_define
class LinkedSeriesOut:
    """A series linked to an entity.

    Attributes:
        name (str):
        connector_type (str | Unset):  Default: ''.
        relation_type (str | Unset):  Default: ''.
        tenor (None | str | Unset):
    """

    name: str
    connector_type: str | Unset = ""
    relation_type: str | Unset = ""
    tenor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        connector_type = self.connector_type

        relation_type = self.relation_type

        tenor: None | str | Unset
        if isinstance(self.tenor, Unset):
            tenor = UNSET
        else:
            tenor = self.tenor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if connector_type is not UNSET:
            field_dict["connector_type"] = connector_type
        if relation_type is not UNSET:
            field_dict["relation_type"] = relation_type
        if tenor is not UNSET:
            field_dict["tenor"] = tenor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        connector_type = d.pop("connector_type", UNSET)

        relation_type = d.pop("relation_type", UNSET)

        def _parse_tenor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenor = _parse_tenor(d.pop("tenor", UNSET))

        linked_series_out = cls(
            name=name,
            connector_type=connector_type,
            relation_type=relation_type,
            tenor=tenor,
        )

        linked_series_out.additional_properties = d
        return linked_series_out

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
