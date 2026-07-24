from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connector_out import ConnectorOut
from ...models.validation_error_model import ValidationErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_class: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    currency: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_asset_class: None | str | Unset
    if isinstance(asset_class, Unset):
        json_asset_class = UNSET
    else:
        json_asset_class = asset_class
    params["asset_class"] = json_asset_class

    json_country: None | str | Unset
    if isinstance(country, Unset):
        json_country = UNSET
    else:
        json_country = country
    params["country"] = json_country

    json_currency: None | str | Unset
    if isinstance(currency, Unset):
        json_currency = UNSET
    else:
        json_currency = currency
    params["currency"] = json_currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/connectors",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectorOut | list[ValidationErrorModel] | None:
    if response.status_code == 200:
        response_200 = ConnectorOut.from_dict(response.json())

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
) -> Response[ConnectorOut | list[ValidationErrorModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    asset_class: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    currency: None | str | Unset = UNSET,
) -> Response[ConnectorOut | list[ValidationErrorModel]]:
    """List connectors

     Returns all available data connectors with their requirements and taxonomy metadata (asset classes,
    countries, currencies). Optional query-string filters narrow the list: asset_class, country,
    currency (AND-ed).

    Args:
        asset_class (None | str | Unset): Filter by asset class (e.g. 'rates', 'crypto',
            'economics/macro').
        country (None | str | Unset): Filter by country tag (ISO-3166 alpha-2, aggregate code, or
            'global').
        currency (None | str | Unset): Filter by currency tag (ISO-4217 alpha-3 or 'multi').

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectorOut | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        asset_class=asset_class,
        country=country,
        currency=currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    asset_class: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    currency: None | str | Unset = UNSET,
) -> ConnectorOut | list[ValidationErrorModel] | None:
    """List connectors

     Returns all available data connectors with their requirements and taxonomy metadata (asset classes,
    countries, currencies). Optional query-string filters narrow the list: asset_class, country,
    currency (AND-ed).

    Args:
        asset_class (None | str | Unset): Filter by asset class (e.g. 'rates', 'crypto',
            'economics/macro').
        country (None | str | Unset): Filter by country tag (ISO-3166 alpha-2, aggregate code, or
            'global').
        currency (None | str | Unset): Filter by currency tag (ISO-4217 alpha-3 or 'multi').

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectorOut | list[ValidationErrorModel]
    """

    return sync_detailed(
        client=client,
        asset_class=asset_class,
        country=country,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    asset_class: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    currency: None | str | Unset = UNSET,
) -> Response[ConnectorOut | list[ValidationErrorModel]]:
    """List connectors

     Returns all available data connectors with their requirements and taxonomy metadata (asset classes,
    countries, currencies). Optional query-string filters narrow the list: asset_class, country,
    currency (AND-ed).

    Args:
        asset_class (None | str | Unset): Filter by asset class (e.g. 'rates', 'crypto',
            'economics/macro').
        country (None | str | Unset): Filter by country tag (ISO-3166 alpha-2, aggregate code, or
            'global').
        currency (None | str | Unset): Filter by currency tag (ISO-4217 alpha-3 or 'multi').

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectorOut | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        asset_class=asset_class,
        country=country,
        currency=currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    asset_class: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    currency: None | str | Unset = UNSET,
) -> ConnectorOut | list[ValidationErrorModel] | None:
    """List connectors

     Returns all available data connectors with their requirements and taxonomy metadata (asset classes,
    countries, currencies). Optional query-string filters narrow the list: asset_class, country,
    currency (AND-ed).

    Args:
        asset_class (None | str | Unset): Filter by asset class (e.g. 'rates', 'crypto',
            'economics/macro').
        country (None | str | Unset): Filter by country tag (ISO-3166 alpha-2, aggregate code, or
            'global').
        currency (None | str | Unset): Filter by currency tag (ISO-4217 alpha-3 or 'multi').

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectorOut | list[ValidationErrorModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_class=asset_class,
            country=country,
            currency=currency,
        )
    ).parsed
