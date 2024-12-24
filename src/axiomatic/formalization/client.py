# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.formalize_response import FormalizeResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.validate_response import ValidateResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FormalizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def formalize(
        self,
        *,
        query: str,
        domain: typing.Optional[typing.Literal["PIC"]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FormalizeResponse:
        """
        Formalize a query into a dictionary of constraints

        Parameters
        ----------
        query : str

        domain : typing.Optional[typing.Literal["PIC"]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormalizeResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.formalization.formalize(
            query="query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "formalization/formalize",
            method="POST",
            json={
                "query": query,
                "domain": domain,
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
                    FormalizeResponse,
                    parse_obj_as(
                        type_=FormalizeResponse,  # type: ignore
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

    def validate(
        self,
        *,
        constraints: FormalizeResponse,
        values: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidateResponse:
        """
        Validate a set of values with respect to a dictionary of constraints

        Parameters
        ----------
        constraints : FormalizeResponse

        values : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidateResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic, FormalizeResponse

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.formalization.validate(
            constraints=FormalizeResponse(
                variables={"key": "value"},
                expressions=[],
            ),
            values={"key": "value"},
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "formalization/validate",
            method="POST",
            json={
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints, annotation=FormalizeResponse, direction="write"
                ),
                "values": values,
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
                    ValidateResponse,
                    parse_obj_as(
                        type_=ValidateResponse,  # type: ignore
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


class AsyncFormalizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def formalize(
        self,
        *,
        query: str,
        domain: typing.Optional[typing.Literal["PIC"]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FormalizeResponse:
        """
        Formalize a query into a dictionary of constraints

        Parameters
        ----------
        query : str

        domain : typing.Optional[typing.Literal["PIC"]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormalizeResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.formalization.formalize(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "formalization/formalize",
            method="POST",
            json={
                "query": query,
                "domain": domain,
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
                    FormalizeResponse,
                    parse_obj_as(
                        type_=FormalizeResponse,  # type: ignore
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

    async def validate(
        self,
        *,
        constraints: FormalizeResponse,
        values: typing.Dict[str, str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidateResponse:
        """
        Validate a set of values with respect to a dictionary of constraints

        Parameters
        ----------
        constraints : FormalizeResponse

        values : typing.Dict[str, str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic, FormalizeResponse

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.formalization.validate(
                constraints=FormalizeResponse(
                    variables={"key": "value"},
                    expressions=[],
                ),
                values={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "formalization/validate",
            method="POST",
            json={
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints, annotation=FormalizeResponse, direction="write"
                ),
                "values": values,
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
                    ValidateResponse,
                    parse_obj_as(
                        type_=ValidateResponse,  # type: ignore
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