players_sent_off = input().split()

players_count_A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
players_count_B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

referee_stop_the_game = False

for player in players_sent_off:
    if player in players_count_A:
        players_count_A.remove(player)
    elif player in players_count_B:
        players_count_B.remove(player)
    if len(players_count_A) < 7 or len(players_count_B) < 7:
        referee_stop_the_game = True
        break
print(f"Team A - {len(players_count_A)}; Team B - {len(players_count_B)}")
if referee_stop_the_game:
    print('Game was terminated')
