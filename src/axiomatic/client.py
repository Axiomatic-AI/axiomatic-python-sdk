# This file was auto-generated by Fern from our API Definition.

import typing
from .environment import AxiomaticEnvironment
import httpx
from .core.client_wrapper import SyncClientWrapper
from .requirements.client import RequirementsClient
from .pic.client import PicClient
from .lean.client import LeanClient
from .experimental.client import ExperimentalClient
from .formalization.client import FormalizationClient
from .generic.client import GenericClient
from .core.request_options import RequestOptions
from .core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper
from .requirements.client import AsyncRequirementsClient
from .pic.client import AsyncPicClient
from .lean.client import AsyncLeanClient
from .experimental.client import AsyncExperimentalClient
from .formalization.client import AsyncFormalizationClient
from .generic.client import AsyncGenericClient


class Axiomatic:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : AxiomaticEnvironment
        The environment to use for requests from the client. from .environment import AxiomaticEnvironment



        Defaults to AxiomaticEnvironment.DEFAULT



    api_key : str
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from axiomatic import Axiomatic

    client = Axiomatic(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: AxiomaticEnvironment = AxiomaticEnvironment.DEFAULT,
        api_key: str,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.requirements = RequirementsClient(client_wrapper=self._client_wrapper)
        self.pic = PicClient(client_wrapper=self._client_wrapper)
        self.lean = LeanClient(client_wrapper=self._client_wrapper)
        self.experimental = ExperimentalClient(client_wrapper=self._client_wrapper)
        self.formalization = FormalizationClient(client_wrapper=self._client_wrapper)
        self.generic = GenericClient(client_wrapper=self._client_wrapper)

    def health_check_health_check_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
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
        client.health_check_health_check_get()
        """
        _response = self._client_wrapper.httpx_client.request(
            "health_check",
            method="GET",
            request_options=request_options,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAxiomatic:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : AxiomaticEnvironment
        The environment to use for requests from the client. from .environment import AxiomaticEnvironment



        Defaults to AxiomaticEnvironment.DEFAULT



    api_key : str
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from axiomatic import AsyncAxiomatic

    client = AsyncAxiomatic(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: AxiomaticEnvironment = AxiomaticEnvironment.DEFAULT,
        api_key: str,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.requirements = AsyncRequirementsClient(client_wrapper=self._client_wrapper)
        self.pic = AsyncPicClient(client_wrapper=self._client_wrapper)
        self.lean = AsyncLeanClient(client_wrapper=self._client_wrapper)
        self.experimental = AsyncExperimentalClient(client_wrapper=self._client_wrapper)
        self.formalization = AsyncFormalizationClient(client_wrapper=self._client_wrapper)
        self.generic = AsyncGenericClient(client_wrapper=self._client_wrapper)

    async def health_check_health_check_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
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
            await client.health_check_health_check_get()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "health_check",
            method="GET",
            request_options=request_options,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: AxiomaticEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
