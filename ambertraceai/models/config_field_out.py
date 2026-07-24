from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigFieldOut")


@_attrs_define
class ConfigFieldOut:
    """Machine-readable descriptor for a single connector config key.

    Attributes:
        description (str):
        name (str):
        required (bool):
        type_ (str): Value type: str, int, list, bool, or dict.
        default (Any | None | Unset):
        enum (list[str] | None | Unset):
        example (Any | None | Unset):
    """

    description: str
    name: str
    required: bool
    type_: str
    default: Any | None | Unset = UNSET
    enum: list[str] | None | Unset = UNSET
    example: Any | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        required = self.required

        type_ = self.type_

        default: Any | None | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        enum: list[str] | None | Unset
        if isinstance(self.enum, Unset):
            enum = UNSET
        elif isinstance(self.enum, list):
            enum = self.enum

        else:
            enum = self.enum

        example: Any | None | Unset
        if isinstance(self.example, Unset):
            example = UNSET
        else:
            example = self.example

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
                "required": required,
                "type": type_,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if enum is not UNSET:
            field_dict["enum"] = enum
        if example is not UNSET:
            field_dict["example"] = example

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        required = d.pop("required")

        type_ = d.pop("type")

        def _parse_default(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        def _parse_enum(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enum_type_0 = cast(list[str], data)

                return enum_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        enum = _parse_enum(d.pop("enum", UNSET))

        def _parse_example(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        example = _parse_example(d.pop("example", UNSET))

        config_field_out = cls(
            description=description,
            name=name,
            required=required,
            type_=type_,
            default=default,
            enum=enum,
            example=example,
        )

        config_field_out.additional_properties = d
        return config_field_out

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
