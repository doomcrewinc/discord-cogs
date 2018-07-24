# Developed by doomcrewinc
from discord.ext import commands
import random
import json
from pprint import pprint

class Catfact:
    """Random Cat Fact."""

    def __init__(self, bot):
        self.bot = bot
        
        with open('catfacts.json', encoding='utf-8') as cat_file:
            catdata = json.loads(cat_file.read())
        factslist=[]
        for line in catdata["data"]:
            factslist.append(line)
        choice=random.choice(factslist)
        pprint(choice['fact'])
        
        

    @commands.command(name="catfact")
    async def _cookie(self):
        """You want a catfact?

        Here's your catfact!
        """
        return await self.bot.say("`" + choice['fact'] + "`")


def setup(bot):
    bot.add_cog(Catfact(bot))

