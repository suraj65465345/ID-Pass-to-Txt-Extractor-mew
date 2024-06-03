import os

api_id = 22223501
api_hash = os.environ.get("API_HASH", "e78c151d670ab33c5f7f731027c5ab26")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "6235754855")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "6235754855")
owner_users = [int(num) for num in osowner_users.split(",")]
