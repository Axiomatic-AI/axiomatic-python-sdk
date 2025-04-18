# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .extracted_points import ExtractedPoints
import typing
from .plot_info import PlotInfo
import pydantic
from .axes_info import AxesInfo
from .platform_data import PlatformData
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PlotParserOutput(UniversalBaseModel):
    """
    Represents the parsed output of a plot, including extracted points and metadata.
    """

    extracted_points: ExtractedPoints
    plot_info: typing.Optional[PlotInfo] = pydantic.Field(default=None)
    """
    Extracted information about the plot
    """

    axes_info: typing.Optional[AxesInfo] = pydantic.Field(default=None)
    """
    Important axes info
    """

    raw_ocr_data: typing.Optional[typing.List[typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Raw OCR data
    """

    platform_data: typing.Optional[PlatformData] = pydantic.Field(default=None)
    """
    Concise platform data
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
