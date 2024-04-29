#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6700540841:AAEzEG75XEQXqfTGmIvy136zVclAUBxQKOI")
    API_ID = int(os.environ.get("API_ID", "24665357"))
    API_HASH = os.environ.get("API_HASH", "beb7e4b83ada668fa85f9a9b56338f1d")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1717511106")
