from typing import Self
from .keys import *

class LevelObject:
    def __init__(self, id: int) -> None:
        self.properties: dict[int, any] = {}
        self.properties[K_ID] = id
        self.properties[155] = 1 # ???
    
    def get(self, key: int) -> any:
        return self.properties[key] if key in self.properties else None

    def set(self, key: int, value: any) -> Self:
        self.properties[key] = value
        return self
    
    def move_to(self, x: float, y: float) -> Self:
        return self \
            .set(K_POS_X, x) \
            .set(K_POS_Y, y)

    def rotate_to(self, degrees: float) -> Self:
        return self.set(K_ROTATION_DEGREES, degrees)

    def scale_to(self, x: float, y: float) -> Self:
        return self \
            .set(K_SCALE_X, x) \
            .set(K_SCALE_Y, y)

    def to_string(self) -> str:
        return ",".join([f"{k},{v}" for k, v in sorted(self.properties.items())]) + ";"