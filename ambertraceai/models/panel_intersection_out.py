from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PanelIntersectionOut")


@_attrs_define
class PanelIntersectionOut:
    """
    Attributes:
        coverage_pct (float): usable_rows as a percentage of row_count.
        usable_rows (int): Rows where EVERY column is non-null -- the joint intersection.
        first_index (None | str | Unset):
        last_index (None | str | Unset):
    """

    coverage_pct: float
    usable_rows: int
    first_index: None | str | Unset = UNSET
    last_index: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        coverage_pct = self.coverage_pct

        usable_rows = self.usable_rows

        first_index: None | str | Unset
        if isinstance(self.first_index, Unset):
            first_index = UNSET
        else:
            first_index = self.first_index

        last_index: None | str | Unset
        if isinstance(self.last_index, Unset):
            last_index = UNSET
        else:
            last_index = self.last_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "coverage_pct": coverage_pct,
                "usable_rows": usable_rows,
            }
        )
        if first_index is not UNSET:
            field_dict["first_index"] = first_index
        if last_index is not UNSET:
            field_dict["last_index"] = last_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        coverage_pct = d.pop("coverage_pct")

        usable_rows = d.pop("usable_rows")

        def _parse_first_index(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_index = _parse_first_index(d.pop("first_index", UNSET))

        def _parse_last_index(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_index = _parse_last_index(d.pop("last_index", UNSET))

        panel_intersection_out = cls(
            coverage_pct=coverage_pct,
            usable_rows=usable_rows,
            first_index=first_index,
            last_index=last_index,
        )

        panel_intersection_out.additional_properties = d
        return panel_intersection_out

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
