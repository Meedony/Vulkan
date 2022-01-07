import re
import asyncio
from config import config


def is_connected(ctx):
    try:
        voice_channel = ctx.guild.voice_client.channel
        return voice_channel
    except:
        return None


def format_time(duration):
    if not duration:
        return "00:00"

    hours = duration // 60 // 60
    minutes = duration // 60 % 60
    seconds = duration % 60

    return "{}{}{:02d}:{:02d}".format(
        hours if hours else "",
        ":" if hours else "",
        minutes,
        seconds
    )


def is_url(string) -> bool:
    """Verify if a string is a url"""
    regex = re.compile(
        "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

    if re.search(regex, string):
        return True
    else:
        return False


class Timer:
    def __init__(self, callback):
        self.__callback = callback
        self.__task = asyncio.create_task(self.__executor())

    async def __executor(self):
        await asyncio.sleep(config.VC_TIMEOUT)
        await self.__callback()

    def cancel(self):
        self.__task.cancel()
