from .hello import doHello
from .groupy import doGroup

apps = [
    {
        "Name" : "hello",
        "Command" : doHello
    },
    {
        "Name" : "groupy",
        "Command" : doGroup
    }
]

def get_app_data():
    return apps