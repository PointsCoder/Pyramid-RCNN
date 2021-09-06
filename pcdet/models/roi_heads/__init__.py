from .roi_head_template import RoIHeadTemplate
from .pyramid_head import PyramidRoIHead, PyramidRoIHeadV2

__all__ = {
    'RoIHeadTemplate': RoIHeadTemplate,
    'PyramidRoIHead': PyramidRoIHead,
    'PyramidRoIHeadV2': PyramidRoIHeadV2
}
