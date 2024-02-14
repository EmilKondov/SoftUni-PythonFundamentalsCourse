def team_lineup(*data):
    #Count in a dict key-country values- player how many players for each country
    players = {}

    #iterate through KVP and add to the dict
    for player, country in data:
        if country not in players:
            players[country] = []
        players[country].append(player)

    #sort the countires by the number of players (descending) and then by country name lenght
    sorted_countires_players = dict(sorted(players.items(), key=lambda x: (-len(x[1]), (x[0]))))

    result = ''
    for country, player in sorted_countires_players.items():
        result += f"{country}:\n"

        for name in player:
            result += f"  -{name}\n"
    return result.strip()

print(team_lineup(

   ("Harry Kane", "England"),

   ("Manuel Neuer", "Germany"),

   ("Raheem Sterling", "England"),

   ("Toni Kroos", "Germany"),

   ("Cristiano Ronaldo", "Portugal"),

   ("Thomas Muller", "Germany"),

   ("Bruno Fernandes", "Portugal"),

   ("Bernardo Silva", "Portugal"),

   ("Harry Maguire", "England")))

