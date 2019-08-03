from pymongo import MongoClient

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
    'TeamId' : "",
    'Groups' : [
        {
            'GroupName' : "",
            'Members' :  []
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
                'TeamId' : team_id,
                'Groups' : [
                    {
                        'GroupName' : group_name,
                        'Members' :  members
                    }
                ]
            }
        )
    return result

def update_team_add_new_group(team_id, group_name, members, collection):
    # method called when team exists, so it team should not be None
    team = collection.find_one({ 'TeamId' : team_id})
    
    for group in team['Groups']:
        if group['GroupName'] == group_name:
            return {"Text" : group_name + " already exists as a group in this workspace" }
    
    result = teams.update_one(
        { 'TeamId': team_id} , 
        {
            '$push' : { 
                'Groups' : { 
                    'GroupName' : group_name, 
                    'Members' : members }}})

    return result

def update_team_update_group(team_id, group_name, members, collection):
    # method called when team exists, so it team should not be None
    team = collection.find_one({ 'TeamId' : team_id})
    
    for group in team['Groups']:
        if group['GroupName'] == group_name:
            return {"Text" : group_name + " already exists as a group in this workspace" }
    
    result = teams.update_one(
        { 'TeamId': team_id} , 
        {
            '$push' : { 
                'Groups' : { 
                    'GroupName' : group_name, 
                    'Members' : members }}})

    return result

def create_new_group(team_id, group_name, members):
    collection = get_collection()
    if collection.count() == 0:
        return create_new_team_document(team_id, group_name, members, collection)
    else:
        return update_team_add_new_group(team_id, group_name, members, collection)

