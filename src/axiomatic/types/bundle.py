# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .bundle_settings_value import BundleSettingsValue
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class Bundle(UniversalBaseModel):
    links: typing.Dict[str, str]
    settings: typing.Optional[typing.Dict[str, typing.Optional[BundleSettingsValue]]] = None
    routing_strategy: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
