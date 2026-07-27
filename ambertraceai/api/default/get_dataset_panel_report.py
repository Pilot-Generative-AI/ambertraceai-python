from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.panel_report_out import PanelReportOut
from ...models.validation_error_model import ValidationErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    index_column: None | str | Unset = UNSET,
    stale_periods: int | Unset = 3,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_index_column: None | str | Unset
    if isinstance(index_column, Unset):
        json_index_column = UNSET
    else:
        json_index_column = index_column
    params["index_column"] = json_index_column

    params["stale_periods"] = stale_periods

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/datasets/{id}/panel-report".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PanelReportOut | list[ValidationErrorModel] | None:
    if response.status_code == 200:
        response_200 = PanelReportOut.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = []
        _response_422 = response.json()
        for response_422_item_data in _response_422:
            response_422_item = ValidationErrorModel.from_dict(response_422_item_data)

            response_422.append(response_422_item)

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PanelReportOut | list[ValidationErrorModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    index_column: None | str | Unset = UNSET,
    stale_periods: int | Unset = 3,
) -> Response[PanelReportOut | list[ValidationErrorModel]]:
    """Get panel sufficiency report

     Pre-training data-sufficiency report for a multi-source panel: how many rows survive an all-columns-
    non-null intersection and over what window, which column is the binding constraint (and how many
    rows dropping it alone recovers), which small GROUPS of columns go missing together, and per-column
    first/last non-null dates with a staleness flag for discontinued series. The dataset must be in
    'ingested' or 'ready' status. Recomputed per call from the stored file. The index column is auto-
    detected (date/time/timestamp/datetime/period) unless index_column names one explicitly.
    recovery_groups is a HEURISTIC (each entry says so): candidates are the co-missing sets actually
    observed as some row's exact missing set, not all subsets of columns, so the best set to drop may be
    a superset that never appears on its own.

    Args:
        id (int): Resource ID
        index_column (None | str | Unset): Column to treat as the panel index (case-insensitive).
            OMIT it to auto-detect the first of date/time/timestamp/datetime/period that is present --
            the same detection the ingest-time block uses, so this route and
            schema_info['panel_sufficiency'] agree on a panel whose index is not literally called
            'date'. When an EXPLICITLY named column is absent the report comes back with
            skipped_reason='index_column_not_found' (no silent fallback).
        stale_periods (int | Unset): A column is flagged stale when its last non-null value lags
            the panel's last index by MORE than this many cadence periods (cadence = median index
            spacing). Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PanelReportOut | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        index_column=index_column,
        stale_periods=stale_periods,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    index_column: None | str | Unset = UNSET,
    stale_periods: int | Unset = 3,
) -> PanelReportOut | list[ValidationErrorModel] | None:
    """Get panel sufficiency report

     Pre-training data-sufficiency report for a multi-source panel: how many rows survive an all-columns-
    non-null intersection and over what window, which column is the binding constraint (and how many
    rows dropping it alone recovers), which small GROUPS of columns go missing together, and per-column
    first/last non-null dates with a staleness flag for discontinued series. The dataset must be in
    'ingested' or 'ready' status. Recomputed per call from the stored file. The index column is auto-
    detected (date/time/timestamp/datetime/period) unless index_column names one explicitly.
    recovery_groups is a HEURISTIC (each entry says so): candidates are the co-missing sets actually
    observed as some row's exact missing set, not all subsets of columns, so the best set to drop may be
    a superset that never appears on its own.

    Args:
        id (int): Resource ID
        index_column (None | str | Unset): Column to treat as the panel index (case-insensitive).
            OMIT it to auto-detect the first of date/time/timestamp/datetime/period that is present --
            the same detection the ingest-time block uses, so this route and
            schema_info['panel_sufficiency'] agree on a panel whose index is not literally called
            'date'. When an EXPLICITLY named column is absent the report comes back with
            skipped_reason='index_column_not_found' (no silent fallback).
        stale_periods (int | Unset): A column is flagged stale when its last non-null value lags
            the panel's last index by MORE than this many cadence periods (cadence = median index
            spacing). Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PanelReportOut | list[ValidationErrorModel]
    """

    return sync_detailed(
        id=id,
        client=client,
        index_column=index_column,
        stale_periods=stale_periods,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    index_column: None | str | Unset = UNSET,
    stale_periods: int | Unset = 3,
) -> Response[PanelReportOut | list[ValidationErrorModel]]:
    """Get panel sufficiency report

     Pre-training data-sufficiency report for a multi-source panel: how many rows survive an all-columns-
    non-null intersection and over what window, which column is the binding constraint (and how many
    rows dropping it alone recovers), which small GROUPS of columns go missing together, and per-column
    first/last non-null dates with a staleness flag for discontinued series. The dataset must be in
    'ingested' or 'ready' status. Recomputed per call from the stored file. The index column is auto-
    detected (date/time/timestamp/datetime/period) unless index_column names one explicitly.
    recovery_groups is a HEURISTIC (each entry says so): candidates are the co-missing sets actually
    observed as some row's exact missing set, not all subsets of columns, so the best set to drop may be
    a superset that never appears on its own.

    Args:
        id (int): Resource ID
        index_column (None | str | Unset): Column to treat as the panel index (case-insensitive).
            OMIT it to auto-detect the first of date/time/timestamp/datetime/period that is present --
            the same detection the ingest-time block uses, so this route and
            schema_info['panel_sufficiency'] agree on a panel whose index is not literally called
            'date'. When an EXPLICITLY named column is absent the report comes back with
            skipped_reason='index_column_not_found' (no silent fallback).
        stale_periods (int | Unset): A column is flagged stale when its last non-null value lags
            the panel's last index by MORE than this many cadence periods (cadence = median index
            spacing). Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PanelReportOut | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        index_column=index_column,
        stale_periods=stale_periods,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    index_column: None | str | Unset = UNSET,
    stale_periods: int | Unset = 3,
) -> PanelReportOut | list[ValidationErrorModel] | None:
    """Get panel sufficiency report

     Pre-training data-sufficiency report for a multi-source panel: how many rows survive an all-columns-
    non-null intersection and over what window, which column is the binding constraint (and how many
    rows dropping it alone recovers), which small GROUPS of columns go missing together, and per-column
    first/last non-null dates with a staleness flag for discontinued series. The dataset must be in
    'ingested' or 'ready' status. Recomputed per call from the stored file. The index column is auto-
    detected (date/time/timestamp/datetime/period) unless index_column names one explicitly.
    recovery_groups is a HEURISTIC (each entry says so): candidates are the co-missing sets actually
    observed as some row's exact missing set, not all subsets of columns, so the best set to drop may be
    a superset that never appears on its own.

    Args:
        id (int): Resource ID
        index_column (None | str | Unset): Column to treat as the panel index (case-insensitive).
            OMIT it to auto-detect the first of date/time/timestamp/datetime/period that is present --
            the same detection the ingest-time block uses, so this route and
            schema_info['panel_sufficiency'] agree on a panel whose index is not literally called
            'date'. When an EXPLICITLY named column is absent the report comes back with
            skipped_reason='index_column_not_found' (no silent fallback).
        stale_periods (int | Unset): A column is flagged stale when its last non-null value lags
            the panel's last index by MORE than this many cadence periods (cadence = median index
            spacing). Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PanelReportOut | list[ValidationErrorModel]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            index_column=index_column,
            stale_periods=stale_periods,
        )
    ).parsed
