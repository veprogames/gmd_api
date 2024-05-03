from typing import Self

K_ID = 1
K_POS_X = 2
K_POS_Y = 3
K_ROTATION_DEGREES = 6

K_GROUPS = 57

K_SCALE_X = 128
K_SCALE_Y = 129

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
    
    def positioned_at(self, x: float, y: float) -> Self:
        return self \
            .set(K_POS_X, x) \
            .set(K_POS_Y, y)

    def rotated_to(self, degrees: float) -> Self:
        return self.set(K_ROTATION_DEGREES, degrees)

    def scaled_to(self, x: float, y: float) -> Self:
        return self \
            .set(K_SCALE_X, x) \
            .set(K_SCALE_Y, y)

    def to_string(self) -> str:
        return ",".join([f"{k},{v}" for k, v in sorted(self.properties.items())]) + ";"