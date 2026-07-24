from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKeyRequest")


@_attrs_define
class CreateKeyRequest:
    """
    Attributes:
        expires_at (datetime.datetime | None | Unset):
        name (str | Unset):  Default: 'Default'.
        platform_id (int | None | Unset):
        scope (str | Unset):  Default: 'platform'.
    """

    expires_at: datetime.datetime | None | Unset = UNSET
    name: str | Unset = "Default"
    platform_id: int | None | Unset = UNSET
    scope: str | Unset = "platform"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        name = self.name

        platform_id: int | None | Unset
        if isinstance(self.platform_id, Unset):
            platform_id = UNSET
        else:
            platform_id = self.platform_id

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if name is not UNSET:
            field_dict["name"] = name
        if platform_id is not UNSET:
            field_dict["platform_id"] = platform_id
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        name = d.pop("name", UNSET)

        def _parse_platform_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        platform_id = _parse_platform_id(d.pop("platform_id", UNSET))

        scope = d.pop("scope", UNSET)

        create_key_request = cls(
            expires_at=expires_at,
            name=name,
            platform_id=platform_id,
            scope=scope,
        )

        create_key_request.additional_properties = d
        return create_key_request

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
