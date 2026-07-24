from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnreachableOutcome")


@_attrs_define
class UnreachableOutcome:
    """A declared decision outcome that no firing chain reaches.

    Attributes:
        detail (str): Human-readable explanation of the unreachability reason.
        outcome (str): The unreachable outcome label.
        reason (str): Why the outcome is unreachable: 'no_verdict', 'all_verdicts_dangling', or 'all_verdicts_dead'.
        verdict_names (list[str] | Unset): Names of the verdict rules associated with this outcome (if any).
    """

    detail: str
    outcome: str
    reason: str
    verdict_names: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        outcome = self.outcome

        reason = self.reason

        verdict_names: list[str] | Unset = UNSET
        if not isinstance(self.verdict_names, Unset):
            verdict_names = self.verdict_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
                "outcome": outcome,
                "reason": reason,
            }
        )
        if verdict_names is not UNSET:
            field_dict["verdict_names"] = verdict_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detail = d.pop("detail")

        outcome = d.pop("outcome")

        reason = d.pop("reason")

        verdict_names = cast(list[str], d.pop("verdict_names", UNSET))

        unreachable_outcome = cls(
            detail=detail,
            outcome=outcome,
            reason=reason,
            verdict_names=verdict_names,
        )

        unreachable_outcome.additional_properties = d
        return unreachable_outcome

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
