from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sharing_audit_list_out import SharingAuditListOut
from ...models.validation_error_model import ValidationErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    event_type: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_event_type: None | str | Unset
    if isinstance(event_type, Unset):
        json_event_type = UNSET
    else:
        json_event_type = event_type
    params["event_type"] = json_event_type

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/audit",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SharingAuditListOut | list[ValidationErrorModel] | None:
    if response.status_code == 200:
        response_200 = SharingAuditListOut.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

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
) -> Response[Any | SharingAuditListOut | list[ValidationErrorModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    event_type: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
) -> Response[Any | SharingAuditListOut | list[ValidationErrorModel]]:
    """List sharing/team/role audit events (SIEM export)

     Returns the append-only sharing/team/role audit trail for the caller's organisation — team
    membership changes, domain/platform visibility shares and revocations, and RBAC role lifecycle
    events — newest first, paginated. Org-admin only (403 otherwise). Org-scoped: only the caller's own
    organisation's events are ever returned.

    Filterable by ``event_type`` (e.g. ``domain_shared``, ``team_member_added``, ``role_assigned``) and
    date range (``start_date`` / ``end_date``, ISO-8601). A date-only ``end_date`` is inclusive of the
    whole day.

    Known event types: ``team_member_added``, ``team_member_removed``, ``domain_shared``,
    ``platform_shared``, ``share_revoked``, ``role_created``, ``role_updated``, ``role_deleted``,
    ``role_assigned``, ``role_revoked``, ``org_admin_granted``, ``org_admin_revoked``.

    Note: SSO/login authentication events are not currently written to this trail. Coverage is limited
    to team/sharing/role events.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        event_type (None | str | Unset): Filter to a single event type (e.g. 'domain_shared').
        start_date (None | str | Unset): Only events at or after this ISO date/datetime.
        end_date (None | str | Unset): Only events at or before this ISO date/datetime (date =
            inclusive of the day).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SharingAuditListOut | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        event_type=event_type,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    event_type: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
) -> Any | SharingAuditListOut | list[ValidationErrorModel] | None:
    """List sharing/team/role audit events (SIEM export)

     Returns the append-only sharing/team/role audit trail for the caller's organisation — team
    membership changes, domain/platform visibility shares and revocations, and RBAC role lifecycle
    events — newest first, paginated. Org-admin only (403 otherwise). Org-scoped: only the caller's own
    organisation's events are ever returned.

    Filterable by ``event_type`` (e.g. ``domain_shared``, ``team_member_added``, ``role_assigned``) and
    date range (``start_date`` / ``end_date``, ISO-8601). A date-only ``end_date`` is inclusive of the
    whole day.

    Known event types: ``team_member_added``, ``team_member_removed``, ``domain_shared``,
    ``platform_shared``, ``share_revoked``, ``role_created``, ``role_updated``, ``role_deleted``,
    ``role_assigned``, ``role_revoked``, ``org_admin_granted``, ``org_admin_revoked``.

    Note: SSO/login authentication events are not currently written to this trail. Coverage is limited
    to team/sharing/role events.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        event_type (None | str | Unset): Filter to a single event type (e.g. 'domain_shared').
        start_date (None | str | Unset): Only events at or after this ISO date/datetime.
        end_date (None | str | Unset): Only events at or before this ISO date/datetime (date =
            inclusive of the day).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SharingAuditListOut | list[ValidationErrorModel]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        event_type=event_type,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    event_type: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
) -> Response[Any | SharingAuditListOut | list[ValidationErrorModel]]:
    """List sharing/team/role audit events (SIEM export)

     Returns the append-only sharing/team/role audit trail for the caller's organisation — team
    membership changes, domain/platform visibility shares and revocations, and RBAC role lifecycle
    events — newest first, paginated. Org-admin only (403 otherwise). Org-scoped: only the caller's own
    organisation's events are ever returned.

    Filterable by ``event_type`` (e.g. ``domain_shared``, ``team_member_added``, ``role_assigned``) and
    date range (``start_date`` / ``end_date``, ISO-8601). A date-only ``end_date`` is inclusive of the
    whole day.

    Known event types: ``team_member_added``, ``team_member_removed``, ``domain_shared``,
    ``platform_shared``, ``share_revoked``, ``role_created``, ``role_updated``, ``role_deleted``,
    ``role_assigned``, ``role_revoked``, ``org_admin_granted``, ``org_admin_revoked``.

    Note: SSO/login authentication events are not currently written to this trail. Coverage is limited
    to team/sharing/role events.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        event_type (None | str | Unset): Filter to a single event type (e.g. 'domain_shared').
        start_date (None | str | Unset): Only events at or after this ISO date/datetime.
        end_date (None | str | Unset): Only events at or before this ISO date/datetime (date =
            inclusive of the day).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SharingAuditListOut | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        event_type=event_type,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    event_type: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
) -> Any | SharingAuditListOut | list[ValidationErrorModel] | None:
    """List sharing/team/role audit events (SIEM export)

     Returns the append-only sharing/team/role audit trail for the caller's organisation — team
    membership changes, domain/platform visibility shares and revocations, and RBAC role lifecycle
    events — newest first, paginated. Org-admin only (403 otherwise). Org-scoped: only the caller's own
    organisation's events are ever returned.

    Filterable by ``event_type`` (e.g. ``domain_shared``, ``team_member_added``, ``role_assigned``) and
    date range (``start_date`` / ``end_date``, ISO-8601). A date-only ``end_date`` is inclusive of the
    whole day.

    Known event types: ``team_member_added``, ``team_member_removed``, ``domain_shared``,
    ``platform_shared``, ``share_revoked``, ``role_created``, ``role_updated``, ``role_deleted``,
    ``role_assigned``, ``role_revoked``, ``org_admin_granted``, ``org_admin_revoked``.

    Note: SSO/login authentication events are not currently written to this trail. Coverage is limited
    to team/sharing/role events.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        event_type (None | str | Unset): Filter to a single event type (e.g. 'domain_shared').
        start_date (None | str | Unset): Only events at or after this ISO date/datetime.
        end_date (None | str | Unset): Only events at or before this ISO date/datetime (date =
            inclusive of the day).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SharingAuditListOut | list[ValidationErrorModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            event_type=event_type,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
