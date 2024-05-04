from typing import Self
from .keys.colors import *
from .keys.color_channels import *

class ColorChannel:
    def __init__(self, id: int) -> None:
        self.properties: dict[int, any] = {}

        self.set(ID, id)
        self.set(RED, 0)
        self.set(GREEN, 0)
        self.set(BLUE, 0)

        # unknown for now
        self.set(11, 255)
        self.set(12, 255)
        self.set(13, 255)

        self.set(4, -1)

        self.set(7, 1)
        self.set(8, 1)
        self.set(15, 1)
        self.set(18, 1)
    
    def set(self, key: int, value: any) -> Self:
        self.properties[key] = value
        return self

    def set_rgb(self, r: int, g: int, b: int) -> Self:
        return self.set(RED, r) \
            .set(GREEN, g) \
            .set(BLUE, b)
    
    def to_string(self) -> str:
        return "_".join([f"{k}_{v}" for k, v in self.properties.items()]) + "|"

def get_default_colors() -> list[ColorChannel]:
    return [
        ColorChannel(CHANNEL_BG).set_rgb(255, 255, 255),
        ColorChannel(CHANNEL_G1).set_rgb(0, 0, 0),
        ColorChannel(CHANNEL_G2).set_rgb(0, 0, 0),
        ColorChannel(CHANNEL_MG1).set_rgb(0, 0, 0),
        ColorChannel(CHANNEL_MG2).set_rgb(0, 0, 0),
        ColorChannel(CHANNEL_OBJ).set_rgb(200, 200, 200),

        ColorChannel(CHANNEL_P1).set_rgb(255, 255, 255),
        ColorChannel(CHANNEL_P2).set_rgb(255, 255, 255),
    ]

def make_hsv_string(h: int, s: float, v: float) -> str:
    return f"{h}a{s}a{v}a0a0"