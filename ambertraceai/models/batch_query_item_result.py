from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_query_item_result_data_type_0 import BatchQueryItemResultDataType0
    from ..models.batch_query_item_result_error_type_0 import BatchQueryItemResultErrorType0


T = TypeVar("T", bound="BatchQueryItemResult")


@_attrs_define
class BatchQueryItemResult:
    """Result for a single item in a batch query response.

    Attributes:
        index (int): Zero-based index of this item in the request ``queries`` list.
        status (str): ``ok`` on success, ``error`` on per-item failure.
        data (BatchQueryItemResultDataType0 | None | Unset): The query result (same shape as a single-query ``data``),
            present when ``status=ok``.
        error (BatchQueryItemResultErrorType0 | None | Unset): Per-item error object (present when ``status=error``).
            Shape mirrors the single-query error envelope: ``{code, message}`` plus optional ``details``,
            ``rejected_facts``, ``query_diagnostics`` for verified fail-closed errors.
    """

    index: int
    status: str
    data: BatchQueryItemResultDataType0 | None | Unset = UNSET
    error: BatchQueryItemResultErrorType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_query_item_result_data_type_0 import BatchQueryItemResultDataType0
        from ..models.batch_query_item_result_error_type_0 import BatchQueryItemResultErrorType0

        index = self.index

        status = self.status

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, BatchQueryItemResultDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, BatchQueryItemResultErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "status": status,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_query_item_result_data_type_0 import BatchQueryItemResultDataType0
        from ..models.batch_query_item_result_error_type_0 import BatchQueryItemResultErrorType0

        d = dict(src_dict)
        index = d.pop("index")

        status = d.pop("status")

        def _parse_data(data: object) -> BatchQueryItemResultDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = BatchQueryItemResultDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchQueryItemResultDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_error(data: object) -> BatchQueryItemResultErrorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = BatchQueryItemResultErrorType0.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchQueryItemResultErrorType0 | None | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        batch_query_item_result = cls(
            index=index,
            status=status,
            data=data,
            error=error,
        )

        batch_query_item_result.additional_properties = d
        return batch_query_item_result

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
