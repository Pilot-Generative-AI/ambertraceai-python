from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.fact_with_confidence import FactWithConfidence


T = TypeVar("T", bound="QueryRequestFactsType0")


@_attrs_define
class QueryRequestFactsType0:
    """ """

    additional_properties: dict[str, bool | FactWithConfidence | float | int | str] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.fact_with_confidence import FactWithConfidence

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, FactWithConfidence):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fact_with_confidence import FactWithConfidence

        d = dict(src_dict)
        query_request_facts_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> bool | FactWithConfidence | float | int | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_4 = FactWithConfidence.from_dict(data)

                    return additional_property_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(bool | FactWithConfidence | float | int | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        query_request_facts_type_0.additional_properties = additional_properties
        return query_request_facts_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> bool | FactWithConfidence | float | int | str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: bool | FactWithConfidence | float | int | str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
