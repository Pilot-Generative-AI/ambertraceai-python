from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decision_logic_edge import DecisionLogicEdge
    from ..models.decision_logic_node import DecisionLogicNode
    from ..models.decision_logic_summary import DecisionLogicSummary
    from ..models.unreachable_outcome import UnreachableOutcome


T = TypeVar("T", bound="DecisionLogicMapOut")


@_attrs_define
class DecisionLogicMapOut:
    """The decision-logic map: a DAG of classifiers, verdicts, and outcomes
    with live fire-rates and reachability status.

        Attributes:
            firing_evaluated (bool): Whether firing was evaluated (False on data-less builds).
            n_rows (int): Number of sample rows used for fire-rate evaluation.
            summary (DecisionLogicSummary): Summary counts for the decision-logic map.
            edges (list[DecisionLogicEdge] | Unset):
            nodes (list[DecisionLogicNode] | Unset):
            unreachable_outcomes (list[UnreachableOutcome] | Unset):
    """

    firing_evaluated: bool
    n_rows: int
    summary: DecisionLogicSummary
    edges: list[DecisionLogicEdge] | Unset = UNSET
    nodes: list[DecisionLogicNode] | Unset = UNSET
    unreachable_outcomes: list[UnreachableOutcome] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        firing_evaluated = self.firing_evaluated

        n_rows = self.n_rows

        summary = self.summary.to_dict()

        edges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edges, Unset):
            edges = []
            for edges_item_data in self.edges:
                edges_item = edges_item_data.to_dict()
                edges.append(edges_item)

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        unreachable_outcomes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unreachable_outcomes, Unset):
            unreachable_outcomes = []
            for unreachable_outcomes_item_data in self.unreachable_outcomes:
                unreachable_outcomes_item = unreachable_outcomes_item_data.to_dict()
                unreachable_outcomes.append(unreachable_outcomes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firing_evaluated": firing_evaluated,
                "n_rows": n_rows,
                "summary": summary,
            }
        )
        if edges is not UNSET:
            field_dict["edges"] = edges
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if unreachable_outcomes is not UNSET:
            field_dict["unreachable_outcomes"] = unreachable_outcomes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.decision_logic_edge import DecisionLogicEdge
        from ..models.decision_logic_node import DecisionLogicNode
        from ..models.decision_logic_summary import DecisionLogicSummary
        from ..models.unreachable_outcome import UnreachableOutcome

        d = dict(src_dict)
        firing_evaluated = d.pop("firing_evaluated")

        n_rows = d.pop("n_rows")

        summary = DecisionLogicSummary.from_dict(d.pop("summary"))

        _edges = d.pop("edges", UNSET)
        edges: list[DecisionLogicEdge] | Unset = UNSET
        if _edges is not UNSET:
            edges = []
            for edges_item_data in _edges:
                edges_item = DecisionLogicEdge.from_dict(edges_item_data)

                edges.append(edges_item)

        _nodes = d.pop("nodes", UNSET)
        nodes: list[DecisionLogicNode] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = DecisionLogicNode.from_dict(nodes_item_data)

                nodes.append(nodes_item)

        _unreachable_outcomes = d.pop("unreachable_outcomes", UNSET)
        unreachable_outcomes: list[UnreachableOutcome] | Unset = UNSET
        if _unreachable_outcomes is not UNSET:
            unreachable_outcomes = []
            for unreachable_outcomes_item_data in _unreachable_outcomes:
                unreachable_outcomes_item = UnreachableOutcome.from_dict(unreachable_outcomes_item_data)

                unreachable_outcomes.append(unreachable_outcomes_item)

        decision_logic_map_out = cls(
            firing_evaluated=firing_evaluated,
            n_rows=n_rows,
            summary=summary,
            edges=edges,
            nodes=nodes,
            unreachable_outcomes=unreachable_outcomes,
        )

        decision_logic_map_out.additional_properties = d
        return decision_logic_map_out

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
