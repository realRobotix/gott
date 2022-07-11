from itertools import islice
from disnake.ext import commands
import disnake


class AnimalVoteEmbed(disnake.Embed):
    def __init__(self, url: str):
        super().__init__()
        self.set_image(url=url)


class AnimalVoteButtons(disnake.ui.ActionRow):
    def __init__(self, inter: disnake.ApplicationCommandInteraction):
        super().__init__()
        self.add_button(
            emoji="👍",
            style=disnake.ButtonStyle.success,
            custom_id=f"animal_upvote-{inter.id}",
            disabled=False,
        )
        self.add_button(
            emoji="👎",
            style=disnake.ButtonStyle.danger,
            custom_id=f"animal_downvote-{inter.id}",
            disabled=False,
        )
        self.add_button(
            emoji="🔄",
            style=disnake.ButtonStyle.primary,
            custom_id=f"animal_refresh-{inter.id}",
            disabled=False,
        )


class AnimalBreedEmbed(disnake.Embed):
    def __init__(
        self,
        breed: dict,
        page: int,
        max_page: int,
        avatar_url: str,
        cache: list = None,
        set_image: bool = True,
        id: int = None,
    ):

        if "name" in breed.keys():
            super().__init__(title=f'Breed: {breed["name"]}')
        else:
            super().__init__()

        for key in breed.keys():
            if key in [
                "indoor",
                "lap",
                "alt_name",
                "adaptability",
                "affection_level",
                "child_friendly",
                "dog_friendly",
                "energy_level",
                "grooming",
                "health_issues",
                "intelligence",
                "shedding_level",
                "social_needs",
                "stranger_friendly",
                "vocalisation",
                "experimental",
                "hairless",
                "natural",
                "rare",
                "rex",
                "suppressed_tail",
                "short_legs",
                "hypoallergenic",
            ]:
                self.add_field(
                    name=f"{key.replace('_',' ').capitalize()}:",
                    value=str(breed[key]) + " / 5",
                    inline=False,
                )
            elif (
                not key
                in [
                    "country_code",
                    "country_codes",
                    "weight",
                    "height",
                    "image",
                    "reference_image_id",
                    "id",
                ]
                and breed[key] != None
                and breed[key] != ""
            ):
                self.add_field(
                    name=f"{key.replace('_',' ').capitalize()}:",
                    value=breed[key],
                    inline=False,
                )
            elif (
                key in ["weight"]
                and breed[key]["metric"] != None
                and breed[key]["metric"] != ""
            ):
                self.add_field(
                    name=f"{key.capitalize()} (kg):",
                    value=breed[key]["metric"],
                    inline=False,
                )
            elif (
                key in ["height"]
                and breed[key]["metric"] != None
                and breed[key]["metric"] != ""
            ):
                self.add_field(
                    name=f"{key.capitalize()} (cm):",
                    value=breed[key]["metric"],
                    inline=False,
                )
        if set_image:
            if (
                "image" in breed.keys()
                and breed["image"] != None
                and breed["image"] != ""
            ):
                self.set_image(url=breed["image"]["url"])
            elif (
                "reference_image_id" in breed.keys()
                and breed["reference_image_id"] != None
                and breed["reference_image_id"] != ""
                and "id" in breed.keys()
                or id != None
                and cache != None
            ):

                if id != None:
                    pass
                else:
                    id = breed["id"]

                image_url = next(
                    item
                    for item in cache
                    if item["id"] == id
                    and item["image"]["url"] != ""
                    and item["image"]["url"] != None
                )["image"]["url"]
                if image_url != "" and image_url != None:
                    self.set_image(url=image_url)

            self.set_footer(text=f"Page {page}/{max_page}", icon_url=avatar_url)


class AnimalBreedEmbedComponents(disnake.ui.ActionRow):
    def __init__(self, inter: disnake.ApplicationCommandInteraction, bot: commands.Bot):
        super().__init__()
        self.add_button(
            emoji="⬅️",
            style=disnake.ButtonStyle.primary,
            custom_id=f"animal_left-{inter.id}",
            disabled=False,
        )
        self.add_button(
            emoji="➡️",
            style=disnake.ButtonStyle.primary,
            custom_id=f"animal_right-{inter.id}",
            disabled=False,
        )


class AnimalBreedEmbeds(list):
    def __init__(
        self,
        breed: dict,
        page: int,
        max_page: int,
        avatar_url: str,
        cache: list = None,
        id: int = None,
    ) -> None:
        super().__init__()
        while len(breed) > 0:
            part_breed = dict(islice(breed.items(), None, 25))
            self.append(
                AnimalBreedEmbed(
                    breed=part_breed,
                    page=page,
                    max_page=max_page,
                    avatar_url=avatar_url,
                    cache=cache,
                    set_image=len(breed) < 25,
                    id=id,
                )
            )
            for key in dict(islice(breed.items(), None, 25)).keys():
                breed.pop(key)
