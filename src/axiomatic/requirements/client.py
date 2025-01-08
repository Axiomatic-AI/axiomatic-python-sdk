# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .data_files.client import DataFilesClient
from ..types.requirement_body import RequirementBody
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper
from .data_files.client import AsyncDataFilesClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RequirementsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.data_files = DataFilesClient(client_wrapper=self._client_wrapper)

    def check(
        self, *, request: typing.Sequence[RequirementBody], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
        request : typing.Sequence[RequirementBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic, RequirementBody

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.requirements.check(
            request=[
                RequirementBody(
                    latex_symbol="latex_symbol",
                    requirement_name="requirement_name",
                    tolerance=1.1,
                    value=1.1,
                    units="units",
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "requirements/check_requirements",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[RequirementBody], direction="write"
            ),
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

    def add_equation(
        self, *, equation_id: str, latex_formula: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Add a new equation to the database

        Parameters
        ----------
        equation_id : str

        latex_formula : str

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
        client.requirements.add_equation(
            equation_id="equation_id",
            latex_formula="latex_formula",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "requirements/add_equation",
            method="POST",
            json={
                "equation_id": equation_id,
                "latex_formula": latex_formula,
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

    def add_variable(
        self, *, latex_name: str, name: str, symbol: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Add new variable to database

        Parameters
        ----------
        latex_name : str

        name : str

        symbol : str

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
        client.requirements.add_variable(
            latex_name="latex_name",
            name="name",
            symbol="symbol",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "requirements/add_variable",
            method="POST",
            json={
                "latex_name": latex_name,
                "name": name,
                "symbol": symbol,
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


class AsyncRequirementsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.data_files = AsyncDataFilesClient(client_wrapper=self._client_wrapper)

    async def check(
        self, *, request: typing.Sequence[RequirementBody], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
        request : typing.Sequence[RequirementBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic, RequirementBody

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.requirements.check(
                request=[
                    RequirementBody(
                        latex_symbol="latex_symbol",
                        requirement_name="requirement_name",
                        tolerance=1.1,
                        value=1.1,
                        units="units",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "requirements/check_requirements",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[RequirementBody], direction="write"
            ),
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

    async def add_equation(
        self, *, equation_id: str, latex_formula: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Add a new equation to the database

        Parameters
        ----------
        equation_id : str

        latex_formula : str

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
            await client.requirements.add_equation(
                equation_id="equation_id",
                latex_formula="latex_formula",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "requirements/add_equation",
            method="POST",
            json={
                "equation_id": equation_id,
                "latex_formula": latex_formula,
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

    async def add_variable(
        self, *, latex_name: str, name: str, symbol: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Add new variable to database

        Parameters
        ----------
        latex_name : str

        name : str

        symbol : str

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
            await client.requirements.add_variable(
                latex_name="latex_name",
                name="name",
                symbol="symbol",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "requirements/add_variable",
            method="POST",
            json={
                "latex_name": latex_name,
                "name": name,
                "symbol": symbol,
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
