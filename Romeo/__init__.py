from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION

spam_chats = []
SUDO_USER = SUDO_USERS
SUDO_USERS.append(OWNER_ID)

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN,
    plugins=dict(root="Romeo/plugins"),
    in_memory=True,
)

client = Client(
    name="demon",
    api_id=API_ID,22652483
    api_hash=API_HASH,3046c28ec83815dcee7f2a6e3a82127b
    bot_token=BOT_TOKEN,
    session_string=STRING_SESSION,BQBociWuKpiIGHB1zDdf0JKEdQKqlmI95Jlpx3ECpRTMDLG63KfIPhpms9odbDsoKN8f1gguKqu4Lrd0BlBCzuTjCdu6DzDR1S0GlEhFnZjD_0Vyf275hc3eZ6IP_riqaY63NnNRPvPzEP7Qhl4HbjKv1_NHD-RSY_X8MA6Fy5zkwjkIXK5dvCjQjvPhlqt4QAkmeDTW0JmBl4RC4d-PpDf9HLuW-fDkrY0yickOAIv2Xvcntc9-zdmkihN4blolzBZ3SKVI5CG-hdqatI9mjEmZNFaBsJVqG2Y1rk0EO73qYE51Sjmc0UdFc43R2J0Vxi5dXunDICWtzH6I2u6PJKVFAAAAAZSqtywA
    plugins=dict(root="Romeo/plugins")
)

