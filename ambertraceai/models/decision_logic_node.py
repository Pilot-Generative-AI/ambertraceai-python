from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DecisionLogicNode")


@_attrs_define
class DecisionLogicNode:
    """A node in the decision-logic DAG.

    Attributes:
        id (str): Unique node identifier (type:name).
        name (str): Human-readable rule or outcome name.
        type_ (str): Node type: 'classifier', 'verdict', or 'outcome'.
        connected (bool | None | Unset): Whether the rule's references resolve (verdicts only).
        fire_count (int | Unset): Absolute count of sample rows this rule fires on. Default: 0.
        fire_rate (float | None | Unset): Fraction of sample rows this rule fires on (0.0-1.0). Null when firing was not
            evaluated (data-less build).
        is_default (bool | Unset): Whether this is the default/fall-through outcome. Default: False.
        outcome (None | str | Unset): The decision outcome this node certifies (verdicts/outcomes).
        reachable (bool | Unset): Whether this node is reachable (connected and firing). Default: True.
    """

    id: str
    name: str
    type_: str
    connected: bool | None | Unset = UNSET
    fire_count: int | Unset = 0
    fire_rate: float | None | Unset = UNSET
    is_default: bool | Unset = False
    outcome: None | str | Unset = UNSET
    reachable: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        connected: bool | None | Unset
        if isinstance(self.connected, Unset):
            connected = UNSET
        else:
            connected = self.connected

        fire_count = self.fire_count

        fire_rate: float | None | Unset
        if isinstance(self.fire_rate, Unset):
            fire_rate = UNSET
        else:
            fire_rate = self.fire_rate

        is_default = self.is_default

        outcome: None | str | Unset
        if isinstance(self.outcome, Unset):
            outcome = UNSET
        else:
            outcome = self.outcome

        reachable = self.reachable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
            }
        )
        if connected is not UNSET:
            field_dict["connected"] = connected
        if fire_count is not UNSET:
            field_dict["fire_count"] = fire_count
        if fire_rate is not UNSET:
            field_dict["fire_rate"] = fire_rate
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if reachable is not UNSET:
            field_dict["reachable"] = reachable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        def _parse_connected(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        connected = _parse_connected(d.pop("connected", UNSET))

        fire_count = d.pop("fire_count", UNSET)

        def _parse_fire_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fire_rate = _parse_fire_rate(d.pop("fire_rate", UNSET))

        is_default = d.pop("is_default", UNSET)

        def _parse_outcome(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outcome = _parse_outcome(d.pop("outcome", UNSET))

        reachable = d.pop("reachable", UNSET)

        decision_logic_node = cls(
            id=id,
            name=name,
            type_=type_,
            connected=connected,
            fire_count=fire_count,
            fire_rate=fire_rate,
            is_default=is_default,
            outcome=outcome,
            reachable=reachable,
        )

        decision_logic_node.additional_properties = d
        return decision_logic_node

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
