# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GenericClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def extract(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.generic.extract(
            query="query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "generic/statement",
            method="POST",
            json={
                "query": query,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncGenericClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def extract(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.generic.extract(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "generic/statement",
            method="POST",
            json={
                "query": query,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)