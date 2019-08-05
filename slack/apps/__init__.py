from .hello import doHello
from .groupy import doGroupSlashCommand

apps = [
    {
        "Name" : "hello",
        "Command" : doHello
    },
    {
        "Name" : "groupy",
        "Command" : doGroupSlashCommand
    }
]

def get_app_data():
    return apps