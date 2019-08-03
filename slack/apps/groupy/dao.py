from pymongo import MongoClient
from .constants import db_name, db_user_profile, db_user_pwd, db_hosts, db_team_id_key, db_groups_key, db_group_name_key, db_members_key

## DAO - store the user group info in Mongo Atlas (My team 205 cluster )

#  An example Document in Teams COllection
# [
#     {
#         'TeamId' : ...,
#         'Groups' : [
#             {
#                 'GroupName' : ...,
#                 'Members' : [ "" , "" ]
#             },
#             ...
#         ]
#     }
# ]


if db_user_profile is not None and db_user_pwd is not None and db_hosts is not None:
    mongoURI = 'mongodb://' + db_user_profile + ':' + db_user_pwd + '@' + db_hosts + '/test?ssl=true&replicaSet=raghav-atlas-cluster0-shard-0&authSource=admin&w=majority'
else:
    mongoURI = 'mongodb://localhost:27017/'

dbName = db_name
collectionName = 'teams'

def get_collection():
    client = MongoClient(mongoURI)
    db = client[dbName]
    return db[collectionName]


def create_new_team_document(team_id, group_name, members, collection):
    result = collection.insert_one(
            {
                db_team_id_key : team_id,
                db_groups_key : [
                    {
                        db_group_name_key : group_name,
                        db_members_key :  members
                    }
                ]
            }
        )
    return result.acknowledged


def update_team_add_new_group(team_id, group_name, members, collection):
    # method called when team exists, so it team should not be None
    team = collection.find_one({ db_team_id_key : team_id})
    
    for group in team[db_groups_key]:
        if group[db_group_name_key] == group_name:
            return False
    
    result = collection.update_one(
        { db_team_id_key : team_id} , 
        {
            '$push' : { 
                db_groups_key : { 
                    db_group_name_key : group_name, 
                    db_members_key : members }}})

    return result.acknowledged


def update_team_update_group_members(team_id, group_name, members, collection, method="add"):
    # method called when team exists, so it team should not be None
    team = collection.find_one({ db_team_id_key : team_id})
    
    for group in team[db_groups_key]:
        if group[db_group_name_key] == group_name:
            members_in_group = group[db_members_key]
            old_members = group[db_members_key]

            if method == "remove":
                for member in members:
                    if member in members_in_group:
                        members_in_group.remove(member)
                    else:
                        print(member + " was not in group")
            else:
                for member in members:
                    if member not in members_in_group:
                        members_in_group.append(member)
                    else:
                        print(member + " was already in group")

            result = collection.update_one(
                { db_team_id_key : team_id } , 
                {
                    '$pull' : { 
                        db_groups_key : { 
                            db_group_name_key : group_name,
                            db_members_key : old_members }}})

            if result.acknowledged:
                result = collection.update_one(
                    { db_team_id_key : team_id} , 
                    {
                        '$push' : { 
                            db_groups_key : { 
                                db_group_name_key : group_name, 
                                db_members_key : members_in_group }}})
                return result.acknowledged
            else:
                return False


    #  No such group existed, so nothing was deleted
    print("No such group")
    return False


def create_new_group(team_id, group_name, members):
    collection = get_collection()
    if collection.count() == 0:
        return create_new_team_document(team_id, group_name, members, collection)
    else:
        if collection.find_one({ db_team_id_key : team_id}) is None:
            return create_new_team_document(team_id, group_name, members, collection)
        else:
            return update_team_add_new_group(team_id, group_name, members, collection)


def update_group_members(team_id, group_name, members, method):
    collection = get_collection()
    if collection.count() == 0:
        return False
    else:
        return update_team_update_group_members(team_id, group_name, members, collection, method)