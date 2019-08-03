from pymongo import MongoClient
from .constants import db_team_id_key, db_groups_key, db_group_name_key, db_members_key

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

mongoURI = 'mongodb://raghav-meta-api-user:XiBHv3tXc1v2eQQ7@raghav-atlas-cluster0-shard-00-01-osbeo.mongodb.net:27017,raghav-atlas-cluster0-shard-00-00-osbeo.mongodb.net:27017,raghav-atlas-cluster0-shard-00-02-osbeo.mongodb.net:27017'
dbName = 'meta-api'
collectionName = 'teams'

template_doc = {
    db_team_id_key : "",
    db_groups_key : [
        {
            db_group_name_key : "",
            db_members_key :  []
        }
    ]
}

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
    return result

def update_team_add_new_group(team_id, group_name, members, collection):
    # method called when team exists, so it team should not be None
    team = collection.find_one({ db_team_id_key : team_id})
    
    for group in team[db_groups_key]:
        if group[db_group_name_key] == group_name:
            return {"Text" : group_name + " already exists as a group in this workspace" }
    
    result = teams.update_one(
        { db_team_id_key : team_id} , 
        {
            '$push' : { 
                db_groups_key : { 
                    db_group_name_key : group_name, 
                    db_members_key : members }}})

    return result

def update_team_update_group(team_id, group_name, members, collection):
    # method called when team exists, so it team should not be None
    team = collection.find_one({ db_team_id_key : team_id})
    
    for group in team[db_groups_key]:
        if group[db_group_name_key] == group_name:
            return {"Text" : group_name + " already exists as a group in this workspace" }
    
    result = teams.update_one(
        { db_team_id_key : team_id} , 
        {
            '$push' : { 
                db_groups_key : { 
                    db_group_name_key : group_name, 
                    db_members_key : members }}})

    return result

def create_new_group(team_id, group_name, members):
    collection = get_collection()
    if collection.count() == 0:
        return create_new_team_document(team_id, group_name, members, collection)
    else:
        return update_team_add_new_group(team_id, group_name, members, collection)

