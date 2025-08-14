from enum import Enum

class RegexEnum(Enum):
    NAME =(
        r'^[A-Z][a-z]{,19}$',
        'Only alha ch is allowed'
    )
    def __init__(self, pattern, msg:str):
        self.pattern = pattern
        self.msg = msg
