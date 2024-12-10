# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..core.request_options import RequestOptions
from ..types.interactive_response import InteractiveResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.code_synthesis_response import CodeSynthesisResponse
from ..types.magic_response import MagicResponse
from ..core.client_wrapper import AsyncClientWrapper


class ExperimentalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def assistant(
        self, *, query: str, context: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InteractiveResponse:
        """
        Interactive assistant for IDE extension

        Parameters
        ----------
        query : str

        context : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InteractiveResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.experimental.assistant(
            query="query",
            context="context",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "experimental/assistant",
            method="POST",
            params={
                "query": query,
                "context": context,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    InteractiveResponse,
                    parse_obj_as(
                        type_=InteractiveResponse,  # type: ignore
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

    def synthesize(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CodeSynthesisResponse:
        """
        Synthesize GDS factory code from a statement describing a PIC

        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CodeSynthesisResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.experimental.synthesize(
            query="query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "experimental/pic/code/synthesize",
            method="POST",
            params={
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CodeSynthesisResponse,
                    parse_obj_as(
                        type_=CodeSynthesisResponse,  # type: ignore
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

    def magic_request(
        self, *, query: str, cell: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> MagicResponse:
        """
        Interactive assistant for IPython extension

        Parameters
        ----------
        query : str

        cell : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MagicResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.experimental.magic_request(
            query="query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "experimental/circuit_assistant",
            method="POST",
            params={
                "query": query,
                "cell": cell,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MagicResponse,
                    parse_obj_as(
                        type_=MagicResponse,  # type: ignore
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


class AsyncExperimentalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def assistant(
        self, *, query: str, context: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InteractiveResponse:
        """
        Interactive assistant for IDE extension

        Parameters
        ----------
        query : str

        context : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InteractiveResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.experimental.assistant(
                query="query",
                context="context",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experimental/assistant",
            method="POST",
            params={
                "query": query,
                "context": context,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    InteractiveResponse,
                    parse_obj_as(
                        type_=InteractiveResponse,  # type: ignore
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

    async def synthesize(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CodeSynthesisResponse:
        """
        Synthesize GDS factory code from a statement describing a PIC

        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CodeSynthesisResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.experimental.synthesize(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experimental/pic/code/synthesize",
            method="POST",
            params={
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CodeSynthesisResponse,
                    parse_obj_as(
                        type_=CodeSynthesisResponse,  # type: ignore
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

    async def magic_request(
        self, *, query: str, cell: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> MagicResponse:
        """
        Interactive assistant for IPython extension

        Parameters
        ----------
        query : str

        cell : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MagicResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.experimental.magic_request(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experimental/circuit_assistant",
            method="POST",
            params={
                "query": query,
                "cell": cell,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MagicResponse,
                    parse_obj_as(
                        type_=MagicResponse,  # type: ignore
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
