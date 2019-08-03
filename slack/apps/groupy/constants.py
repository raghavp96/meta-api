import os

# JSON Keys

json_team_id_key = "TeamId"
json_message_id_key = "MessageId"
json_users_id_key = "Users"
json_group_name_key = "GroupName"

# DB Keys
db_name = os.environ.get('GROUPY_APP_DB_NAME', 'test')
db_user_profile = os.environ.get('GROUPY_APP_DB_USER_PROFILE', None)
db_user_pwd = os.environ.get('GROUPY_APP_DB_USER_PWD', None)
db_hosts = os.environ.get('GROUPY_APP_DB_HOST_PORT', None)

db_team_id_key = json_team_id_key
db_groups_key = 'Groups'
db_group_name_key = json_group_name_key
db_members_key = 'Members'