async def get_max_role_position(guild):
    max_role_position = 0
    for role in guild.roles:
        if role.position > max_role_position:
            max_role_position = role.position
    return max_role_position


async def get_bot_role_position(guild, bot):
    for role in guild.roles:
        if role.name == bot.user.name:
            return role.position
