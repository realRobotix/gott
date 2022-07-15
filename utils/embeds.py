import disnake
from disnake.ext import commands
import subprocess


class SubprocessEmbed(disnake.Embed):
    def __init__(self, process: subprocess.CompletedProcess):
        if process.returncode == 0:
            colour = disnake.Colour.green()
        else:
            colour = disnake.Colour.red()
        super().__init__(colour=colour)
        self.add_field(name="Output:", value=process.stdout)
