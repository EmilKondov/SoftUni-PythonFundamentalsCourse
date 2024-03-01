from project.player import Player

class Guild:
    def __init__(self, name: str,):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):

        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        # self.players.append(player.name)
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name not in self.players:
            player.guild = "Unaffiliated"
            return f"Player {player_name} is not in the guild."

        self.players.remove(player_name)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        # guild_info = Player.player_info(self)
        guild_info = "\n".join(player.player_info() for player in self.players)
        return f"Guild: {self.name}\n"\
               f"{guild_info}"




