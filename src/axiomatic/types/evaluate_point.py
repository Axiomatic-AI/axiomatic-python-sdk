# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class EvaluatePoint(UniversalBaseModel):
    value_x: float
    percentage_coord_x: float
    value_y: float
    percentage_coord_y: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
