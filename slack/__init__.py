from .apps import get_app_data

def performSlackAction(appName, command, args):
    for app in get_app_data():
        if appName == app["Name"]:
            return app["Command"](command, args)
    return { "Text" : "No such app" }