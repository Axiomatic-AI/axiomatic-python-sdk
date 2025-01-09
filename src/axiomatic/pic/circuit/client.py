# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.formalize_circuit_response import FormalizeCircuitResponse
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.generate_code_response import GenerateCodeResponse
from ...types.refine_code_response import RefineCodeResponse
from ...types.netlist import Netlist
from ...types.statement import Statement
from ...types.measurement import Measurement
from ...types.optimize_netlist_response import OptimizeNetlistResponse
from ...core.serialization import convert_and_respect_annotation_metadata
from ...types.verify_circuit_code_response import VerifyCircuitCodeResponse
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CircuitClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def formalize(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FormalizeCircuitResponse:
        """
        Formalize a query about a circuit into a dictionary of constraints

        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormalizeCircuitResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.pic.circuit.formalize(
            query="query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "pic/circuit/query/formalize",
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
                    FormalizeCircuitResponse,
                    parse_obj_as(
                        type_=FormalizeCircuitResponse,  # type: ignore
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

    def generate(self, *, query: str, request_options: typing.Optional[RequestOptions] = None) -> GenerateCodeResponse:
        """
        Generate GDS factory code to create a circuit

        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateCodeResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.pic.circuit.generate(
            query="query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "pic/circuit/generate",
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
                    GenerateCodeResponse,
                    parse_obj_as(
                        type_=GenerateCodeResponse,  # type: ignore
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

    def refine(
        self,
        *,
        query: str,
        feedback: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefineCodeResponse:
        """
        Refine GDS factory code to create a circuit

        Parameters
        ----------
        query : str

        feedback : typing.Optional[str]

        code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefineCodeResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.pic.circuit.refine(
            query="query",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "pic/circuit/refine",
            method="POST",
            json={
                "query": query,
                "feedback": feedback,
                "code": code,
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
                    RefineCodeResponse,
                    parse_obj_as(
                        type_=RefineCodeResponse,  # type: ignore
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

    def optimize(
        self,
        *,
        netlist: Netlist,
        statements: typing.Sequence[Statement],
        measurements: typing.Sequence[Measurement],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OptimizeNetlistResponse:
        """
        Optimize a PIC circuit with given cost and constraints

        Parameters
        ----------
        netlist : Netlist

        statements : typing.Sequence[Statement]

        measurements : typing.Sequence[Measurement]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OptimizeNetlistResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic, Measurement, Netlist, PicComponent, Statement

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.pic.circuit.optimize(
            netlist=Netlist(
                name="name",
                instances={
                    "key": PicComponent(
                        component="component",
                    )
                },
                connections={"key": "value"},
                ports={"key": "value"},
            ),
            statements=[
                Statement(
                    id="id",
                    statement="statement",
                )
            ],
            measurements=[
                Measurement(
                    variable="variable",
                    arguments={"key": "value"},
                    measurement_name="measurement_name",
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "pic/circuit/optimize",
            method="POST",
            json={
                "netlist": convert_and_respect_annotation_metadata(
                    object_=netlist, annotation=Netlist, direction="write"
                ),
                "statements": convert_and_respect_annotation_metadata(
                    object_=statements, annotation=typing.Sequence[Statement], direction="write"
                ),
                "measurements": convert_and_respect_annotation_metadata(
                    object_=measurements, annotation=typing.Sequence[Measurement], direction="write"
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
                    OptimizeNetlistResponse,
                    parse_obj_as(
                        type_=OptimizeNetlistResponse,  # type: ignore
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

    def verify(
        self, *, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifyCircuitCodeResponse:
        """
        Verifies that the code for a circuit

        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyCircuitCodeResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.pic.circuit.verify(
            code="code",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "pic/circuit/verifycode",
            method="POST",
            json={
                "code": code,
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
                    VerifyCircuitCodeResponse,
                    parse_obj_as(
                        type_=VerifyCircuitCodeResponse,  # type: ignore
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


class AsyncCircuitClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def formalize(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FormalizeCircuitResponse:
        """
        Formalize a query about a circuit into a dictionary of constraints

        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormalizeCircuitResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pic.circuit.formalize(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pic/circuit/query/formalize",
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
                    FormalizeCircuitResponse,
                    parse_obj_as(
                        type_=FormalizeCircuitResponse,  # type: ignore
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

    async def generate(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerateCodeResponse:
        """
        Generate GDS factory code to create a circuit

        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerateCodeResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pic.circuit.generate(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pic/circuit/generate",
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
                    GenerateCodeResponse,
                    parse_obj_as(
                        type_=GenerateCodeResponse,  # type: ignore
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

    async def refine(
        self,
        *,
        query: str,
        feedback: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefineCodeResponse:
        """
        Refine GDS factory code to create a circuit

        Parameters
        ----------
        query : str

        feedback : typing.Optional[str]

        code : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefineCodeResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pic.circuit.refine(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pic/circuit/refine",
            method="POST",
            json={
                "query": query,
                "feedback": feedback,
                "code": code,
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
                    RefineCodeResponse,
                    parse_obj_as(
                        type_=RefineCodeResponse,  # type: ignore
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

    async def optimize(
        self,
        *,
        netlist: Netlist,
        statements: typing.Sequence[Statement],
        measurements: typing.Sequence[Measurement],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OptimizeNetlistResponse:
        """
        Optimize a PIC circuit with given cost and constraints

        Parameters
        ----------
        netlist : Netlist

        statements : typing.Sequence[Statement]

        measurements : typing.Sequence[Measurement]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OptimizeNetlistResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import (
            AsyncAxiomatic,
            Measurement,
            Netlist,
            PicComponent,
            Statement,
        )

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pic.circuit.optimize(
                netlist=Netlist(
                    name="name",
                    instances={
                        "key": PicComponent(
                            component="component",
                        )
                    },
                    connections={"key": "value"},
                    ports={"key": "value"},
                ),
                statements=[
                    Statement(
                        id="id",
                        statement="statement",
                    )
                ],
                measurements=[
                    Measurement(
                        variable="variable",
                        arguments={"key": "value"},
                        measurement_name="measurement_name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pic/circuit/optimize",
            method="POST",
            json={
                "netlist": convert_and_respect_annotation_metadata(
                    object_=netlist, annotation=Netlist, direction="write"
                ),
                "statements": convert_and_respect_annotation_metadata(
                    object_=statements, annotation=typing.Sequence[Statement], direction="write"
                ),
                "measurements": convert_and_respect_annotation_metadata(
                    object_=measurements, annotation=typing.Sequence[Measurement], direction="write"
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
                    OptimizeNetlistResponse,
                    parse_obj_as(
                        type_=OptimizeNetlistResponse,  # type: ignore
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

    async def verify(
        self, *, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifyCircuitCodeResponse:
        """
        Verifies that the code for a circuit

        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyCircuitCodeResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pic.circuit.verify(
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pic/circuit/verifycode",
            method="POST",
            json={
                "code": code,
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
                    VerifyCircuitCodeResponse,
                    parse_obj_as(
                        type_=VerifyCircuitCodeResponse,  # type: ignore
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
