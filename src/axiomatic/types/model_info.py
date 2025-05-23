# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .model_names import ModelNames
import typing
from .model_parameter_info import ModelParameterInfo
from .model_target_info import ModelTargetInfo
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ModelInfo(UniversalBaseModel):
    model_name: ModelNames
    parameters: typing.List[ModelParameterInfo]
    target_functions: typing.List[ModelTargetInfo]
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
