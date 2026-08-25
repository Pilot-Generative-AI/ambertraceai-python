from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.batch_query_item_result import BatchQueryItemResult


T = TypeVar("T", bound="BatchQueryResponse")


@_attrs_define
class BatchQueryResponse:
    """Batch query response — per-item results in request order.

    Attributes:
        platform_id (int):
        results (list[BatchQueryItemResult]): Per-item results, one per request query, in the same order.
    """

    platform_id: int
    results: list[BatchQueryItemResult]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_id = self.platform_id

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform_id": platform_id,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_query_item_result import BatchQueryItemResult

        d = dict(src_dict)
        platform_id = d.pop("platform_id")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = BatchQueryItemResult.from_dict(results_item_data)

            results.append(results_item)

        batch_query_response = cls(
            platform_id=platform_id,
            results=results,
        )

        batch_query_response.additional_properties = d
        return batch_query_response

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
