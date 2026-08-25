from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_review_role_out import AccessReviewRoleOut


T = TypeVar("T", bound="AccessReviewMemberOut")


@_attrs_define
class AccessReviewMemberOut:
    """One member in the org-scoped access-review snapshot.

    Attributes:
        email (str):
        is_org_admin (bool):
        roles (list[AccessReviewRoleOut]):
        user_id (int):
        username (str):
        first_name (None | str | Unset):
        last_name (None | str | Unset):
    """

    email: str
    is_org_admin: bool
    roles: list[AccessReviewRoleOut]
    user_id: int
    username: str
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        is_org_admin = self.is_org_admin

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        user_id = self.user_id

        username = self.username

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "is_org_admin": is_org_admin,
                "roles": roles,
                "user_id": user_id,
                "username": username,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.access_review_role_out import AccessReviewRoleOut

        d = dict(src_dict)
        email = d.pop("email")

        is_org_admin = d.pop("is_org_admin")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = AccessReviewRoleOut.from_dict(roles_item_data)

            roles.append(roles_item)

        user_id = d.pop("user_id")

        username = d.pop("username")

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        access_review_member_out = cls(
            email=email,
            is_org_admin=is_org_admin,
            roles=roles,
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        access_review_member_out.additional_properties = d
        return access_review_member_out

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
