from enum import Enum


class Weather(Enum):
    SUNNY = "sunny"
    RAINY = "rainy"
    CLOUDY = "cloudy"
    WINDY = "windy"


class Feeling(Enum):
    HAPPY = "happy"
    GOOD = "good"
    SOSO = "so_so"
    SAD = "sad"
    ANGRY = "angry"


class Gender(Enum):
    FEMALE = "female"
    MALE = "male"
