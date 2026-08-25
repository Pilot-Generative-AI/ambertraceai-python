from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_query_request import BatchQueryRequest
from ...models.batch_query_response import BatchQueryResponse
from ...models.validation_error_model import ValidationErrorModel
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: BatchQueryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/platforms/{id}/query-batch".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BatchQueryResponse | list[ValidationErrorModel] | None:
    if response.status_code == 200:
        response_200 = BatchQueryResponse.from_dict(response.json())

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
) -> Response[BatchQueryResponse | list[ValidationErrorModel]]:
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
    body: BatchQueryRequest,
) -> Response[BatchQueryResponse | list[ValidationErrorModel]]:
    r"""Run batch neurosymbolic queries

     Executes N neurosymbolic queries against a single platform in one call. Each query item is
    independent — a failure in one item produces a per-item error object (``status: \"error\"``), never
    a batch-level failure. Results are returned in the same order as the request ``queries`` list.

    The batch-level ``projection`` parameter applies to all items that do not override it with their own
    per-item ``projection``. Maximum 10 queries per batch (synchronous-latency budget).

    A per-batch wall-clock budget (default 30s, env ``AMBERTRACE_BATCH_QUERY_BUDGET_S``) caps total
    execution time. Items that would exceed the budget receive a per-item ``batch_budget_exhausted``
    error; already-processed items keep their real results (partial completion, never a dropped batch).

    Capability gating: requires the \"query\" capability (see GET /api/v1/capabilities). Returns 403
    capability_disabled when the capability is not enabled for the org.

    Each item supports the same parameters as the single-query endpoint (``query``, ``explain``,
    ``top_k``, ``facts``, ``predictions``, ``relations``). Per-item semantics (proof, certified facts,
    decision) are identical to the single-query endpoint.

    Args:
        id (int): Resource ID
        body (BatchQueryRequest): Batch query request — N queries in one call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchQueryResponse | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: BatchQueryRequest,
) -> BatchQueryResponse | list[ValidationErrorModel] | None:
    r"""Run batch neurosymbolic queries

     Executes N neurosymbolic queries against a single platform in one call. Each query item is
    independent — a failure in one item produces a per-item error object (``status: \"error\"``), never
    a batch-level failure. Results are returned in the same order as the request ``queries`` list.

    The batch-level ``projection`` parameter applies to all items that do not override it with their own
    per-item ``projection``. Maximum 10 queries per batch (synchronous-latency budget).

    A per-batch wall-clock budget (default 30s, env ``AMBERTRACE_BATCH_QUERY_BUDGET_S``) caps total
    execution time. Items that would exceed the budget receive a per-item ``batch_budget_exhausted``
    error; already-processed items keep their real results (partial completion, never a dropped batch).

    Capability gating: requires the \"query\" capability (see GET /api/v1/capabilities). Returns 403
    capability_disabled when the capability is not enabled for the org.

    Each item supports the same parameters as the single-query endpoint (``query``, ``explain``,
    ``top_k``, ``facts``, ``predictions``, ``relations``). Per-item semantics (proof, certified facts,
    decision) are identical to the single-query endpoint.

    Args:
        id (int): Resource ID
        body (BatchQueryRequest): Batch query request — N queries in one call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchQueryResponse | list[ValidationErrorModel]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: BatchQueryRequest,
) -> Response[BatchQueryResponse | list[ValidationErrorModel]]:
    r"""Run batch neurosymbolic queries

     Executes N neurosymbolic queries against a single platform in one call. Each query item is
    independent — a failure in one item produces a per-item error object (``status: \"error\"``), never
    a batch-level failure. Results are returned in the same order as the request ``queries`` list.

    The batch-level ``projection`` parameter applies to all items that do not override it with their own
    per-item ``projection``. Maximum 10 queries per batch (synchronous-latency budget).

    A per-batch wall-clock budget (default 30s, env ``AMBERTRACE_BATCH_QUERY_BUDGET_S``) caps total
    execution time. Items that would exceed the budget receive a per-item ``batch_budget_exhausted``
    error; already-processed items keep their real results (partial completion, never a dropped batch).

    Capability gating: requires the \"query\" capability (see GET /api/v1/capabilities). Returns 403
    capability_disabled when the capability is not enabled for the org.

    Each item supports the same parameters as the single-query endpoint (``query``, ``explain``,
    ``top_k``, ``facts``, ``predictions``, ``relations``). Per-item semantics (proof, certified facts,
    decision) are identical to the single-query endpoint.

    Args:
        id (int): Resource ID
        body (BatchQueryRequest): Batch query request — N queries in one call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchQueryResponse | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: BatchQueryRequest,
) -> BatchQueryResponse | list[ValidationErrorModel] | None:
    r"""Run batch neurosymbolic queries

     Executes N neurosymbolic queries against a single platform in one call. Each query item is
    independent — a failure in one item produces a per-item error object (``status: \"error\"``), never
    a batch-level failure. Results are returned in the same order as the request ``queries`` list.

    The batch-level ``projection`` parameter applies to all items that do not override it with their own
    per-item ``projection``. Maximum 10 queries per batch (synchronous-latency budget).

    A per-batch wall-clock budget (default 30s, env ``AMBERTRACE_BATCH_QUERY_BUDGET_S``) caps total
    execution time. Items that would exceed the budget receive a per-item ``batch_budget_exhausted``
    error; already-processed items keep their real results (partial completion, never a dropped batch).

    Capability gating: requires the \"query\" capability (see GET /api/v1/capabilities). Returns 403
    capability_disabled when the capability is not enabled for the org.

    Each item supports the same parameters as the single-query endpoint (``query``, ``explain``,
    ``top_k``, ``facts``, ``predictions``, ``relations``). Per-item semantics (proof, certified facts,
    decision) are identical to the single-query endpoint.

    Args:
        id (int): Resource ID
        body (BatchQueryRequest): Batch query request — N queries in one call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchQueryResponse | list[ValidationErrorModel]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
