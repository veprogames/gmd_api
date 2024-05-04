from .level_object import LevelObject
from .color import ColorChannel
from .level_string import InnerLevelString
from typing import Self

class Level:
    def __init__(self, name: str = "") -> None:
        self.name: str = name
        self.inner_string: InnerLevelString = InnerLevelString()

    def add_object(self, obj: LevelObject) -> Self:
        self.inner_string.objects.append(obj)
        return self
    
    def add_color_channel(self, channel: ColorChannel) -> Self:
        self.inner_string.color_channels.append(channel)
        return self
    
    def inner(self) -> InnerLevelString:
        return self.inner_string

    def to_string(self) -> str:
        string: str = f"""<?xml version="1.0"?>
<plist version="1.0" gjver="2.0">
    <dict>
        <k>kCEK</k><i>4</i>
        <k>k2</k><s>{self.name}</s>
        <k>k4</k><s>{self.inner_string.to_string()}</s>
        <k>k21</k><i>2</i>
        <k>k16</k><i>1</i>
        <k>k50</k><i>40</i>
    </dict>
</plist>"""
        return string \
            .replace("\n", "") \
            .replace("\t", "")
    
    def save(self, to_file: str) -> None:
        with open(to_file, "w") as f:
            f.write(self.to_string())