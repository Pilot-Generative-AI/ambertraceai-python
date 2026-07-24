from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResidualDiagnosisRequest")


@_attrs_define
class ResidualDiagnosisRequest:
    """Request body for the residual-diagnosis "why" endpoint.

    Diagnoses a *significant* residual on a symbolic forecast and calls **drift
    vs correction** — attributing the miss to the driver-rules that lost
    sensitivity. Supply EITHER a stored ``forecast_id`` (the value + backfilled
    actual are read off the record) OR an explicit ``value`` + ``actual`` pair
    (for an ad-hoc what-if breach).

        Attributes:
            prediction_config_id (int): ID of a prediction config on this platform — supplies the dataset the symbolic
                forecaster is fit over and the recent cohort the rolling sensitivity is measured on.
            actual (float | None | Unset): Explicit realised target value (use with 'value' instead of forecast_id). The
                observed value the forecast was trying to hit.
            forecast_id (int | None | Unset): ID of a stored forecast record (from prediction history). Its predicted value
                and backfilled actual_value drive the residual. Mutually exclusive with value+actual; the record must have an
                actual_value backfilled.
            k (float | None | Unset): Breach gate: the residual is significant when |z| > k standard deviations of the model
                error. Default 2.0.
            value (float | None | Unset): Explicit forecast value to diagnose (use with 'actual' instead of forecast_id).
                The issued symbolic forecast's point value.
    """

    prediction_config_id: int
    actual: float | None | Unset = UNSET
    forecast_id: int | None | Unset = UNSET
    k: float | None | Unset = UNSET
    value: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prediction_config_id = self.prediction_config_id

        actual: float | None | Unset
        if isinstance(self.actual, Unset):
            actual = UNSET
        else:
            actual = self.actual

        forecast_id: int | None | Unset
        if isinstance(self.forecast_id, Unset):
            forecast_id = UNSET
        else:
            forecast_id = self.forecast_id

        k: float | None | Unset
        if isinstance(self.k, Unset):
            k = UNSET
        else:
            k = self.k

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prediction_config_id": prediction_config_id,
            }
        )
        if actual is not UNSET:
            field_dict["actual"] = actual
        if forecast_id is not UNSET:
            field_dict["forecast_id"] = forecast_id
        if k is not UNSET:
            field_dict["k"] = k
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prediction_config_id = d.pop("prediction_config_id")

        def _parse_actual(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        actual = _parse_actual(d.pop("actual", UNSET))

        def _parse_forecast_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        forecast_id = _parse_forecast_id(d.pop("forecast_id", UNSET))

        def _parse_k(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        k = _parse_k(d.pop("k", UNSET))

        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        residual_diagnosis_request = cls(
            prediction_config_id=prediction_config_id,
            actual=actual,
            forecast_id=forecast_id,
            k=k,
            value=value,
        )

        residual_diagnosis_request.additional_properties = d
        return residual_diagnosis_request

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
