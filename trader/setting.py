"""
Global setting of VN Trader.
"""

from logging import CRITICAL

from .utility import load_json

SETTINGS = {
    "font.family": "Arial",
    "font.size": 12,

    "log.active": True,
    "log.level": CRITICAL,
    "log.console": True,
    "log.file": True,

    "email.server": "smtp.qq.com",
    "email.port": 465,
    "email.username": "",
    "email.password": "",
    "email.sender": "",
    "email.receiver": "",

    "rqdata.username": "license",
    "rqdata.password": "hNquASLMnsj6XvN7244jRy9wAiGGpGKcS-mrlPpND9TOUajZD61S2KjTfEEv22szfARmC7Ab4sOWcHGBlc8sJSKjQUxgxGm_uxYmwDmszQoGsr3qrdC1fgvDiTtBtuy3KtdngdyY6kOrkXOnu0hi5-de7Avdfl_riZUc_Yk2DAU=N78cYFYpV95cAStJFo0qcsV6fHuLFainVSspsleIUzgT6gLrld0cV6RU2MsLJX0M6eHKjjkAxfL4ypilQvowHwKUBybdi94hhGOfZ_GmV_GMEDitnM40HoVCYErA4fm_7melaRGHrQBUbcqQQZ2gu3rtmZWQgcIUTTFc6QI-tCM=",

    "database.driver": "mongodb",  # see database.Driver
    "database.database": "vnpy",#"database.db",  # for sqlite, use this as filepath
    "database.host": "localhost",
    "database.port": 27017,#3306,
    "database.user": "",#"root",
    "database.password": "",
    "database.authentication_source": "admin",  # for mongodb
}

# Load global setting from json file.
SETTING_FILENAME = "vt_setting.json"
SETTINGS.update(load_json(SETTING_FILENAME))


def get_settings(prefix: str = ""):
    prefix_length = len(prefix)
    return {k[prefix_length:]: v for k, v in SETTINGS.items() if k.startswith(prefix)}