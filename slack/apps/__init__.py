from .hello import doHello

apps = [
    {
        "Name" : "hello",
        "Command" : hello.doHello
    }
]

def get_app_data():
    return apps