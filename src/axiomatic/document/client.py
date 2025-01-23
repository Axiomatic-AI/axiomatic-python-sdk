# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .. import core
from ..core.request_options import RequestOptions
from ..types.extract_text_response import ExtractTextResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.parse_response import ParseResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def text(
        self,
        *,
        file: core.File,
        method: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractTextResponse:
        """
        Extracts text from documents

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        method : typing.Optional[str]
            Method to use for text-only extraction.It uses a very simple pdf text extractor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractTextResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.document.text()
        """
        _response = self._client_wrapper.httpx_client.request(
            "document/text",
            method="POST",
            params={
                "method": method,
            },
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExtractTextResponse,
                    parse_obj_as(
                        type_=ExtractTextResponse,  # type: ignore
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

    def parse(
        self,
        *,
        file: core.File,
        method: typing.Optional[str] = None,
        ocr: typing.Optional[bool] = None,
        layout_model: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParseResponse:
        """
        Extracts text from documents. It uses advanced pdf segmentation.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        method : typing.Optional[str]
            Method to use for text extraction

        ocr : typing.Optional[bool]
            Whether to use OCR

        layout_model : typing.Optional[str]
            Method for layout parsing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParseResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.document.parse()
        """
        _response = self._client_wrapper.httpx_client.request(
            "document/parse",
            method="POST",
            params={
                "method": method,
                "ocr": ocr,
                "layout_model": layout_model,
            },
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ParseResponse,
                    parse_obj_as(
                        type_=ParseResponse,  # type: ignore
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


class AsyncDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def text(
        self,
        *,
        file: core.File,
        method: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractTextResponse:
        """
        Extracts text from documents

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        method : typing.Optional[str]
            Method to use for text-only extraction.It uses a very simple pdf text extractor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractTextResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document.text()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "document/text",
            method="POST",
            params={
                "method": method,
            },
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExtractTextResponse,
                    parse_obj_as(
                        type_=ExtractTextResponse,  # type: ignore
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

    async def parse(
        self,
        *,
        file: core.File,
        method: typing.Optional[str] = None,
        ocr: typing.Optional[bool] = None,
        layout_model: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParseResponse:
        """
        Extracts text from documents. It uses advanced pdf segmentation.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        method : typing.Optional[str]
            Method to use for text extraction

        ocr : typing.Optional[bool]
            Whether to use OCR

        layout_model : typing.Optional[str]
            Method for layout parsing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document.parse()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "document/parse",
            method="POST",
            params={
                "method": method,
                "ocr": ocr,
                "layout_model": layout_model,
            },
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ParseResponse,
                    parse_obj_as(
                        type_=ParseResponse,  # type: ignore
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
