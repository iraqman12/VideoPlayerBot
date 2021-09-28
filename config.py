"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "8634206"))
API_HASH = getenv("API_HASH", "fc8f066ba30e9cc6b0da2af1561f2744")
BOT_TOKEN = getenv("BOT_TOKEN", "1983708781:AAGxBsWO1FE6DzZuAF-PMnlbaa1Ompzeg8Y")
SESSION_STRING = getenv("SESSION_STRING", "AgAM2GjROA6X9Cjdscn0pTJum7BdZmNZzmRw8XcGjWTVDUKTEBirCUeJCDTngEoKvQJBHyCSjKJYMpw80efiSatOXo6BWCRSKL9opGD1dk90LKFXtcVgzvMnDbJP9MkEvb7RykutSgSdBfOoGj_Z5Pvub9CuyGBB_12YB0_hKMU_zQym0iyALBWFVcQCYBQwT4TlOMm7JCMwQ1Yt34Xz66ksbl_o7gcaZJe6o5FePUlBsE4tMwQ-FlKSXXVO-ZGTmZeSSPDtqqn2e_KUoRLfjII9R9elcpkCE76JcNL3eH75VdFm0mVoY6PtvDLWZ7Eii8mDj2MxH1t2dZtO5lFGqgd7d6VUsQA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "SafoTheBot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsmSafone")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MyVideoPlayer")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2007323825").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "Hello Sir, I'm a bot, not having time to chat with you.")
if REPLY_MESSAGE:
    REPLY_MESSAGE = REPLY_MESSAGE
else:
    REPLY_MESSAGE = None
