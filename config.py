#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", "22505271"))
API_HASH = getenv("API_HASH", "c89a94fcfda4bc06524d0903977fc81e")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "6020516635").split())
)  # Input type must be interger

# ADMIN USERS
ADMIN_USER = list(
    map(int, getenv("ADMIN_USER", "6020516635").split())
)  # Input type must be interger

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = getenv(
    "PRIVATE_START_MESSAGE",
    "Hello! Welcome to Cheems Feedback Bot, Send feedback about our bots here",
)
