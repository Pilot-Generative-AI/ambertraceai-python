from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.panel_binding_constraint_out import PanelBindingConstraintOut
    from ..models.panel_column_out import PanelColumnOut
    from ..models.panel_intersection_out import PanelIntersectionOut
    from ..models.panel_recovery_group_out import PanelRecoveryGroupOut
    from ..models.panel_tradeoff_step_out import PanelTradeoffStepOut


T = TypeVar("T", bound="PanelReportOut")


@_attrs_define
class PanelReportOut:
    """
    Attributes:
        intersection (PanelIntersectionOut):
        binding_constraint (None | PanelBindingConstraintOut | Unset):
        cadence_days (float | None | Unset):
        caveats (list[str] | Unset):
        column_count (int | Unset):  Default: 0.
        columns (list[PanelColumnOut] | Unset):
        index_column (None | str | Unset):
        panel_first_index (None | str | Unset):
        panel_last_index (None | str | Unset):
        recovery_groups (list[PanelRecoveryGroupOut] | Unset):
        row_count (int | Unset):  Default: 0.
        skipped_reason (None | str | Unset): Populated when the report could not be computed (unparseable file, no index
            column, unsupported format). Always present in the body -- an ABSENT report block would read as a clean panel.
        stale_columns (list[str] | Unset):
        tradeoff_curve (list[PanelTradeoffStepOut] | Unset): Sparsity-ordered greedy column-drop curve.  At each step
            the SPARSEST remaining column is dropped and usable_rows is recomputed. Step 0 is the baseline (no drops).  Use
            this to see how many rows you recover by cutting the N sparsest columns.
    """

    intersection: PanelIntersectionOut
    binding_constraint: None | PanelBindingConstraintOut | Unset = UNSET
    cadence_days: float | None | Unset = UNSET
    caveats: list[str] | Unset = UNSET
    column_count: int | Unset = 0
    columns: list[PanelColumnOut] | Unset = UNSET
    index_column: None | str | Unset = UNSET
    panel_first_index: None | str | Unset = UNSET
    panel_last_index: None | str | Unset = UNSET
    recovery_groups: list[PanelRecoveryGroupOut] | Unset = UNSET
    row_count: int | Unset = 0
    skipped_reason: None | str | Unset = UNSET
    stale_columns: list[str] | Unset = UNSET
    tradeoff_curve: list[PanelTradeoffStepOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.panel_binding_constraint_out import PanelBindingConstraintOut

        intersection = self.intersection.to_dict()

        binding_constraint: dict[str, Any] | None | Unset
        if isinstance(self.binding_constraint, Unset):
            binding_constraint = UNSET
        elif isinstance(self.binding_constraint, PanelBindingConstraintOut):
            binding_constraint = self.binding_constraint.to_dict()
        else:
            binding_constraint = self.binding_constraint

        cadence_days: float | None | Unset
        if isinstance(self.cadence_days, Unset):
            cadence_days = UNSET
        else:
            cadence_days = self.cadence_days

        caveats: list[str] | Unset = UNSET
        if not isinstance(self.caveats, Unset):
            caveats = self.caveats

        column_count = self.column_count

        columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)

        index_column: None | str | Unset
        if isinstance(self.index_column, Unset):
            index_column = UNSET
        else:
            index_column = self.index_column

        panel_first_index: None | str | Unset
        if isinstance(self.panel_first_index, Unset):
            panel_first_index = UNSET
        else:
            panel_first_index = self.panel_first_index

        panel_last_index: None | str | Unset
        if isinstance(self.panel_last_index, Unset):
            panel_last_index = UNSET
        else:
            panel_last_index = self.panel_last_index

        recovery_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recovery_groups, Unset):
            recovery_groups = []
            for recovery_groups_item_data in self.recovery_groups:
                recovery_groups_item = recovery_groups_item_data.to_dict()
                recovery_groups.append(recovery_groups_item)

        row_count = self.row_count

        skipped_reason: None | str | Unset
        if isinstance(self.skipped_reason, Unset):
            skipped_reason = UNSET
        else:
            skipped_reason = self.skipped_reason

        stale_columns: list[str] | Unset = UNSET
        if not isinstance(self.stale_columns, Unset):
            stale_columns = self.stale_columns

        tradeoff_curve: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tradeoff_curve, Unset):
            tradeoff_curve = []
            for tradeoff_curve_item_data in self.tradeoff_curve:
                tradeoff_curve_item = tradeoff_curve_item_data.to_dict()
                tradeoff_curve.append(tradeoff_curve_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "intersection": intersection,
            }
        )
        if binding_constraint is not UNSET:
            field_dict["binding_constraint"] = binding_constraint
        if cadence_days is not UNSET:
            field_dict["cadence_days"] = cadence_days
        if caveats is not UNSET:
            field_dict["caveats"] = caveats
        if column_count is not UNSET:
            field_dict["column_count"] = column_count
        if columns is not UNSET:
            field_dict["columns"] = columns
        if index_column is not UNSET:
            field_dict["index_column"] = index_column
        if panel_first_index is not UNSET:
            field_dict["panel_first_index"] = panel_first_index
        if panel_last_index is not UNSET:
            field_dict["panel_last_index"] = panel_last_index
        if recovery_groups is not UNSET:
            field_dict["recovery_groups"] = recovery_groups
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if skipped_reason is not UNSET:
            field_dict["skipped_reason"] = skipped_reason
        if stale_columns is not UNSET:
            field_dict["stale_columns"] = stale_columns
        if tradeoff_curve is not UNSET:
            field_dict["tradeoff_curve"] = tradeoff_curve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.panel_binding_constraint_out import PanelBindingConstraintOut
        from ..models.panel_column_out import PanelColumnOut
        from ..models.panel_intersection_out import PanelIntersectionOut
        from ..models.panel_recovery_group_out import PanelRecoveryGroupOut
        from ..models.panel_tradeoff_step_out import PanelTradeoffStepOut

        d = dict(src_dict)
        intersection = PanelIntersectionOut.from_dict(d.pop("intersection"))

        def _parse_binding_constraint(data: object) -> None | PanelBindingConstraintOut | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                binding_constraint_type_0 = PanelBindingConstraintOut.from_dict(data)

                return binding_constraint_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PanelBindingConstraintOut | Unset, data)

        binding_constraint = _parse_binding_constraint(d.pop("binding_constraint", UNSET))

        def _parse_cadence_days(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cadence_days = _parse_cadence_days(d.pop("cadence_days", UNSET))

        caveats = cast(list[str], d.pop("caveats", UNSET))

        column_count = d.pop("column_count", UNSET)

        _columns = d.pop("columns", UNSET)
        columns: list[PanelColumnOut] | Unset = UNSET
        if _columns is not UNSET:
            columns = []
            for columns_item_data in _columns:
                columns_item = PanelColumnOut.from_dict(columns_item_data)

                columns.append(columns_item)

        def _parse_index_column(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        index_column = _parse_index_column(d.pop("index_column", UNSET))

        def _parse_panel_first_index(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        panel_first_index = _parse_panel_first_index(d.pop("panel_first_index", UNSET))

        def _parse_panel_last_index(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        panel_last_index = _parse_panel_last_index(d.pop("panel_last_index", UNSET))

        _recovery_groups = d.pop("recovery_groups", UNSET)
        recovery_groups: list[PanelRecoveryGroupOut] | Unset = UNSET
        if _recovery_groups is not UNSET:
            recovery_groups = []
            for recovery_groups_item_data in _recovery_groups:
                recovery_groups_item = PanelRecoveryGroupOut.from_dict(recovery_groups_item_data)

                recovery_groups.append(recovery_groups_item)

        row_count = d.pop("row_count", UNSET)

        def _parse_skipped_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        skipped_reason = _parse_skipped_reason(d.pop("skipped_reason", UNSET))

        stale_columns = cast(list[str], d.pop("stale_columns", UNSET))

        _tradeoff_curve = d.pop("tradeoff_curve", UNSET)
        tradeoff_curve: list[PanelTradeoffStepOut] | Unset = UNSET
        if _tradeoff_curve is not UNSET:
            tradeoff_curve = []
            for tradeoff_curve_item_data in _tradeoff_curve:
                tradeoff_curve_item = PanelTradeoffStepOut.from_dict(tradeoff_curve_item_data)

                tradeoff_curve.append(tradeoff_curve_item)

        panel_report_out = cls(
            intersection=intersection,
            binding_constraint=binding_constraint,
            cadence_days=cadence_days,
            caveats=caveats,
            column_count=column_count,
            columns=columns,
            index_column=index_column,
            panel_first_index=panel_first_index,
            panel_last_index=panel_last_index,
            recovery_groups=recovery_groups,
            row_count=row_count,
            skipped_reason=skipped_reason,
            stale_columns=stale_columns,
            tradeoff_curve=tradeoff_curve,
        )

        panel_report_out.additional_properties = d
        return panel_report_out

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
