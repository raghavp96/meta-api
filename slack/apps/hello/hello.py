## Simple Hello App

# To trigger this:
# curl -i -X POST -H "Content-Type: application/json" -d '{ "Team" : "1", "MessageId" : "123A" }' http://127.0.0.1:8000/slack/apps/hello/fakeCommand


def doHello(command, args): 
    return { "Text" : "Echoing command: '" + command + "', args: '" + str(args) + "'" }