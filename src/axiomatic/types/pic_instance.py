# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .pic_instance_info_value import PicInstanceInfoValue
from .pic_instance_settings_value import PicInstanceSettingsValue
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PicInstance(UniversalBaseModel):
    """
    Class to represent a PIC instance / component in the Netlist
    """

    component: str
    info: typing.Optional[typing.Dict[str, PicInstanceInfoValue]] = None
    settings: typing.Optional[typing.Dict[str, typing.Optional[PicInstanceSettingsValue]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
