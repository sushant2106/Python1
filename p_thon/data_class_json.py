from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Person:
    name: str


person=Person("Ram..")

#encoding json
print(person.to_json())



# Decoding from JSON
print(Person.from_json('{"name": "lidatong"}'))