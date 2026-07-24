from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linked_dataset_out import LinkedDatasetOut
    from ..models.linked_series_out import LinkedSeriesOut


T = TypeVar("T", bound="EntityLinkOut")


@_attrs_define
class EntityLinkOut:
    """An entity with its linked series and datasets.

    Attributes:
        entity_label (str):
        node_uuid (str):
        entity_type (str | Unset):  Default: ''.
        linked_datasets (list[LinkedDatasetOut] | Unset):
        linked_series (list[LinkedSeriesOut] | Unset):
    """

    entity_label: str
    node_uuid: str
    entity_type: str | Unset = ""
    linked_datasets: list[LinkedDatasetOut] | Unset = UNSET
    linked_series: list[LinkedSeriesOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_label = self.entity_label

        node_uuid = self.node_uuid

        entity_type = self.entity_type

        linked_datasets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_datasets, Unset):
            linked_datasets = []
            for linked_datasets_item_data in self.linked_datasets:
                linked_datasets_item = linked_datasets_item_data.to_dict()
                linked_datasets.append(linked_datasets_item)

        linked_series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_series, Unset):
            linked_series = []
            for linked_series_item_data in self.linked_series:
                linked_series_item = linked_series_item_data.to_dict()
                linked_series.append(linked_series_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity_label": entity_label,
                "node_uuid": node_uuid,
            }
        )
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if linked_datasets is not UNSET:
            field_dict["linked_datasets"] = linked_datasets
        if linked_series is not UNSET:
            field_dict["linked_series"] = linked_series

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linked_dataset_out import LinkedDatasetOut
        from ..models.linked_series_out import LinkedSeriesOut

        d = dict(src_dict)
        entity_label = d.pop("entity_label")

        node_uuid = d.pop("node_uuid")

        entity_type = d.pop("entity_type", UNSET)

        _linked_datasets = d.pop("linked_datasets", UNSET)
        linked_datasets: list[LinkedDatasetOut] | Unset = UNSET
        if _linked_datasets is not UNSET:
            linked_datasets = []
            for linked_datasets_item_data in _linked_datasets:
                linked_datasets_item = LinkedDatasetOut.from_dict(linked_datasets_item_data)

                linked_datasets.append(linked_datasets_item)

        _linked_series = d.pop("linked_series", UNSET)
        linked_series: list[LinkedSeriesOut] | Unset = UNSET
        if _linked_series is not UNSET:
            linked_series = []
            for linked_series_item_data in _linked_series:
                linked_series_item = LinkedSeriesOut.from_dict(linked_series_item_data)

                linked_series.append(linked_series_item)

        entity_link_out = cls(
            entity_label=entity_label,
            node_uuid=node_uuid,
            entity_type=entity_type,
            linked_datasets=linked_datasets,
            linked_series=linked_series,
        )

        entity_link_out.additional_properties = d
        return entity_link_out

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
