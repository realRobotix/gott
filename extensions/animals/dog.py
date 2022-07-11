import json
from disnake.ext import commands
import disnake
from requests import request
from typing import *
import os
from ._animal import *


class Dog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.uri = "https://api.thedogapi.com/v1/"

    @commands.slash_command(name="dog")
    async def dog(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @dog.sub_command(name="breed")
    async def breed(
        self,
        inter: disnake.ApplicationCommandInteraction,
        page: int = 0,
        search: str = "",
    ):
        if search != "":
            __location__ = os.path.realpath(
                os.path.join(os.getcwd(), os.path.dirname(__file__))
            )
            cache = json.load(
                open(os.path.join(__location__, "dog_breeds_cache.json"), "rt")
            )
            breeds = request(
                "GET",
                self.uri + "breeds/search/",
                headers={"x-api-key": self.bot.env.THEDOGAPI_API_KEY},
                params={"q": search},
            ).json()
            await inter.response.send_message(
                embed=AnimalBreedEmbed(
                    breed=breeds[page],
                    page=page,
                    max_page=len(breeds) - 1,
                    avatar_url=self.bot.user.avatar.url,
                    cache=cache,
                ),
                components=AnimalBreedEmbedComponents(inter=inter, bot=self.bot),
                ephemeral=False,
            )

        else:
            __location__ = os.path.realpath(
                os.path.join(os.getcwd(), os.path.dirname(__file__))
            )
            breeds = json.load(
                open(os.path.join(__location__, "dog_breeds_cache.json"), "rt")
            )
            await inter.response.send_message(
                embed=AnimalBreedEmbed(
                    breed=breeds[page],
                    page=page,
                    max_page=len(breeds) - 1,
                    avatar_url=self.bot.user.avatar.url,
                ),
                components=AnimalBreedEmbedComponents(inter=inter, bot=self.bot),
                ephemeral=False,
            )
            cache = None
        while True:
            try:
                button_inter: disnake.MessageInteraction = await self.wait_for_buttons(
                    inter=inter,
                    ids=[
                        f"animal_left-{inter.id}",
                        f"animal_right-{inter.id}",
                    ],
                )
            except TimeoutError:
                for button in button_inter.message.components:
                    button.disabled = True
                return
            # check wich button has been pressed
            if button_inter.component.custom_id == f"animal_left-{inter.id}":
                page -= 1
                if page < 0:
                    page = len(breeds) - 1
            elif button_inter.component.custom_id == f"animal_right-{inter.id}":
                page += 1
                if page > len(breeds) - 1:
                    page = 0
            else:
                continue
            await button_inter.response.edit_message(
                embed=AnimalBreedEmbed(
                    breed=breeds[page],
                    page=page,
                    max_page=len(breeds) - 1,
                    avatar_url=self.bot.user.avatar.url,
                    cache=cache,
                ),
                components=AnimalBreedEmbedComponents(inter=inter, bot=self.bot),
            )

    @dog.sub_command(name="vote")
    async def vote(self, inter: disnake.ApplicationCommandInteraction):
        has_voted = []
        image = request(
            "GET",
            url=self.uri + "images/search",
            headers={"x-api-key": self.bot.env.THEDOGAPI_API_KEY},
            params={"order": "random", "limit": "1"},
        ).json()[0]
        await inter.response.send_message(
            embed=AnimalVoteEmbed(url=image["url"]), components=AnimalVoteButtons(inter)
        )
        while True:
            button_inter = await self.wait_for_buttons(
                inter=inter,
                ids=[
                    f"animal_upvote-{inter.id}",
                    f"animal_downvote-{inter.id}",
                    f"animal_refresh-{inter.id}",
                ],
            )

            if button_inter.component.custom_id == f"animal_refresh-{inter.id}":
                has_voted = []
                image = request(
                    "GET",
                    url=self.uri + "images/search",
                    headers={"x-api-key": self.bot.env.THEDOGAPI_API_KEY},
                    params={"order": "random", "limit": "1"},
                ).json()[0]
                await button_inter.response.edit_message(
                    embed=AnimalVoteEmbed(url=image["url"]),
                    components=AnimalVoteButtons(inter),
                )

            print(has_voted)
            if button_inter.author.id in has_voted:
                if button_inter.response.is_done():
                    await button_inter.response.edit_message("You have already voted!")
                else:
                    await button_inter.response.send_message(
                        "You have already voted!", ephemeral=True
                    )
                continue

            if button_inter.component.custom_id == f"animal_upvote-{inter.id}":
                data = {
                    "image_id": image["id"],
                    "sub_id": str(self.bot.user.id) + str(inter.author.id),
                    "value": 1,
                }
                request(
                    method="POST",
                    url=self.uri + "votes",
                    json=data,
                    headers={"x-api-key": self.bot.env.THEDOGAPI_API_KEY},
                )
                await button_inter.response.send_message(
                    "You upvoted successfully!", ephemeral=True
                )
                has_voted.append(button_inter.author.id)

            if button_inter.component.custom_id == f"animal_downvote-{inter.id}":
                data = {
                    "image_id": image["id"],
                    "sub_id": str(self.bot.user.id) + str(inter.author.id),
                    "value": 0,
                }
                request(
                    method="POST",
                    url=self.uri + "votes",
                    json=data,
                    headers={"x-api-key": self.bot.env.THEDOGAPI_API_KEY},
                )
                await button_inter.response.send_message(
                    "You downvoted successfully!", ephemeral=True
                )
                has_voted.append(button_inter.author.id)

    async def wait_for_buttons(
        self, inter: disnake.ApplicationCommandInteraction, ids: List[str]
    ) -> disnake.MessageInteraction:
        return await self.bot.wait_for(
            "button_click",
            check=lambda i: i.component.custom_id in ids,
            timeout=1200,
        )


def setup(bot: commands.Bot):
    bot.add_cog(Dog(bot))
