from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fetch_source import FetchSource
    from ..models.on_missing_policy import OnMissingPolicy
    from ..models.on_stale_policy import OnStalePolicy


T = TypeVar("T", bound="DatasetFetchMultiRequest")


@_attrs_define
class DatasetFetchMultiRequest:
    """
    Attributes:
        domain_id (int):
        sources (list[FetchSource]): Two or more connector sources to fetch and merge into one dataset. Each value
            column is namespaced by connector_type (e.g. boe__IUDSOIA).
        aggregation (str | Unset): Resample aggregation when frequency is set: 'last' or 'mean'. Default: 'last'.
        frequency (None | str | Unset): Optional common grid to resample every source onto before joining: daily,
            weekly, monthly, quarterly, or annual. Without it, mixed-frequency sources outer-join to a mostly-null table.
        join_on (str | Unset): Index column to outer-join the sources on (default 'date'). Default: 'date'.
        on_missing (None | OnMissingPolicy | Unset): Missing-value policy applied after the outer join (Part of #1482).
            Omit for backward-compatible forward-fill. The transformation manifest on the resulting dataset records every
            fill/drop/interpolation with column, method, rows_affected, and modeled_extrapolation flag.
        on_stale (None | OnStalePolicy | Unset): Staleness policy applied after the panel sufficiency computation
            (#1382). Omit for backward-compatible warn-only (stale columns are recorded in the panel report but do not
            block). 'error' fails the dataset; 'drop_columns' removes stale columns from the merged frame. stale_periods
            overrides the default threshold (3 cadence periods).
    """

    domain_id: int
    sources: list[FetchSource]
    aggregation: str | Unset = "last"
    frequency: None | str | Unset = UNSET
    join_on: str | Unset = "date"
    on_missing: None | OnMissingPolicy | Unset = UNSET
    on_stale: None | OnStalePolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.on_missing_policy import OnMissingPolicy
        from ..models.on_stale_policy import OnStalePolicy

        domain_id = self.domain_id

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        aggregation = self.aggregation

        frequency: None | str | Unset
        if isinstance(self.frequency, Unset):
            frequency = UNSET
        else:
            frequency = self.frequency

        join_on = self.join_on

        on_missing: dict[str, Any] | None | Unset
        if isinstance(self.on_missing, Unset):
            on_missing = UNSET
        elif isinstance(self.on_missing, OnMissingPolicy):
            on_missing = self.on_missing.to_dict()
        else:
            on_missing = self.on_missing

        on_stale: dict[str, Any] | None | Unset
        if isinstance(self.on_stale, Unset):
            on_stale = UNSET
        elif isinstance(self.on_stale, OnStalePolicy):
            on_stale = self.on_stale.to_dict()
        else:
            on_stale = self.on_stale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_id": domain_id,
                "sources": sources,
            }
        )
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if join_on is not UNSET:
            field_dict["join_on"] = join_on
        if on_missing is not UNSET:
            field_dict["on_missing"] = on_missing
        if on_stale is not UNSET:
            field_dict["on_stale"] = on_stale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fetch_source import FetchSource
        from ..models.on_missing_policy import OnMissingPolicy
        from ..models.on_stale_policy import OnStalePolicy

        d = dict(src_dict)
        domain_id = d.pop("domain_id")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = FetchSource.from_dict(sources_item_data)

            sources.append(sources_item)

        aggregation = d.pop("aggregation", UNSET)

        def _parse_frequency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        frequency = _parse_frequency(d.pop("frequency", UNSET))

        join_on = d.pop("join_on", UNSET)

        def _parse_on_missing(data: object) -> None | OnMissingPolicy | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                on_missing_type_0 = OnMissingPolicy.from_dict(data)

                return on_missing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OnMissingPolicy | Unset, data)

        on_missing = _parse_on_missing(d.pop("on_missing", UNSET))

        def _parse_on_stale(data: object) -> None | OnStalePolicy | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                on_stale_type_0 = OnStalePolicy.from_dict(data)

                return on_stale_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OnStalePolicy | Unset, data)

        on_stale = _parse_on_stale(d.pop("on_stale", UNSET))

        dataset_fetch_multi_request = cls(
            domain_id=domain_id,
            sources=sources,
            aggregation=aggregation,
            frequency=frequency,
            join_on=join_on,
            on_missing=on_missing,
            on_stale=on_stale,
        )

        dataset_fetch_multi_request.additional_properties = d
        return dataset_fetch_multi_request

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
