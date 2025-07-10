import enum

class Check(enum.Enum):
    sun=1
    mon=2



print(Check.sun._value_)