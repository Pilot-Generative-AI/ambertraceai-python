from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PanelTradeoffStepOut")


@_attrs_define
class PanelTradeoffStepOut:
    """One step of the sparsity-ordered greedy column-drop curve.

    At each step the SPARSEST remaining column (most nulls) is dropped and
    the usable-row count is recomputed via a suffix-AND of the non-null masks
    (O(rows x cols) total).  Step 0 is the baseline (no columns dropped).

        Attributes:
            cumulative_dropped (int): Total number of columns dropped so far (0 at step 0).
            step (int): Step number (0 = baseline, no drops).
            usable_rows (int): Rows where every REMAINING column is non-null after this drop.
            dropped_column (None | str | Unset): Column dropped at this step (None for the baseline step 0).
            heuristic (str | Unset): Algorithm that produced this curve.  'sparsity_greedy' drops the column with the MOST
                nulls at each step. Default: 'sparsity_greedy'.
            usable_first_index (None | str | Unset):
            usable_last_index (None | str | Unset):
    """

    cumulative_dropped: int
    step: int
    usable_rows: int
    dropped_column: None | str | Unset = UNSET
    heuristic: str | Unset = "sparsity_greedy"
    usable_first_index: None | str | Unset = UNSET
    usable_last_index: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cumulative_dropped = self.cumulative_dropped

        step = self.step

        usable_rows = self.usable_rows

        dropped_column: None | str | Unset
        if isinstance(self.dropped_column, Unset):
            dropped_column = UNSET
        else:
            dropped_column = self.dropped_column

        heuristic = self.heuristic

        usable_first_index: None | str | Unset
        if isinstance(self.usable_first_index, Unset):
            usable_first_index = UNSET
        else:
            usable_first_index = self.usable_first_index

        usable_last_index: None | str | Unset
        if isinstance(self.usable_last_index, Unset):
            usable_last_index = UNSET
        else:
            usable_last_index = self.usable_last_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cumulative_dropped": cumulative_dropped,
                "step": step,
                "usable_rows": usable_rows,
            }
        )
        if dropped_column is not UNSET:
            field_dict["dropped_column"] = dropped_column
        if heuristic is not UNSET:
            field_dict["heuristic"] = heuristic
        if usable_first_index is not UNSET:
            field_dict["usable_first_index"] = usable_first_index
        if usable_last_index is not UNSET:
            field_dict["usable_last_index"] = usable_last_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cumulative_dropped = d.pop("cumulative_dropped")

        step = d.pop("step")

        usable_rows = d.pop("usable_rows")

        def _parse_dropped_column(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dropped_column = _parse_dropped_column(d.pop("dropped_column", UNSET))

        heuristic = d.pop("heuristic", UNSET)

        def _parse_usable_first_index(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usable_first_index = _parse_usable_first_index(d.pop("usable_first_index", UNSET))

        def _parse_usable_last_index(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usable_last_index = _parse_usable_last_index(d.pop("usable_last_index", UNSET))

        panel_tradeoff_step_out = cls(
            cumulative_dropped=cumulative_dropped,
            step=step,
            usable_rows=usable_rows,
            dropped_column=dropped_column,
            heuristic=heuristic,
            usable_first_index=usable_first_index,
            usable_last_index=usable_last_index,
        )

        panel_tradeoff_step_out.additional_properties = d
        return panel_tradeoff_step_out

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
