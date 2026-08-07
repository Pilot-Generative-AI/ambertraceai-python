from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnMissingPolicy")


@_attrs_define
class OnMissingPolicy:
    """Customer-declared missing-value policy for multi-source panels (Part of #1482).

    Controls how NaN cells in the outer-joined panel are handled.

        Attributes:
            max_gap (int | Unset): Maximum contiguous NaN gap eligible for interpolation (only used when
                method='interpolate'). Gaps longer than this are NOT interpolated -- those rows are dropped. Default 3. Default:
                3.
            method (str | Unset): How to handle missing values after the outer join. 'drop' -- drop rows with any NaN (no
                fill). 'ffill' -- forward-fill (last observation carried forward; default). 'interpolate' -- linear
                interpolation for short gaps (up to max_gap contiguous NaN); longer gaps are dropped. 'proxy_splice' -- forward-
                fill + back-fill to splice proxy series; flagged as modeled_extrapolation in the transformation manifest.
                Default: 'ffill'.
    """

    max_gap: int | Unset = 3
    method: str | Unset = "ffill"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_gap = self.max_gap

        method = self.method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_gap is not UNSET:
            field_dict["max_gap"] = max_gap
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_gap = d.pop("max_gap", UNSET)

        method = d.pop("method", UNSET)

        on_missing_policy = cls(
            max_gap=max_gap,
            method=method,
        )

        on_missing_policy.additional_properties = d
        return on_missing_policy

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
