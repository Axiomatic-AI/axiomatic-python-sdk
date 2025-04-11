# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...types.validation_requirement import ValidationRequirement
from ...types.expression_processing_response import ExpressionProcessingResponse
from ...core.request_options import RequestOptions
from ...types.expression_validation_result import ExpressionValidationResult
from ...core.serialization import convert_and_respect_annotation_metadata
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ExpressionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def validate(
        self,
        *,
        variables: typing.Sequence[ValidationRequirement],
        paper_expressions: ExpressionProcessingResponse,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExpressionValidationResult:
        """
        Validates a set of variables against stored expressions to check for inconsistencies.
        Returns validation results for each relevant expression.

        Parameters
        ----------
        variables : typing.Sequence[ValidationRequirement]

        paper_expressions : ExpressionProcessingResponse

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExpressionValidationResult
            Successful Response

        Examples
        --------
        from axiomatic import (
            Axiomatic,
            Expression,
            ExpressionProcessingResponse,
            Symbol,
            ValidationRequirement,
            ValidationResult,
        )

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.document.expression.validate(
            variables=[
                ValidationRequirement(
                    symbol=Symbol(
                        name="name",
                        wolfram_format="wolfram_format",
                        latex_representation="latex_representation",
                        dimension="dimension",
                        description="description",
                        type="scalar",
                        validations={
                            "key": ValidationResult(
                                is_valid=True,
                                message="message",
                            )
                        },
                    ),
                    value=1.1,
                )
            ],
            paper_expressions=ExpressionProcessingResponse(
                expressions=[
                    Expression(
                        name="name",
                        description="description",
                        original_format="original_format",
                        wolfram_expression="wolfram_expression",
                        symbols={
                            "key": Symbol(
                                name="name",
                                wolfram_format="wolfram_format",
                                latex_representation="latex_representation",
                                dimension="dimension",
                                description="description",
                                type="scalar",
                                validations={
                                    "key": ValidationResult(
                                        is_valid=True,
                                        message="message",
                                    )
                                },
                            )
                        },
                        narrative_assumptions=["narrative_assumptions"],
                        exp_validations={
                            "key": ValidationResult(
                                is_valid=True,
                                message="message",
                            )
                        },
                    )
                ],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "document/expression/validate",
            method="POST",
            json={
                "variables": convert_and_respect_annotation_metadata(
                    object_=variables, annotation=typing.Sequence[ValidationRequirement], direction="write"
                ),
                "paper_expressions": convert_and_respect_annotation_metadata(
                    object_=paper_expressions, annotation=ExpressionProcessingResponse, direction="write"
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
                    ExpressionValidationResult,
                    parse_obj_as(
                        type_=ExpressionValidationResult,  # type: ignore
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

    def process(
        self,
        *,
        markdown: str,
        images: typing.Optional[typing.Dict[str, str]] = OMIT,
        interline_equations: typing.Optional[typing.Sequence[str]] = OMIT,
        inline_equations: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExpressionProcessingResponse:
        """
        Process all expressions at once and return their annotation

        Parameters
        ----------
        markdown : str

        images : typing.Optional[typing.Dict[str, str]]

        interline_equations : typing.Optional[typing.Sequence[str]]

        inline_equations : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExpressionProcessingResponse
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.document.expression.process(
            markdown="markdown",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "document/expression/process",
            method="POST",
            json={
                "markdown": markdown,
                "images": images,
                "interline_equations": interline_equations,
                "inline_equations": inline_equations,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExpressionProcessingResponse,
                    parse_obj_as(
                        type_=ExpressionProcessingResponse,  # type: ignore
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


class AsyncExpressionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def validate(
        self,
        *,
        variables: typing.Sequence[ValidationRequirement],
        paper_expressions: ExpressionProcessingResponse,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExpressionValidationResult:
        """
        Validates a set of variables against stored expressions to check for inconsistencies.
        Returns validation results for each relevant expression.

        Parameters
        ----------
        variables : typing.Sequence[ValidationRequirement]

        paper_expressions : ExpressionProcessingResponse

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExpressionValidationResult
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import (
            AsyncAxiomatic,
            Expression,
            ExpressionProcessingResponse,
            Symbol,
            ValidationRequirement,
            ValidationResult,
        )

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document.expression.validate(
                variables=[
                    ValidationRequirement(
                        symbol=Symbol(
                            name="name",
                            wolfram_format="wolfram_format",
                            latex_representation="latex_representation",
                            dimension="dimension",
                            description="description",
                            type="scalar",
                            validations={
                                "key": ValidationResult(
                                    is_valid=True,
                                    message="message",
                                )
                            },
                        ),
                        value=1.1,
                    )
                ],
                paper_expressions=ExpressionProcessingResponse(
                    expressions=[
                        Expression(
                            name="name",
                            description="description",
                            original_format="original_format",
                            wolfram_expression="wolfram_expression",
                            symbols={
                                "key": Symbol(
                                    name="name",
                                    wolfram_format="wolfram_format",
                                    latex_representation="latex_representation",
                                    dimension="dimension",
                                    description="description",
                                    type="scalar",
                                    validations={
                                        "key": ValidationResult(
                                            is_valid=True,
                                            message="message",
                                        )
                                    },
                                )
                            },
                            narrative_assumptions=["narrative_assumptions"],
                            exp_validations={
                                "key": ValidationResult(
                                    is_valid=True,
                                    message="message",
                                )
                            },
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "document/expression/validate",
            method="POST",
            json={
                "variables": convert_and_respect_annotation_metadata(
                    object_=variables, annotation=typing.Sequence[ValidationRequirement], direction="write"
                ),
                "paper_expressions": convert_and_respect_annotation_metadata(
                    object_=paper_expressions, annotation=ExpressionProcessingResponse, direction="write"
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
                    ExpressionValidationResult,
                    parse_obj_as(
                        type_=ExpressionValidationResult,  # type: ignore
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

    async def process(
        self,
        *,
        markdown: str,
        images: typing.Optional[typing.Dict[str, str]] = OMIT,
        interline_equations: typing.Optional[typing.Sequence[str]] = OMIT,
        inline_equations: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExpressionProcessingResponse:
        """
        Process all expressions at once and return their annotation

        Parameters
        ----------
        markdown : str

        images : typing.Optional[typing.Dict[str, str]]

        interline_equations : typing.Optional[typing.Sequence[str]]

        inline_equations : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExpressionProcessingResponse
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document.expression.process(
                markdown="markdown",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "document/expression/process",
            method="POST",
            json={
                "markdown": markdown,
                "images": images,
                "interline_equations": interline_equations,
                "inline_equations": inline_equations,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExpressionProcessingResponse,
                    parse_obj_as(
                        type_=ExpressionProcessingResponse,  # type: ignore
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
