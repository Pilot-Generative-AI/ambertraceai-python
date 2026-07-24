from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.compile_policy_request import CompilePolicyRequest
from ...models.validation_error_model import ValidationErrorModel
from ...types import Response


def _get_kwargs(
    *,
    body: CompilePolicyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/agent-policy-gate/policy",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ValidationErrorModel] | None:
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
) -> Response[list[ValidationErrorModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CompilePolicyRequest,
) -> Response[list[ValidationErrorModel]]:
    """Author the governance policy in natural language (compile → admit → build)

     Compiles a natural-language governance policy into a verified agent-policy platform,
    building/replacing the org's existing one. Authoring is slow + external, so it runs in the
    BACKGROUND: this returns 202 with a job_id the client polls via GET /agent-policy-
    gate/policy/jobs/{job_id} until the job completes. The completed job reports one of: done (admitted
    rules + rejected proposals); vacuous (no valid controls — existing policy unchanged); unavailable
    (compiler temporarily down — retry); error. Feature-flagged; 404 when disabled.

    Args:
        body (CompilePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CompilePolicyRequest,
) -> list[ValidationErrorModel] | None:
    """Author the governance policy in natural language (compile → admit → build)

     Compiles a natural-language governance policy into a verified agent-policy platform,
    building/replacing the org's existing one. Authoring is slow + external, so it runs in the
    BACKGROUND: this returns 202 with a job_id the client polls via GET /agent-policy-
    gate/policy/jobs/{job_id} until the job completes. The completed job reports one of: done (admitted
    rules + rejected proposals); vacuous (no valid controls — existing policy unchanged); unavailable
    (compiler temporarily down — retry); error. Feature-flagged; 404 when disabled.

    Args:
        body (CompilePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ValidationErrorModel]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CompilePolicyRequest,
) -> Response[list[ValidationErrorModel]]:
    """Author the governance policy in natural language (compile → admit → build)

     Compiles a natural-language governance policy into a verified agent-policy platform,
    building/replacing the org's existing one. Authoring is slow + external, so it runs in the
    BACKGROUND: this returns 202 with a job_id the client polls via GET /agent-policy-
    gate/policy/jobs/{job_id} until the job completes. The completed job reports one of: done (admitted
    rules + rejected proposals); vacuous (no valid controls — existing policy unchanged); unavailable
    (compiler temporarily down — retry); error. Feature-flagged; 404 when disabled.

    Args:
        body (CompilePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CompilePolicyRequest,
) -> list[ValidationErrorModel] | None:
    """Author the governance policy in natural language (compile → admit → build)

     Compiles a natural-language governance policy into a verified agent-policy platform,
    building/replacing the org's existing one. Authoring is slow + external, so it runs in the
    BACKGROUND: this returns 202 with a job_id the client polls via GET /agent-policy-
    gate/policy/jobs/{job_id} until the job completes. The completed job reports one of: done (admitted
    rules + rejected proposals); vacuous (no valid controls — existing policy unchanged); unavailable
    (compiler temporarily down — retry); error. Feature-flagged; 404 when disabled.

    Args:
        body (CompilePolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ValidationErrorModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
