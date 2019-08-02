from .hello import doHello
from .groupy import doGroup

apps = [
    {
        "Name" : "hello",
        "Command" : hello.doHello
    },
    {
        "Name" : "groupy",
        "Command" : groupy.doGroup
    }
]

def get_app_data():
    return apps