# Groupy App
## Group manages user groups in slack.

# To trigger this:
# curl -i -X POST -H "Content-Type: application/json" -d '{ "TeamId" : "1", "Users" : ["u1", "u2"], "GroupName" : "groupA" }' http://127.0.0.1:8000/slack/apps/groupy/create


#  KEYS for JSON

team_id_key = "TeamId"
message_id_key = "MessageId"
users_id = "Users"
group_name_key = "GroupName"

# FUNCTIONS

def create_group(values):
    return { "Text" : "Creating group " + values[group_name_key] + " for team " + values[team_id_key] + " with members " + str(values[users_id])}

def add_to_group(values):
    return { "Text" : "Adding to group " + values[group_name_key] + " for team " + values[team_id_key] + " the following members " + str(values[users_id])}

def remove_from_group(values):
    return { "Text" : "Removing from group " + values[group_name_key] + " for team " + values[team_id_key] + " the following members " + str(values[users_id])}

def list_members_in_group(values):
    return { "Text" : "Listing members in group " + values[group_name_key] + " for team " + values[team_id_key]}

def list_groups(values):
    return { "Text" : "Listing groups for team " + values[team_id_key]}

def delete_group(values):
    return { "Text" : "Deleting group " + values[group_name_key] + " for team " + values[team_id_key]}

# GATEWAY

commands = [
    { 
        "Name" : "create",
        "Function" : create_group,
        "RequiredKeys" : [team_id_key, group_name_key, users_id]
    },
    { 
        "Name" : "add-to",
        "Function" : add_to_group,
        "RequiredKeys" : [team_id_key, group_name_key, users_id]
    },
    { 
        "Name" : "remove-from",
        "Function" : remove_from_group,
        "RequiredKeys" : [team_id_key, group_name_key, users_id]
    },
    { 
        "Name" : "list-members",
        "Function" : list_members_in_group,
        "RequiredKeys" : [team_id_key, group_name_key]
    },
    { 
        "Name" : "list",
        "Function" : list_groups,
        "RequiredKeys" : [team_id_key]
    },
    { 
        "Name" : "delete",
        "Function" : delete_group,
        "RequiredKeys" : [team_id_key, group_name_key]
    }
]

def doGroup(command, args):
    for item in commands:
        if item["Name"] == command and checkNecessaryArgsExist(item["RequiredKeys"], args):
            return item["Function"](args) 
    return { "Text" : "Echoing command:" }

def checkNecessaryArgsExist(required_args, args):
    for required_arg in required_args:
        if required_arg not in args.keys():
            return False
    return True