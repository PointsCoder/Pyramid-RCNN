from .detector3d_template import Detector3DTemplate
from .pyramid_rcnn_p import PyramidPoint
from .pyramid_rcnn_v import PyramidVoxel
from .pyramid_rcnn_pv import PyramidPointVoxel, PyramidPointVoxelPlus

__all__ = {
    'Detector3DTemplate': Detector3DTemplate,
    'PyramidPoint': PyramidPoint,
    'PyramidVoxel': PyramidVoxel,
    'PyramidPointVoxel': PyramidPointVoxel,
    'PyramidPointVoxelPlus': PyramidPointVoxelPlus,
}

def build_detector(model_cfg, num_class, dataset):
    model = __all__[model_cfg.NAME](
        model_cfg=model_cfg, num_class=num_class, dataset=dataset
    )

    return model