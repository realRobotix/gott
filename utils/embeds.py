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
        value = process.stdout + process.stderr
        if value == "" or value == None:
            value = "None"
        self.add_field(name="Output:", value=value)
