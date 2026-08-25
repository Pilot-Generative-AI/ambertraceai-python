from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharingAuditEntryOut")


@_attrs_define
class SharingAuditEntryOut:
    """One append-only sharing/team audit event.

    Attributes:
        event_type (str):
        id (int):
        organisation_id (str):
        actor_user_id (int | None | Unset):
        created_at (None | str | Unset):
        detail (None | str | Unset):
        subject_team_id (int | None | Unset):
        subject_user_id (int | None | Unset):
        target_id (int | None | Unset):
        target_name (None | str | Unset):
        target_type (None | str | Unset):
        visibility_from (None | str | Unset):
        visibility_to (None | str | Unset):
    """

    event_type: str
    id: int
    organisation_id: str
    actor_user_id: int | None | Unset = UNSET
    created_at: None | str | Unset = UNSET
    detail: None | str | Unset = UNSET
    subject_team_id: int | None | Unset = UNSET
    subject_user_id: int | None | Unset = UNSET
    target_id: int | None | Unset = UNSET
    target_name: None | str | Unset = UNSET
    target_type: None | str | Unset = UNSET
    visibility_from: None | str | Unset = UNSET
    visibility_to: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type

        id = self.id

        organisation_id = self.organisation_id

        actor_user_id: int | None | Unset
        if isinstance(self.actor_user_id, Unset):
            actor_user_id = UNSET
        else:
            actor_user_id = self.actor_user_id

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        subject_team_id: int | None | Unset
        if isinstance(self.subject_team_id, Unset):
            subject_team_id = UNSET
        else:
            subject_team_id = self.subject_team_id

        subject_user_id: int | None | Unset
        if isinstance(self.subject_user_id, Unset):
            subject_user_id = UNSET
        else:
            subject_user_id = self.subject_user_id

        target_id: int | None | Unset
        if isinstance(self.target_id, Unset):
            target_id = UNSET
        else:
            target_id = self.target_id

        target_name: None | str | Unset
        if isinstance(self.target_name, Unset):
            target_name = UNSET
        else:
            target_name = self.target_name

        target_type: None | str | Unset
        if isinstance(self.target_type, Unset):
            target_type = UNSET
        else:
            target_type = self.target_type

        visibility_from: None | str | Unset
        if isinstance(self.visibility_from, Unset):
            visibility_from = UNSET
        else:
            visibility_from = self.visibility_from

        visibility_to: None | str | Unset
        if isinstance(self.visibility_to, Unset):
            visibility_to = UNSET
        else:
            visibility_to = self.visibility_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "id": id,
                "organisation_id": organisation_id,
            }
        )
        if actor_user_id is not UNSET:
            field_dict["actor_user_id"] = actor_user_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if detail is not UNSET:
            field_dict["detail"] = detail
        if subject_team_id is not UNSET:
            field_dict["subject_team_id"] = subject_team_id
        if subject_user_id is not UNSET:
            field_dict["subject_user_id"] = subject_user_id
        if target_id is not UNSET:
            field_dict["target_id"] = target_id
        if target_name is not UNSET:
            field_dict["target_name"] = target_name
        if target_type is not UNSET:
            field_dict["target_type"] = target_type
        if visibility_from is not UNSET:
            field_dict["visibility_from"] = visibility_from
        if visibility_to is not UNSET:
            field_dict["visibility_to"] = visibility_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = d.pop("event_type")

        id = d.pop("id")

        organisation_id = d.pop("organisation_id")

        def _parse_actor_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        actor_user_id = _parse_actor_user_id(d.pop("actor_user_id", UNSET))

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        def _parse_subject_team_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        subject_team_id = _parse_subject_team_id(d.pop("subject_team_id", UNSET))

        def _parse_subject_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        subject_user_id = _parse_subject_user_id(d.pop("subject_user_id", UNSET))

        def _parse_target_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        target_id = _parse_target_id(d.pop("target_id", UNSET))

        def _parse_target_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_name = _parse_target_name(d.pop("target_name", UNSET))

        def _parse_target_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_type = _parse_target_type(d.pop("target_type", UNSET))

        def _parse_visibility_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visibility_from = _parse_visibility_from(d.pop("visibility_from", UNSET))

        def _parse_visibility_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visibility_to = _parse_visibility_to(d.pop("visibility_to", UNSET))

        sharing_audit_entry_out = cls(
            event_type=event_type,
            id=id,
            organisation_id=organisation_id,
            actor_user_id=actor_user_id,
            created_at=created_at,
            detail=detail,
            subject_team_id=subject_team_id,
            subject_user_id=subject_user_id,
            target_id=target_id,
            target_name=target_name,
            target_type=target_type,
            visibility_from=visibility_from,
            visibility_to=visibility_to,
        )

        sharing_audit_entry_out.additional_properties = d
        return sharing_audit_entry_out

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
