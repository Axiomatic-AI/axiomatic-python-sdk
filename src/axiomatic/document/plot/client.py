# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ... import core
from ...core.request_options import RequestOptions
from ...types.color_to_points import ColorToPoints
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PlotClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def points(
        self,
        *,
        plot_img: core.File,
        method: typing.Optional[int] = None,
        plot_info: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ColorToPoints:
        """
        Extracts points from plots

        Parameters
        ----------
        plot_img : core.File
            See core.File for more documentation

        method : typing.Optional[int]
            Can specify a specific method to extract points

        plot_info : typing.Optional[str]
            Can add specific plot info

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ColorToPoints
            Successful Response

        Examples
        --------
        from axiomatic import Axiomatic

        client = Axiomatic(
            api_key="YOUR_API_KEY",
        )
        client.document.plot.points()
        """
        _response = self._client_wrapper.httpx_client.request(
            "document/plot/points",
            method="POST",
            params={
                "method": method,
                "plot_info": plot_info,
            },
            data={},
            files={
                "plot_img": plot_img,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ColorToPoints,
                    parse_obj_as(
                        type_=ColorToPoints,  # type: ignore
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


class AsyncPlotClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def points(
        self,
        *,
        plot_img: core.File,
        method: typing.Optional[int] = None,
        plot_info: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ColorToPoints:
        """
        Extracts points from plots

        Parameters
        ----------
        plot_img : core.File
            See core.File for more documentation

        method : typing.Optional[int]
            Can specify a specific method to extract points

        plot_info : typing.Optional[str]
            Can add specific plot info

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ColorToPoints
            Successful Response

        Examples
        --------
        import asyncio

        from axiomatic import AsyncAxiomatic

        client = AsyncAxiomatic(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document.plot.points()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "document/plot/points",
            method="POST",
            params={
                "method": method,
                "plot_info": plot_info,
            },
            data={},
            files={
                "plot_img": plot_img,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ColorToPoints,
                    parse_obj_as(
                        type_=ColorToPoints,  # type: ignore
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
