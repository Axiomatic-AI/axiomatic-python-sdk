# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...types.formalize_response import FormalizeResponse
from .types.solution_body_values_value import SolutionBodyValuesValue
from ...core.request_options import RequestOptions
from ...types.solution_response import SolutionResponse
from ...core.serialization import convert_and_respect_annotation_metadata
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SolutionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find(
        self,
        *,
        constraints: FormalizeResponse,
        values: typing.Dict[str, SolutionBodyValuesValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SolutionResponse:
        """
        Finds a solution to a set of constraints provided partial values

        Parameters
        ----------
        constraints : FormalizeResponse

        values : typing.Dict[str, SolutionBodyValuesValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SolutionResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic, FormalizeResponse

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.formalization.solution.find(
            constraints=FormalizeResponse(
                variables={"key": "value"},
                expressions=[],
            ),
            values={"key": 1},
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "formalization/solution/find",
            method="POST",
            json={
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints, annotation=FormalizeResponse, direction="write"
                ),
                "values": convert_and_respect_annotation_metadata(
                    object_=values, annotation=typing.Dict[str, SolutionBodyValuesValue], direction="write"
                ),
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
                    SolutionResponse,
                    parse_obj_as(
                        type_=SolutionResponse,  # type: ignore
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


class AsyncSolutionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def find(
        self,
        *,
        constraints: FormalizeResponse,
        values: typing.Dict[str, SolutionBodyValuesValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SolutionResponse:
        """
        Finds a solution to a set of constraints provided partial values

        Parameters
        ----------
        constraints : FormalizeResponse

        values : typing.Dict[str, SolutionBodyValuesValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SolutionResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic, FormalizeResponse

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.formalization.solution.find(
                constraints=FormalizeResponse(
                    variables={"key": "value"},
                    expressions=[],
                ),
                values={"key": 1},
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "formalization/solution/find",
            method="POST",
            json={
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints, annotation=FormalizeResponse, direction="write"
                ),
                "values": convert_and_respect_annotation_metadata(
                    object_=values, annotation=typing.Dict[str, SolutionBodyValuesValue], direction="write"
                ),
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
                    SolutionResponse,
                    parse_obj_as(
                        type_=SolutionResponse,  # type: ignore
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
