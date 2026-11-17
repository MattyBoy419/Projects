num_players = int(input("How many Players? "))
num_teams = round(num_players / 11)

if num_players < 11:
    print("Not enough players")
elif num_players < 22:
    print("Makes 1 team")
else:
    print(f"Makes {num_teams} teams")

