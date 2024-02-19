import discord
from discord.ext import commands
from win10toast import ToastNotifier
import config
import os


# Use sam TTS i couldve used pyttx3? but i didnt :shrug:
class Sam:
    def __init__(self, words: str, SAM_DIR: str = "sam.exe"):
        if not os.path.exists(SAM_DIR):
            raise FileNotFoundError("ERROR SAM.exe Couldnt be found")
        
        args = f"{SAM_DIR} {words}"
        os.system(args)




# Setting up discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
toast = ToastNotifier()

@bot.event
async def on_ready():
    Sam("Bot is ready to rock and roll")

# on >messsage "" ""
@bot.command()
async def message(ctx, *args):
    if len(args) >= 1:

        # get the title and content
        title = f"{ctx.author.name.title()}: {args[0]}"
        content = ' '.join(args[1:])
        
        print(f"\nNew message from {ctx.author.name}: {title}:{content}\n")
        toast.show_toast(title, content, threaded= True)
        Sam(content)

# Run the bot
bot.run(config.TOKEN)
