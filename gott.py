import disnake
import disnake.ext
from disnake.ext import commands
from config import DISCORD_BOT_TOKEN


def main():
    print("running")
    bot.run(DISCORD_BOT_TOKEN)


bot = commands.Bot(command_prefix='!',
                   test_guilds=[970711821478686721], intents=disnake.Intents.all(), auto_sync=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("shutting down")
        exit(0)
    finally:
        bot.close()
