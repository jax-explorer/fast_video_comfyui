
import torch
class FastImageListToImageBatch:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                        "images": ("IMAGE", ),
                      }
                }

    INPUT_IS_LIST = True

    RETURN_TYPES = ("IMAGE", )
    FUNCTION = "doit"

    CATEGORY = "FastVideo/fast_image_handle"

    def doit(self, images):
        if len(images) <= 1:
            return (images,)
        else:
            combined_image = torch.stack(images, dim=0)  # This stacks along a new first dimension
            combined_image = combined_image.view(-1, *images[0].shape[1:])  # Reshape to flatten the first two dimensions
            return (combined_image,)