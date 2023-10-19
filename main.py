import discord, asyncio, datetime, httpx, discordwebutils
from colorama import Fore, init; init()

def getTime():
    x = datetime.datetime.now(); currenttime = x.strftime("%H") + ":" + x.strftime("%M") + ":" + x.strftime("%S")
    return currenttime

GUILD_ID = "1147892436782284912"
valid_codes = {"numb"}

async def snipe_vanity(name):
    url = f"https://discord.com/api/v9/guilds/{GUILD_ID}/vanity-url"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Authorization": f"{TOKEN}",
        "Content-Type": "application/json",
        "Origin": "https://discord.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    }
    data = {
        "code": name
    }
    async with httpx.AsyncClient() as client:
        response = await client.patch(url, headers=headers, json=data)
        if response.status_code == 200:
            print(" "); print(f"{Fore.WHITE}[{Fore.CYAN}{getTime()}{Fore.WHITE}]    Sniped! -> {response.status_code} {response.text}"); print(" ")
        else:
            print(f"{Fore.WHITE}[{Fore.CYAN}{getTime()}{Fore.WHITE}]    Taken -> {response.status_code} {response.text}")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"{Fore.WHITE}[{Fore.CYAN}{getTime()}{Fore.WHITE}]    {Fore.WHITE}[{Fore.GREEN}√{Fore.WHITE}] {self.user} {Fore.GREEN}-> {Fore.WHITE}logged in")

    async def on_guild_update(self, before, after):
        if before.vanity_url != after.vanity_url:
            code = before.vanity_url.split(".gg/")[1]; print(f"{Fore.WHITE}[{Fore.CYAN}{getTime()}{Fore.WHITE}]    Vanity Released -> {code}")
            if code in valid_codes:
                await snipe_vanity(code)




























client = MyClient()
TOKEN = "x"
client.run(TOKEN)
