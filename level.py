from .level_object import LevelObject
from .color import get_default_colors, ColorChannel
from typing import Self
import gzip
from base64 import urlsafe_b64encode

class Level:
    def __init__(self, author: str = "", name: str = "") -> None:
        self.author: str = author
        self.name: str = name
        self.objects: list[LevelObject] = []
        self.color_channels: list[ColorChannel] = get_default_colors()

    def add_object(self, obj: LevelObject) -> Self:
        self.objects.append(obj)
        return self
    
    def add_color_channel(self, channel: ColorChannel) -> Self:
        self.color_channels.append(channel)
        return self
    
    def get_level_string(self) -> str:
        colors: str = "".join([channel.to_string() for channel in self.color_channels])
        prelude: str = f"kS38,{colors},kA13,0,kA15,0,kA16,0,kA14,,kA6,0,kA7,0,kA25,0,kA17,0,kA18,0,kS39,0,kA2,0,kA3,0,kA8,0,kA4,0,kA9,0,kA10,0,kA22,0,kA23,0,kA24,0,kA27,1,kA40,1,kA41,1,kA42,1,kA28,0,kA29,0,kA31,1,kA32,1,kA36,0,kA43,0,kA44,0,kA45,1,kA33,1,kA34,1,kA35,0,kA37,1,kA38,1,kA39,1,kA19,0,kA26,0,kA20,0,kA21,0,kA11,0;"
        objects: str = "".join([obj.to_string() for obj in self.objects])

        raw_level_string = bytes(f"{prelude}{objects}", encoding="utf-8")
        return urlsafe_b64encode(gzip.compress(raw_level_string)).decode("utf-8")

    def to_string(self) -> str:
        string: str = f"""<?xml version="1.0"?>
<plist version="1.0" gjver="2.0">
    <dict>
        <k>kCEK</k><i>4</i>
        <k>k2</k><s>{self.name}</s>
        <k>k4</k><s>{self.get_level_string()}</s>
        <k>k5</k><s>{self.author}</s>
        <k>k101</k><s>0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0</s>
        <k>k13</k><t />
        <k>k21</k><i>2</i>
        <k>k16</k><i>1</i>
        <k>k80</k><i>7</i>
        <k>k50</k><i>40</i>
        <k>k47</k><t />
        <k>k48</k><i>1</i>
        <k>kI1</k><r>183.721</r>
        <k>kI2</k><r>82.2666</r>
        <k>kI3</k><r>0.7</r>
        <k>kI6</k>
        <d>
            <k>0</k><s>0</s>
            <k>1</k><s>0</s>
            <k>2</k><s>0</s>
            <k>3</k><s>0</s>
            <k>4</k><s>0</s>
            <k>5</k><s>0</s>
            <k>6</k><s>0</s>
            <k>7</k><s>0</s>
            <k>8</k><s>0</s>
            <k>9</k><s>0</s>
            <k>10</k><s>0</s>
            <k>11</k><s>0</s>
            <k>12</k><s>0</s>
            <k>13</k><s>0</s>
        </d>
    </dict>
</plist>"""
        return string \
            .replace("\n", "") \
            .replace("\t", "")
    
    def save(self, to_file: str) -> None:
        with open(to_file, "w") as f:
            f.write(self.to_string())