from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_query_item import BatchQueryItem


T = TypeVar("T", bound="BatchQueryRequest")


@_attrs_define
class BatchQueryRequest:
    """Batch query request — N queries in one call.

    Attributes:
        queries (list[BatchQueryItem]): List of queries to execute (1–10). Each item is independent; a failure in one
            item produces a per-item error object, never a batch-level failure.
        projection (list[str] | None | Unset): Batch-level default projection applied to every item that does not
            declare its own ``projection``. ``None`` = full response.
    """

    queries: list[BatchQueryItem]
    projection: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queries = []
        for queries_item_data in self.queries:
            queries_item = queries_item_data.to_dict()
            queries.append(queries_item)

        projection: list[str] | None | Unset
        if isinstance(self.projection, Unset):
            projection = UNSET
        elif isinstance(self.projection, list):
            projection = self.projection

        else:
            projection = self.projection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queries": queries,
            }
        )
        if projection is not UNSET:
            field_dict["projection"] = projection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_query_item import BatchQueryItem

        d = dict(src_dict)
        queries = []
        _queries = d.pop("queries")
        for queries_item_data in _queries:
            queries_item = BatchQueryItem.from_dict(queries_item_data)

            queries.append(queries_item)

        def _parse_projection(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                projection_type_0 = cast(list[str], data)

                return projection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        projection = _parse_projection(d.pop("projection", UNSET))

        batch_query_request = cls(
            queries=queries,
            projection=projection,
        )

        batch_query_request.additional_properties = d
        return batch_query_request

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
