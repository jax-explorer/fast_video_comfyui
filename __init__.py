
import os
import sys
modules_path = os.path.join(os.path.dirname(__file__), "fast")
from .fast.utils import *
NODE_CLASS_MAPPINGS = {
    "Fast_Video_ComfyUI": FastImageListToImageBatch
}