from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessReviewRoleOut")


@_attrs_define
class AccessReviewRoleOut:
    """A single RBAC role assigned to a member in the access-review snapshot.

    Attributes:
        role_id (int):
        role_name (str):
        source (str):
        assigned_at (None | str | Unset):
    """

    role_id: int
    role_name: str
    source: str
    assigned_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_id = self.role_id

        role_name = self.role_name

        source = self.source

        assigned_at: None | str | Unset
        if isinstance(self.assigned_at, Unset):
            assigned_at = UNSET
        else:
            assigned_at = self.assigned_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role_id": role_id,
                "role_name": role_name,
                "source": source,
            }
        )
        if assigned_at is not UNSET:
            field_dict["assigned_at"] = assigned_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role_id = d.pop("role_id")

        role_name = d.pop("role_name")

        source = d.pop("source")

        def _parse_assigned_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assigned_at = _parse_assigned_at(d.pop("assigned_at", UNSET))

        access_review_role_out = cls(
            role_id=role_id,
            role_name=role_name,
            source=source,
            assigned_at=assigned_at,
        )

        access_review_role_out.additional_properties = d
        return access_review_role_out

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
