from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.access_review_snapshot_out import AccessReviewSnapshotOut
from ...models.validation_error_model import ValidationErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/access-review",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccessReviewSnapshotOut | Any | list[ValidationErrorModel] | None:
    if response.status_code == 200:
        response_200 = AccessReviewSnapshotOut.from_dict(response.json())

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
) -> Response[AccessReviewSnapshotOut | Any | list[ValidationErrorModel]]:
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
) -> Response[AccessReviewSnapshotOut | Any | list[ValidationErrorModel]]:
    """Access-review snapshot (SOC 2 CC6.2/CC6.3)

     Returns a point-in-time snapshot of every member in the caller's organisation with their current
    RBAC role assignments. Designed for periodic access-review evidence (SOC 2 CC6.2/CC6.3): export the
    snapshot, diff against the previous period, and flag stale entitlements.

    Org-admin only (403 otherwise). Org-scoped: only the caller's own organisation's members are ever
    returned. Each member entry includes ``is_org_admin`` (boolean) and a ``roles`` list with role name,
    assignment source (``manual`` / ``sso`` / ``scim``), and assignment date. Members with no role
    assignments appear with an empty ``roles`` list. Paginated via ``limit`` / ``offset``.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccessReviewSnapshotOut | Any | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
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
) -> AccessReviewSnapshotOut | Any | list[ValidationErrorModel] | None:
    """Access-review snapshot (SOC 2 CC6.2/CC6.3)

     Returns a point-in-time snapshot of every member in the caller's organisation with their current
    RBAC role assignments. Designed for periodic access-review evidence (SOC 2 CC6.2/CC6.3): export the
    snapshot, diff against the previous period, and flag stale entitlements.

    Org-admin only (403 otherwise). Org-scoped: only the caller's own organisation's members are ever
    returned. Each member entry includes ``is_org_admin`` (boolean) and a ``roles`` list with role name,
    assignment source (``manual`` / ``sso`` / ``scim``), and assignment date. Members with no role
    assignments appear with an empty ``roles`` list. Paginated via ``limit`` / ``offset``.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccessReviewSnapshotOut | Any | list[ValidationErrorModel]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[AccessReviewSnapshotOut | Any | list[ValidationErrorModel]]:
    """Access-review snapshot (SOC 2 CC6.2/CC6.3)

     Returns a point-in-time snapshot of every member in the caller's organisation with their current
    RBAC role assignments. Designed for periodic access-review evidence (SOC 2 CC6.2/CC6.3): export the
    snapshot, diff against the previous period, and flag stale entitlements.

    Org-admin only (403 otherwise). Org-scoped: only the caller's own organisation's members are ever
    returned. Each member entry includes ``is_org_admin`` (boolean) and a ``roles`` list with role name,
    assignment source (``manual`` / ``sso`` / ``scim``), and assignment date. Members with no role
    assignments appear with an empty ``roles`` list. Paginated via ``limit`` / ``offset``.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccessReviewSnapshotOut | Any | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> AccessReviewSnapshotOut | Any | list[ValidationErrorModel] | None:
    """Access-review snapshot (SOC 2 CC6.2/CC6.3)

     Returns a point-in-time snapshot of every member in the caller's organisation with their current
    RBAC role assignments. Designed for periodic access-review evidence (SOC 2 CC6.2/CC6.3): export the
    snapshot, diff against the previous period, and flag stale entitlements.

    Org-admin only (403 otherwise). Org-scoped: only the caller's own organisation's members are ever
    returned. Each member entry includes ``is_org_admin`` (boolean) and a ``roles`` list with role name,
    assignment source (``manual`` / ``sso`` / ``scim``), and assignment date. Members with no role
    assignments appear with an empty ``roles`` list. Paginated via ``limit`` / ``offset``.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccessReviewSnapshotOut | Any | list[ValidationErrorModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
