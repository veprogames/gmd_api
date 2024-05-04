from .level_object import LevelObject
from .color import ColorChannel, get_default_colors
from .keys.inner_level_string import *
from typing import Self
import gzip
from base64 import urlsafe_b64encode

class InnerLevelString:
    def __init__(self) -> None:
        self.objects: list[LevelObject] = []
        self.color_channels: list[ColorChannel] = get_default_colors()
        self.properties: dict[str, any] = {}
    
    def set(self, key: str, value: any) -> Self:
        self.properties[key] = value
        return self
    
    def set_platformer(self, to: bool = True) -> Self:
        return self.set(IS_PLATFORMER, to)
    
    def set_background_id(self, id: int) -> Self:
        return self.set(BG_ID, id)
    
    def set_ground_id(self, id: int) -> Self:
        return self.set(GROUND_ID, id)
    
    def set_middleground_id(self, id: int) -> Self:
        return self.set(MG_ID, id)

    def to_raw_string(self) -> str:
        colors: str = "".join([channel.to_string() for channel in self.color_channels])
        keys: str = ",".join([f"{k},{v}" for k, v in self.properties.items()])
        prelude: str = f"kS38,{colors},{keys};"
        objects: str = "".join([obj.to_string() for obj in self.objects])

        return f"{prelude}{objects}"
    
    def to_string(self) -> str:
        raw_level_string = bytes(self.to_raw_string(), encoding="utf-8")
        return urlsafe_b64encode(gzip.compress(raw_level_string)).decode("utf-8")