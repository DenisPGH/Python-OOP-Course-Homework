from project_.player import Player
from project_.guild import Guild

player = Player("George", 50, 100)
player_1 = Player("Miro", 500, 1000)
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Shield Break", 20))
# print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.assign_player(player_1))
#print(guild.kick_player("George"))
print(guild.guild_info())
print(player.guild)
