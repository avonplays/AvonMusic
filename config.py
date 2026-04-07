import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 37117827
API_HASH = "5eb1a6965aa5c5fdb59b89479931058d"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8537193754:AAEJCN_0vlga3G5ABy8t7Lylux1uoJe9nkg"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Avon:Avon@avon.fstai.mongodb.net/?retryWrites=true&w=majority"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 999))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002353470224

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7895661089

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/avonplays/AvonMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/Repository_Hub"
SUPPORT_GROUP = "https://t.me/RepoSitory_Chat"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION1", "BQI2X4MALUbG8feSHlRl2LRyKJlM7OeGdGgpNWJszu-d-bH1EKt3Ne3CWs9wbKX-76NdGxrK8jtpyTTsrx9BLBI26eqy8_K5IuVXP5zGhqF9g_xFAh81d9a1nzaYBaEsQtomKSPsOe9pSo0qTCBO-l0vIvMvYevDDrFEwY3iPlWIQB1mUYbxHBXw1E9Z-cZU0EY4YhtTuXvpQH7NXXU2reR-Wy4JMJyUi9nvOMT3YtKqVULrqgrqOrezslP9wKdiIIkWiECgFvHH7PprTPWmWAagmxFcAu_iRiKqFzsWiSQeXg4_66fASoDi7oMoZ1Gnp21Mm0qstzpqADYjl1lQvIOZoWbMvgAAAAGmsRhEAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://telegra.ph/file/d6e41e4ec944ac5005171.jpg"

PING_IMG_URL = "https://graph.org/file/a91c82c2e312a56d2db4e-e60a99710077dbdd38.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/a91c82c2e312a56d2db4e-e60a99710077dbdd38.jpg"
STATS_IMG_URL = "https://graph.org/file/a91c82c2e312a56d2db4e-e60a99710077dbdd38.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )




