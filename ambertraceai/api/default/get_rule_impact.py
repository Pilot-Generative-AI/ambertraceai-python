from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rule_impact_response import RuleImpactResponse
from ...models.validation_error_model import ValidationErrorModel
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/platforms/{id}/graph/rule-impact".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RuleImpactResponse | list[ValidationErrorModel] | None:
    if response.status_code == 200:
        response_200 = RuleImpactResponse.from_dict(response.json())

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
) -> Response[RuleImpactResponse | list[ValidationErrorModel]]:
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
) -> Response[RuleImpactResponse | list[ValidationErrorModel]]:
    """Rule impact analysis

     Returns all live decisions that depend on a given rule. Pairs with rule_edit_gate: before editing or
    deleting a rule, check which decisions would be affected.

    The rule is identified by name (the same identifier convention used by the rule edit API). Returns
    decision nodes with their properties (audit_log_id, report_id, query, proof_checked).

    Args:
        id (int): Resource ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RuleImpactResponse | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> RuleImpactResponse | list[ValidationErrorModel] | None:
    """Rule impact analysis

     Returns all live decisions that depend on a given rule. Pairs with rule_edit_gate: before editing or
    deleting a rule, check which decisions would be affected.

    The rule is identified by name (the same identifier convention used by the rule edit API). Returns
    decision nodes with their properties (audit_log_id, report_id, query, proof_checked).

    Args:
        id (int): Resource ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RuleImpactResponse | list[ValidationErrorModel]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RuleImpactResponse | list[ValidationErrorModel]]:
    """Rule impact analysis

     Returns all live decisions that depend on a given rule. Pairs with rule_edit_gate: before editing or
    deleting a rule, check which decisions would be affected.

    The rule is identified by name (the same identifier convention used by the rule edit API). Returns
    decision nodes with their properties (audit_log_id, report_id, query, proof_checked).

    Args:
        id (int): Resource ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RuleImpactResponse | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> RuleImpactResponse | list[ValidationErrorModel] | None:
    """Rule impact analysis

     Returns all live decisions that depend on a given rule. Pairs with rule_edit_gate: before editing or
    deleting a rule, check which decisions would be affected.

    The rule is identified by name (the same identifier convention used by the rule edit API). Returns
    decision nodes with their properties (audit_log_id, report_id, query, proof_checked).

    Args:
        id (int): Resource ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RuleImpactResponse | list[ValidationErrorModel]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
