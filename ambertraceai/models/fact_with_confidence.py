from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FactWithConfidence")


@_attrs_define
class FactWithConfidence:
    """A fact value with an explicit per-observation confidence.

    Use this form when supplying observations whose certainty varies — e.g.
    sensor readings, model outputs, or human assessments.  The ``confidence``
    is gated independently per fact by the platform's verified τ threshold
    (``verified_min_confidence``).  If ANY supplied fact has
    ``confidence < τ``, the whole decision is refused (fail-closed).

    The carried confidence value is ALSO surfaced into the certified EDB as a
    companion ground atom ``_aria_confidence__{field}`` (float [0, 1]) so that
    authored rules can reason over observation certainty directly.

    Requires a verified platform with ``require_confidence=True`` in
    ``neural_config``; sending a ``FactWithConfidence`` carrier to a
    non-verified platform (or one without ``require_confidence``) returns a
    clear rejection.

        Attributes:
            confidence (float): The caller's stated confidence in this observation, in [0, 1]. Gated by the platform's
                ``verified_min_confidence`` (τ): a fact with ``confidence < τ`` is REFUSED and surfaced in ``rejected_facts``.
            value (bool | float | int | str): The observation value (same types as a bare scalar fact).
    """

    confidence: float
    value: bool | float | int | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence

        value: bool | float | int | str
        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidence": confidence,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confidence = d.pop("confidence")

        def _parse_value(data: object) -> bool | float | int | str:
            return cast(bool | float | int | str, data)

        value = _parse_value(d.pop("value"))

        fact_with_confidence = cls(
            confidence=confidence,
            value=value,
        )

        fact_with_confidence.additional_properties = d
        return fact_with_confidence

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
