from typing import Self

K_ID = 1
K_POS_X = 2
K_POS_Y = 3

class LevelObject:
    def __init__(self, id: int) -> None:
        self.properties: dict[int, any] = {}
        self.properties[K_ID] = id
        self.properties[155] = 1 # ???
    
    def set(self, key: int, value: any) -> Self:
        self.properties[key] = value
        return self
    
    def set_pos(self, x: float, y: float) -> Self:
        return self \
            .set(K_POS_X, x) \
            .set(K_POS_Y, y)

    def to_string(self) -> str:
        return ",".join([f"{k},{v}" for k, v in sorted(self.properties.items())]) + ";"