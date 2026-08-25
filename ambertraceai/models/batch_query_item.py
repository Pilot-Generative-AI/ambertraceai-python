from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_query_item_facts_type_0 import BatchQueryItemFactsType0
    from ..models.batch_query_item_predictions_type_0 import BatchQueryItemPredictionsType0
    from ..models.batch_query_item_relations_type_0 import BatchQueryItemRelationsType0


T = TypeVar("T", bound="BatchQueryItem")


@_attrs_define
class BatchQueryItem:
    """A single query within a batch request.

    Attributes:
        query (str):
        explain (bool | Unset):  Default: True.
        facts (BatchQueryItemFactsType0 | None | Unset): Structured request facts (same schema as the single-query
            endpoint).
        predictions (BatchQueryItemPredictionsType0 | None | Unset): Verified-prediction references (same schema as the
            single-query endpoint).
        projection (list[str] | None | Unset): Per-item projection — same semantics as the single-query ``projection``
            parameter. When ``None`` the item inherits the batch-level ``projection`` (if any); when explicitly set it
            overrides the batch-level default for this item only.
        relations (BatchQueryItemRelationsType0 | None | Unset): Attached related facts (same schema as the single-query
            endpoint).
        top_k (int | Unset):  Default: 10.
    """

    query: str
    explain: bool | Unset = True
    facts: BatchQueryItemFactsType0 | None | Unset = UNSET
    predictions: BatchQueryItemPredictionsType0 | None | Unset = UNSET
    projection: list[str] | None | Unset = UNSET
    relations: BatchQueryItemRelationsType0 | None | Unset = UNSET
    top_k: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_query_item_facts_type_0 import BatchQueryItemFactsType0
        from ..models.batch_query_item_predictions_type_0 import BatchQueryItemPredictionsType0
        from ..models.batch_query_item_relations_type_0 import BatchQueryItemRelationsType0

        query = self.query

        explain = self.explain

        facts: dict[str, Any] | None | Unset
        if isinstance(self.facts, Unset):
            facts = UNSET
        elif isinstance(self.facts, BatchQueryItemFactsType0):
            facts = self.facts.to_dict()
        else:
            facts = self.facts

        predictions: dict[str, Any] | None | Unset
        if isinstance(self.predictions, Unset):
            predictions = UNSET
        elif isinstance(self.predictions, BatchQueryItemPredictionsType0):
            predictions = self.predictions.to_dict()
        else:
            predictions = self.predictions

        projection: list[str] | None | Unset
        if isinstance(self.projection, Unset):
            projection = UNSET
        elif isinstance(self.projection, list):
            projection = self.projection

        else:
            projection = self.projection

        relations: dict[str, Any] | None | Unset
        if isinstance(self.relations, Unset):
            relations = UNSET
        elif isinstance(self.relations, BatchQueryItemRelationsType0):
            relations = self.relations.to_dict()
        else:
            relations = self.relations

        top_k = self.top_k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if explain is not UNSET:
            field_dict["explain"] = explain
        if facts is not UNSET:
            field_dict["facts"] = facts
        if predictions is not UNSET:
            field_dict["predictions"] = predictions
        if projection is not UNSET:
            field_dict["projection"] = projection
        if relations is not UNSET:
            field_dict["relations"] = relations
        if top_k is not UNSET:
            field_dict["top_k"] = top_k

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_query_item_facts_type_0 import BatchQueryItemFactsType0
        from ..models.batch_query_item_predictions_type_0 import BatchQueryItemPredictionsType0
        from ..models.batch_query_item_relations_type_0 import BatchQueryItemRelationsType0

        d = dict(src_dict)
        query = d.pop("query")

        explain = d.pop("explain", UNSET)

        def _parse_facts(data: object) -> BatchQueryItemFactsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                facts_type_0 = BatchQueryItemFactsType0.from_dict(data)

                return facts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchQueryItemFactsType0 | None | Unset, data)

        facts = _parse_facts(d.pop("facts", UNSET))

        def _parse_predictions(data: object) -> BatchQueryItemPredictionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                predictions_type_0 = BatchQueryItemPredictionsType0.from_dict(data)

                return predictions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchQueryItemPredictionsType0 | None | Unset, data)

        predictions = _parse_predictions(d.pop("predictions", UNSET))

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

        def _parse_relations(data: object) -> BatchQueryItemRelationsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                relations_type_0 = BatchQueryItemRelationsType0.from_dict(data)

                return relations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchQueryItemRelationsType0 | None | Unset, data)

        relations = _parse_relations(d.pop("relations", UNSET))

        top_k = d.pop("top_k", UNSET)

        batch_query_item = cls(
            query=query,
            explain=explain,
            facts=facts,
            predictions=predictions,
            projection=projection,
            relations=relations,
            top_k=top_k,
        )

        batch_query_item.additional_properties = d
        return batch_query_item

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
