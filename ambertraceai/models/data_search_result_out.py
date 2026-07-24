from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSearchResultOut")


@_attrs_define
class DataSearchResultOut:
    """A single search result (connector or series).

    Attributes:
        connector_type (str):
        description (str):
        level (str): 'connector' or 'series'
        name (str):
        asset_classes (list[str] | Unset):
        countries (list[str] | Unset):
        currencies (list[str] | Unset):
        tenor (None | str | Unset):
    """

    connector_type: str
    description: str
    level: str
    name: str
    asset_classes: list[str] | Unset = UNSET
    countries: list[str] | Unset = UNSET
    currencies: list[str] | Unset = UNSET
    tenor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        description = self.description

        level = self.level

        name = self.name

        asset_classes: list[str] | Unset = UNSET
        if not isinstance(self.asset_classes, Unset):
            asset_classes = self.asset_classes

        countries: list[str] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        currencies: list[str] | Unset = UNSET
        if not isinstance(self.currencies, Unset):
            currencies = self.currencies

        tenor: None | str | Unset
        if isinstance(self.tenor, Unset):
            tenor = UNSET
        else:
            tenor = self.tenor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connector_type": connector_type,
                "description": description,
                "level": level,
                "name": name,
            }
        )
        if asset_classes is not UNSET:
            field_dict["asset_classes"] = asset_classes
        if countries is not UNSET:
            field_dict["countries"] = countries
        if currencies is not UNSET:
            field_dict["currencies"] = currencies
        if tenor is not UNSET:
            field_dict["tenor"] = tenor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_type = d.pop("connector_type")

        description = d.pop("description")

        level = d.pop("level")

        name = d.pop("name")

        asset_classes = cast(list[str], d.pop("asset_classes", UNSET))

        countries = cast(list[str], d.pop("countries", UNSET))

        currencies = cast(list[str], d.pop("currencies", UNSET))

        def _parse_tenor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenor = _parse_tenor(d.pop("tenor", UNSET))

        data_search_result_out = cls(
            connector_type=connector_type,
            description=description,
            level=level,
            name=name,
            asset_classes=asset_classes,
            countries=countries,
            currencies=currencies,
            tenor=tenor,
        )

        data_search_result_out.additional_properties = d
        return data_search_result_out

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
