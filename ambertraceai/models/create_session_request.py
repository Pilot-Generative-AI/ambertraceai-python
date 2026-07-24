from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSessionRequest")


@_attrs_define
class CreateSessionRequest:
    """
    Attributes:
        platform_id (int): Verified agent-policy platform to bind to
        goal (None | str | Unset): The task given to the (untrusted) agent
    """

    platform_id: int
    goal: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_id = self.platform_id

        goal: None | str | Unset
        if isinstance(self.goal, Unset):
            goal = UNSET
        else:
            goal = self.goal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform_id": platform_id,
            }
        )
        if goal is not UNSET:
            field_dict["goal"] = goal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform_id = d.pop("platform_id")

        def _parse_goal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        goal = _parse_goal(d.pop("goal", UNSET))

        create_session_request = cls(
            platform_id=platform_id,
            goal=goal,
        )

        create_session_request.additional_properties = d
        return create_session_request

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
