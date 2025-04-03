from pydantic.dataclasses import dataclass

@dataclass
class uwu:
    a: str
    b: int

cutie = uwu("woah", 5)

print(tuple(cutie.__dict__.values()))