from .nodes.instructpg_node import InstructPGStableDiffusionPipeline

NODE_CLASS_MAPPINGS = {
    "InstructPG": InstructPGStableDiffusionPipeline,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "InstructPG": "InstructPG - editing images with text prompt",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']