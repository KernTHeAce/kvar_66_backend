from dataclasses import dataclass
import json
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class OutputJSON:
    Ivan_girl_counter: int = 0
    Anton_girl_counter: int = 0
    alko_days: int = 0
    no_alko_days: int = 0
