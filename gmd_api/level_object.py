from typing import Self, Iterable
from .keys.objects import *
from .color import make_hsv_string

class LevelObject:
    def __init__(self, id: int) -> None:
        self.properties: dict[int, any] = {}
        self.properties[ID] = id
        self.properties[155] = 1 # ???
    
    def get(self, key: int) -> any:
        return self.properties[key] if key in self.properties else None

    def set(self, key: int, value: any) -> Self:
        self.properties[key] = value
        return self
    
    def move_to(self, x: float, y: float) -> Self:
        return self \
            .set(POS_X, x) \
            .set(POS_Y, y)

    def rotate_to(self, degrees: float) -> Self:
        return self.set(ROTATION_DEGREES, degrees)

    def scale_to(self, x: float, y: float) -> Self:
        return self \
            .set(SCALE_X, x) \
            .set(SCALE_Y, y)

    def set_base_color(self, channel_id: int) -> Self:
        return self.set(COLOR_CHANNEL_BASE, channel_id)
    
    def set_detail_color(self, channel_id: int) -> Self:
        return self.set(COLOR_CHANNEL_DETAIL, channel_id)

    def set_color_channels(self, base_id: int, detail_id: int) -> Self:
        return self.set_base_color(base_id) \
            .set_detail_color(detail_id)
    
    def set_base_hsv(self, h: int, s: float, v: float) -> Self:
        return self.set(HSV_BASE_ENABLED, 1) \
            .set(HSV_BASE, make_hsv_string(h, s, v))
    
    def disable_base_hsv(self) -> Self:
        return self.set(HSV_BASE_ENABLED, 0)

    def set_detail_hsv(self, h: int, s: float, v: float) -> Self:
        return self.set(HSV_DETAIL_ENABLED, 1) \
            .set(HSV_DETAIL, make_hsv_string(h, s, v))
    
    def disable_detail_hsv(self) -> Self:
        return self.set(HSV_DETAIL, 0)

    def set_groups(self, groups: Iterable[int]) -> Self:
        groups_as_str = [str(gid) for gid in groups]
        return self.set(GROUPS, ".".join(groups_as_str))

    def to_string(self) -> str:
        return ",".join([f"{k},{v}" for k, v in sorted(self.properties.items())]) + ";"