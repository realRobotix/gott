import disnake
import disnake.ext
from disnake.ext import commands


def main():
    print("running")
    bot.run("OTY3NDk3NDQyODU5ODI3MjQy.Gl8ej4.Ctye1103UBjxIcE64X_FNO0o_qOX001WqRpeq4")


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
