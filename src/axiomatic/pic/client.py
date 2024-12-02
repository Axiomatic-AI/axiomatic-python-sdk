# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .. import core
from ..core.request_options import RequestOptions
from ..types.extract_response import ExtractResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.extract_statements_response import ExtractStatementsResponse
from ..types.extract_title_response import ExtractTitleResponse
from ..types.statement_input import StatementInput
from ..types.extract_links_response import ExtractLinksResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.synthesis_response import SynthesisResponse
from ..types.synthesize_circuit_response import SynthesizeCircuitResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PicClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def extract(self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None) -> ExtractResponse:
        """
        Extract statements and circuit image from a PDF describing a PIC

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.pic.extract()
        """
        _response = self._client_wrapper.httpx_client.request(
            "pic/extract",
            method="POST",
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
                    ExtractResponse,
                    parse_obj_as(
                        type_=ExtractResponse,  # type: ignore
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

    def extract_from_text(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractStatementsResponse:
        """
        Extract statements from text describing a PIC

        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractStatementsResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.pic.extract_from_text(
            query="query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "pic/text/statements/extract",
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
                    ExtractStatementsResponse,
                    parse_obj_as(
                        type_=ExtractStatementsResponse,  # type: ignore
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

    def extract_from_paper(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractTitleResponse:
        """
        Extract title from a PDF describing a PIC

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractTitleResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.pic.extract_from_paper()
        """
        _response = self._client_wrapper.httpx_client.request(
            "pic/paper/title/extract",
            method="POST",
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
                    ExtractTitleResponse,
                    parse_obj_as(
                        type_=ExtractTitleResponse,  # type: ignore
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

    def identify(
        self, *, statements: typing.Sequence[StatementInput], request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractLinksResponse:
        """
        Identify links between statements

        Parameters
        ----------
        statements : typing.Sequence[StatementInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractLinksResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic, StatementInput

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.pic.identify(
            statements=[
                StatementInput(
                    id="id",
                    statement="statement",
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "pic/links/indentify",
            method="POST",
            json={
                "statements": convert_and_respect_annotation_metadata(
                    object_=statements, annotation=typing.Sequence[StatementInput], direction="write"
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
                    ExtractLinksResponse,
                    parse_obj_as(
                        type_=ExtractLinksResponse,  # type: ignore
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

    def identify_with_context(
        self,
        *,
        statements: str,
        file: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractLinksResponse:
        """
        Identify links between statements with the context of a paper

        Parameters
        ----------
        statements : str
            List of statements

        file : typing.Optional[str]
            PDF of file e.g. a paper to provide context

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractLinksResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.pic.identify_with_context(
            statements="statements",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "pic/paper/links/indentify",
            method="POST",
            data={
                "statements": statements,
                "file": file,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExtractLinksResponse,
                    parse_obj_as(
                        type_=ExtractLinksResponse,  # type: ignore
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

    def synthesize_circuit_from_paper(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> SynthesisResponse:
        """
        Synthesize circuit from a PDF describing a PIC

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SynthesisResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.pic.synthesize_circuit_from_paper()
        """
        _response = self._client_wrapper.httpx_client.request(
            "pic/paper/circuit/synthesize",
            method="POST",
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
                    SynthesisResponse,
                    parse_obj_as(
                        type_=SynthesisResponse,  # type: ignore
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

    def synthesize_circuit_from_text(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SynthesizeCircuitResponse:
        """
        Synthesize circuit from a string describing a PIC

        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SynthesizeCircuitResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.pic.synthesize_circuit_from_text(
            query="query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "pic/text/circuit/synthesize",
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
                    SynthesizeCircuitResponse,
                    parse_obj_as(
                        type_=SynthesizeCircuitResponse,  # type: ignore
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


class AsyncPicClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def extract(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractResponse:
        """
        Extract statements and circuit image from a PDF describing a PIC

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pic.extract()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pic/extract",
            method="POST",
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
                    ExtractResponse,
                    parse_obj_as(
                        type_=ExtractResponse,  # type: ignore
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

    async def extract_from_text(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractStatementsResponse:
        """
        Extract statements from text describing a PIC

        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractStatementsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pic.extract_from_text(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pic/text/statements/extract",
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
                    ExtractStatementsResponse,
                    parse_obj_as(
                        type_=ExtractStatementsResponse,  # type: ignore
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

    async def extract_from_paper(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractTitleResponse:
        """
        Extract title from a PDF describing a PIC

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractTitleResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pic.extract_from_paper()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pic/paper/title/extract",
            method="POST",
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
                    ExtractTitleResponse,
                    parse_obj_as(
                        type_=ExtractTitleResponse,  # type: ignore
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

    async def identify(
        self, *, statements: typing.Sequence[StatementInput], request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractLinksResponse:
        """
        Identify links between statements

        Parameters
        ----------
        statements : typing.Sequence[StatementInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractLinksResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic, StatementInput

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pic.identify(
                statements=[
                    StatementInput(
                        id="id",
                        statement="statement",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pic/links/indentify",
            method="POST",
            json={
                "statements": convert_and_respect_annotation_metadata(
                    object_=statements, annotation=typing.Sequence[StatementInput], direction="write"
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
                    ExtractLinksResponse,
                    parse_obj_as(
                        type_=ExtractLinksResponse,  # type: ignore
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

    async def identify_with_context(
        self,
        *,
        statements: str,
        file: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractLinksResponse:
        """
        Identify links between statements with the context of a paper

        Parameters
        ----------
        statements : str
            List of statements

        file : typing.Optional[str]
            PDF of file e.g. a paper to provide context

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractLinksResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pic.identify_with_context(
                statements="statements",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pic/paper/links/indentify",
            method="POST",
            data={
                "statements": statements,
                "file": file,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExtractLinksResponse,
                    parse_obj_as(
                        type_=ExtractLinksResponse,  # type: ignore
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

    async def synthesize_circuit_from_paper(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> SynthesisResponse:
        """
        Synthesize circuit from a PDF describing a PIC

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SynthesisResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pic.synthesize_circuit_from_paper()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pic/paper/circuit/synthesize",
            method="POST",
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
                    SynthesisResponse,
                    parse_obj_as(
                        type_=SynthesisResponse,  # type: ignore
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

    async def synthesize_circuit_from_text(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SynthesizeCircuitResponse:
        """
        Synthesize circuit from a string describing a PIC

        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SynthesizeCircuitResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pic.synthesize_circuit_from_text(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pic/text/circuit/synthesize",
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
                    SynthesizeCircuitResponse,
                    parse_obj_as(
                        type_=SynthesizeCircuitResponse,  # type: ignore
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
