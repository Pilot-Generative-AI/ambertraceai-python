from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_search_result_out import DataSearchResultOut
from ...models.validation_error_model import ValidationErrorModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: None | str | Unset = UNSET,
    asset_class: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    region: None | str | Unset = UNSET,
    currency: None | str | Unset = UNSET,
    tenor: None | str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

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

    json_region: None | str | Unset
    if isinstance(region, Unset):
        json_region = UNSET
    else:
        json_region = region
    params["region"] = json_region

    json_currency: None | str | Unset
    if isinstance(currency, Unset):
        json_currency = UNSET
    else:
        json_currency = currency
    params["currency"] = json_currency

    json_tenor: None | str | Unset
    if isinstance(tenor, Unset):
        json_tenor = UNSET
    else:
        json_tenor = tenor
    params["tenor"] = json_tenor

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/data/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DataSearchResultOut | list[ValidationErrorModel] | None:
    if response.status_code == 200:
        response_200 = DataSearchResultOut.from_dict(response.json())

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
) -> Response[DataSearchResultOut | list[ValidationErrorModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: None | str | Unset = UNSET,
    asset_class: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    region: None | str | Unset = UNSET,
    currency: None | str | Unset = UNSET,
    tenor: None | str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> Response[DataSearchResultOut | list[ValidationErrorModel]]:
    r"""Search connectors and series

     Search the connector and series corpus by structured filters (asset_class, country, region,
    currency, tenor) and/or free-text query. Filters are AND-ed. Region expands to constituent country
    codes (e.g. region=asia matches CN, JP, KR, ...). A connector tagged country=global matches every
    region (e.g. Yahoo Finance under region=asia). Note: euro-area sovereign yield curves are tagged
    country=EA, not DE -- for German rates, use region=eurozone (which includes EA) instead of
    country=DE. Series-level results cover the statically-enumerable set (ECB yield-curve keys, BoE
    known series, FRED DGS family, common macro indicators, the FRED OECD broad share-price family for
    the euro area/UK/US -- monthly broad-market PROXIES (2015=100), NOT the tradeable indices -- and the
    ONS UK CPI family); dynamic dataflow enumeration is follow-up work. UK inflation: q=UK inflation (or
    country=GB) resolves 62 curated ONS CDIDs from dataset MM23 -- the headline index and annual rate
    (D7BT, D7G7), CPIH (L522, L55O), the core/goods/services aggregates (DKC6, DKO8, D7F4, D7NM, D7F5,
    D7NN), and for each of the 12 COICOP divisions its index, annual rate, annual expenditure weight
    (CHZQ-CJUW) and contribution to the all-items annual rate (WUMA-WUNG). q=COICOP 07 returns exactly
    transport's four series. Raise limit (default 50, max 200) to page the whole family in one call,
    then feed the CDIDs to the ons connector: {\"series\": [\"D7BT\", \"D7G7\"], \"dataset\": \"MM23\"}.
    Source: Office for National Statistics, OGL v3.0.

    Args:
        q (None | str | Unset): Free-text search term (lexical, case-insensitive substring match
            on names, descriptions, and series labels).
        asset_class (None | str | Unset): Filter by asset class (e.g. 'rates', 'fx',
            'economics/macro').
        country (None | str | Unset): Filter by country tag (ISO-3166 alpha-2 or aggregate code).
        region (None | str | Unset): Filter by named region group (e.g. 'asia', 'europe',
            'americas', 'developed-markets', 'emerging-markets', 'G7', 'G10', 'eurozone'). Expands to
            the constituent country codes before filtering. A connector tagged country='global'
            matches every region (e.g. Yahoo Finance under region='asia').
        currency (None | str | Unset): Filter by currency tag (ISO-4217 alpha-3 or 'multi').
        tenor (None | str | Unset): Filter by tenor (e.g. '5Y', '10Y', '3M'). Series-level only.
        offset (int | Unset): Pagination offset (default 0). Default: 0.
        limit (int | Unset): Pagination page size (default 50, max 200). Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataSearchResultOut | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        q=q,
        asset_class=asset_class,
        country=country,
        region=region,
        currency=currency,
        tenor=tenor,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: None | str | Unset = UNSET,
    asset_class: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    region: None | str | Unset = UNSET,
    currency: None | str | Unset = UNSET,
    tenor: None | str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> DataSearchResultOut | list[ValidationErrorModel] | None:
    r"""Search connectors and series

     Search the connector and series corpus by structured filters (asset_class, country, region,
    currency, tenor) and/or free-text query. Filters are AND-ed. Region expands to constituent country
    codes (e.g. region=asia matches CN, JP, KR, ...). A connector tagged country=global matches every
    region (e.g. Yahoo Finance under region=asia). Note: euro-area sovereign yield curves are tagged
    country=EA, not DE -- for German rates, use region=eurozone (which includes EA) instead of
    country=DE. Series-level results cover the statically-enumerable set (ECB yield-curve keys, BoE
    known series, FRED DGS family, common macro indicators, the FRED OECD broad share-price family for
    the euro area/UK/US -- monthly broad-market PROXIES (2015=100), NOT the tradeable indices -- and the
    ONS UK CPI family); dynamic dataflow enumeration is follow-up work. UK inflation: q=UK inflation (or
    country=GB) resolves 62 curated ONS CDIDs from dataset MM23 -- the headline index and annual rate
    (D7BT, D7G7), CPIH (L522, L55O), the core/goods/services aggregates (DKC6, DKO8, D7F4, D7NM, D7F5,
    D7NN), and for each of the 12 COICOP divisions its index, annual rate, annual expenditure weight
    (CHZQ-CJUW) and contribution to the all-items annual rate (WUMA-WUNG). q=COICOP 07 returns exactly
    transport's four series. Raise limit (default 50, max 200) to page the whole family in one call,
    then feed the CDIDs to the ons connector: {\"series\": [\"D7BT\", \"D7G7\"], \"dataset\": \"MM23\"}.
    Source: Office for National Statistics, OGL v3.0.

    Args:
        q (None | str | Unset): Free-text search term (lexical, case-insensitive substring match
            on names, descriptions, and series labels).
        asset_class (None | str | Unset): Filter by asset class (e.g. 'rates', 'fx',
            'economics/macro').
        country (None | str | Unset): Filter by country tag (ISO-3166 alpha-2 or aggregate code).
        region (None | str | Unset): Filter by named region group (e.g. 'asia', 'europe',
            'americas', 'developed-markets', 'emerging-markets', 'G7', 'G10', 'eurozone'). Expands to
            the constituent country codes before filtering. A connector tagged country='global'
            matches every region (e.g. Yahoo Finance under region='asia').
        currency (None | str | Unset): Filter by currency tag (ISO-4217 alpha-3 or 'multi').
        tenor (None | str | Unset): Filter by tenor (e.g. '5Y', '10Y', '3M'). Series-level only.
        offset (int | Unset): Pagination offset (default 0). Default: 0.
        limit (int | Unset): Pagination page size (default 50, max 200). Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataSearchResultOut | list[ValidationErrorModel]
    """

    return sync_detailed(
        client=client,
        q=q,
        asset_class=asset_class,
        country=country,
        region=region,
        currency=currency,
        tenor=tenor,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: None | str | Unset = UNSET,
    asset_class: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    region: None | str | Unset = UNSET,
    currency: None | str | Unset = UNSET,
    tenor: None | str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> Response[DataSearchResultOut | list[ValidationErrorModel]]:
    r"""Search connectors and series

     Search the connector and series corpus by structured filters (asset_class, country, region,
    currency, tenor) and/or free-text query. Filters are AND-ed. Region expands to constituent country
    codes (e.g. region=asia matches CN, JP, KR, ...). A connector tagged country=global matches every
    region (e.g. Yahoo Finance under region=asia). Note: euro-area sovereign yield curves are tagged
    country=EA, not DE -- for German rates, use region=eurozone (which includes EA) instead of
    country=DE. Series-level results cover the statically-enumerable set (ECB yield-curve keys, BoE
    known series, FRED DGS family, common macro indicators, the FRED OECD broad share-price family for
    the euro area/UK/US -- monthly broad-market PROXIES (2015=100), NOT the tradeable indices -- and the
    ONS UK CPI family); dynamic dataflow enumeration is follow-up work. UK inflation: q=UK inflation (or
    country=GB) resolves 62 curated ONS CDIDs from dataset MM23 -- the headline index and annual rate
    (D7BT, D7G7), CPIH (L522, L55O), the core/goods/services aggregates (DKC6, DKO8, D7F4, D7NM, D7F5,
    D7NN), and for each of the 12 COICOP divisions its index, annual rate, annual expenditure weight
    (CHZQ-CJUW) and contribution to the all-items annual rate (WUMA-WUNG). q=COICOP 07 returns exactly
    transport's four series. Raise limit (default 50, max 200) to page the whole family in one call,
    then feed the CDIDs to the ons connector: {\"series\": [\"D7BT\", \"D7G7\"], \"dataset\": \"MM23\"}.
    Source: Office for National Statistics, OGL v3.0.

    Args:
        q (None | str | Unset): Free-text search term (lexical, case-insensitive substring match
            on names, descriptions, and series labels).
        asset_class (None | str | Unset): Filter by asset class (e.g. 'rates', 'fx',
            'economics/macro').
        country (None | str | Unset): Filter by country tag (ISO-3166 alpha-2 or aggregate code).
        region (None | str | Unset): Filter by named region group (e.g. 'asia', 'europe',
            'americas', 'developed-markets', 'emerging-markets', 'G7', 'G10', 'eurozone'). Expands to
            the constituent country codes before filtering. A connector tagged country='global'
            matches every region (e.g. Yahoo Finance under region='asia').
        currency (None | str | Unset): Filter by currency tag (ISO-4217 alpha-3 or 'multi').
        tenor (None | str | Unset): Filter by tenor (e.g. '5Y', '10Y', '3M'). Series-level only.
        offset (int | Unset): Pagination offset (default 0). Default: 0.
        limit (int | Unset): Pagination page size (default 50, max 200). Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataSearchResultOut | list[ValidationErrorModel]]
    """

    kwargs = _get_kwargs(
        q=q,
        asset_class=asset_class,
        country=country,
        region=region,
        currency=currency,
        tenor=tenor,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: None | str | Unset = UNSET,
    asset_class: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    region: None | str | Unset = UNSET,
    currency: None | str | Unset = UNSET,
    tenor: None | str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
) -> DataSearchResultOut | list[ValidationErrorModel] | None:
    r"""Search connectors and series

     Search the connector and series corpus by structured filters (asset_class, country, region,
    currency, tenor) and/or free-text query. Filters are AND-ed. Region expands to constituent country
    codes (e.g. region=asia matches CN, JP, KR, ...). A connector tagged country=global matches every
    region (e.g. Yahoo Finance under region=asia). Note: euro-area sovereign yield curves are tagged
    country=EA, not DE -- for German rates, use region=eurozone (which includes EA) instead of
    country=DE. Series-level results cover the statically-enumerable set (ECB yield-curve keys, BoE
    known series, FRED DGS family, common macro indicators, the FRED OECD broad share-price family for
    the euro area/UK/US -- monthly broad-market PROXIES (2015=100), NOT the tradeable indices -- and the
    ONS UK CPI family); dynamic dataflow enumeration is follow-up work. UK inflation: q=UK inflation (or
    country=GB) resolves 62 curated ONS CDIDs from dataset MM23 -- the headline index and annual rate
    (D7BT, D7G7), CPIH (L522, L55O), the core/goods/services aggregates (DKC6, DKO8, D7F4, D7NM, D7F5,
    D7NN), and for each of the 12 COICOP divisions its index, annual rate, annual expenditure weight
    (CHZQ-CJUW) and contribution to the all-items annual rate (WUMA-WUNG). q=COICOP 07 returns exactly
    transport's four series. Raise limit (default 50, max 200) to page the whole family in one call,
    then feed the CDIDs to the ons connector: {\"series\": [\"D7BT\", \"D7G7\"], \"dataset\": \"MM23\"}.
    Source: Office for National Statistics, OGL v3.0.

    Args:
        q (None | str | Unset): Free-text search term (lexical, case-insensitive substring match
            on names, descriptions, and series labels).
        asset_class (None | str | Unset): Filter by asset class (e.g. 'rates', 'fx',
            'economics/macro').
        country (None | str | Unset): Filter by country tag (ISO-3166 alpha-2 or aggregate code).
        region (None | str | Unset): Filter by named region group (e.g. 'asia', 'europe',
            'americas', 'developed-markets', 'emerging-markets', 'G7', 'G10', 'eurozone'). Expands to
            the constituent country codes before filtering. A connector tagged country='global'
            matches every region (e.g. Yahoo Finance under region='asia').
        currency (None | str | Unset): Filter by currency tag (ISO-4217 alpha-3 or 'multi').
        tenor (None | str | Unset): Filter by tenor (e.g. '5Y', '10Y', '3M'). Series-level only.
        offset (int | Unset): Pagination offset (default 0). Default: 0.
        limit (int | Unset): Pagination page size (default 50, max 200). Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataSearchResultOut | list[ValidationErrorModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            asset_class=asset_class,
            country=country,
            region=region,
            currency=currency,
            tenor=tenor,
            offset=offset,
            limit=limit,
        )
    ).parsed
