from enum import Enum


class RegEx(Enum):
    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,50}$', [
            'Password must contain 1 number (0-9)',
            'Password must 1 uppercase letters',
            'Password must 1 lowercase letters',
            'Password must1 non-alpha numeric number',
            'Password is 8-50 characters with no space'
        ])
    NAME = (
        r'^[a-zA-Z]{2,100}$',
        'only letters min 2 max 100 char'
    )
    PHONE = (
        r'^0[9567]{1}\d{8}$',
        'Invalid phone number'
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.msg = msg
        self.pattern = pattern