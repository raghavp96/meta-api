from .constants import json_group_name_key, json_team_id_key, json_message_id_key, json_users_id_key
from .dao import create_new_group, update_group_members, list_team_groups, list_team_group_members, delete_team_group

# Groupy App
## Group manages user groups in slack.

# To trigger this:
# curl -i -X POST -H "Content-Type: application/json" -d '{ "TeamId" : "1", "Users" : ["u1", "u2"], "GroupName" : "groupA" }' http://127.0.0.1:8000/slack/apps/groupy/create

# APP FUNCTIONS

def create_group(values): 
    if create_new_group(values[json_team_id_key], values[json_group_name_key], values[json_users_id_key]):
        return { "response_type": "in_channel", "text" : "Created group " + values[json_group_name_key] + " for team " + values[json_team_id_key] + " with members " + str(values[json_users_id_key])}
    else:
        return { "text" : "Could not create group " + values[json_group_name_key] + " for team " + values[json_team_id_key] + " with members " + str(values[json_users_id_key])}


def add_to_group(values):
    if update_group_members(values[json_team_id_key], values[json_group_name_key], values[json_users_id_key], method="add"):
        return { "response_type": "in_channel", "text" : "Added to group " + values[json_group_name_key] + " for team " + values[json_team_id_key] + " the following members " + str(values[json_users_id_key])}
    else:
        return { "text" : "Could not add to group " + values[json_group_name_key] + " for team " + values[json_team_id_key] + " the following members " + str(values[json_users_id_key])}            


def remove_from_group(values):
    if update_group_members(values[json_team_id_key], values[json_group_name_key], values[json_users_id_key], method="remove"):
        return { "response_type": "in_channel", "text" : "Removed from group " + values[json_group_name_key] + " for team " + values[json_team_id_key] + " the following members " + str(values[json_users_id_key])}
    else:
        return { "text" : "Could not remove from group " + values[json_group_name_key] + " for team " + values[json_team_id_key] + " the following members " + str(values[json_users_id_key])}            


def list_members_in_group(values):
    return { "response_type": "in_channel", "text" : str(list_team_group_members(values[json_team_id_key], values[json_group_name_key])) }


def list_groups(values):
    return { "response_type": "in_channel", "text" : str(list_team_groups(values[json_team_id_key])) }


def delete_group(values):
    if delete_team_group(values[json_team_id_key], values[json_group_name_key]):
        return { "response_type": "in_channel", "text" : "Deleted group " + values[json_group_name_key] + " for team " + values[json_team_id_key]}
    else:
        return { "text" : "Could not delete group " + values[json_group_name_key] + " for team " + values[json_team_id_key]}


def notify_members(values):
    group_members = list_members_in_group({ json_team_id_key : values[json_team_id_key], json_group_name_key : values[json_group_name_key]})["text"]

    return {"response_type": "in_channel", "text" : "Tagging " + group_members}

# GATEWAY

slash_commands = [
    { 
        "Name" : "create",
        "Function" : create_group,
        "RequiredKeys" : [json_team_id_key, json_group_name_key, json_users_id_key]
    },
    { 
        "Name" : "add-to",
        "Function" : add_to_group,
        "RequiredKeys" : [json_team_id_key, json_group_name_key, json_users_id_key]
    },
    { 
        "Name" : "remove-from",
        "Function" : remove_from_group,
        "RequiredKeys" : [json_team_id_key, json_group_name_key, json_users_id_key]
    },
    { 
        "Name" : "list-members",
        "Function" : list_members_in_group,
        "RequiredKeys" : [json_team_id_key, json_group_name_key]
    },
    { 
        "Name" : "list",
        "Function" : list_groups,
        "RequiredKeys" : [json_team_id_key]
    },
    { 
        "Name" : "delete",
        "Function" : delete_group,
        "RequiredKeys" : [json_team_id_key, json_group_name_key]
    },
    {
        "Name" : "tag-group",
        "Function" : notify_members,
        "RequiredKeys" : [json_team_id_key, json_group_name_key]
    }
]


def __parseSlashCommandRequestData(data):
    relevantArgs = {}
    relevantArgs[json_team_id_key] = data["team_id"]
    text = data["text"].split()

    if len(text) == 1:
        relevantArgs[json_group_name_key] = text[0]
    
    elif len(text) > 1:
        relevantArgs[json_group_name_key] = text[0]
        relevantArgs[json_users_id_key] = text[1:]

    return relevantArgs


def doGroupSlashCommand(command, args):
    parsedArgs = __parseSlashCommandRequestData(args)
    # print(parsedArgs)
    for item in slash_commands:
        if item["Name"] == command and checkNecessaryArgsExist(item["RequiredKeys"], parsedArgs):
            return item["Function"](parsedArgs) 
    return { "text" : "Valid args not passed to command" }
    

def checkNecessaryArgsExist(required_args, args):
    for required_arg in required_args:
        if required_arg not in args.keys():
            return False
    return True