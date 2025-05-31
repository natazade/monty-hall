import random
def monty_hall_game(switch_door):
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)
    initial_choice = random.choice(range(3))
    revealed_doors = [i for i in range(3) if i!=initial_choice and doors[i] != 'car' ]
    revealed_door = random.choice(revealed_doors)
   
    if switch_door:
        final_choice = [i for i in range(3) if i!= revealed_door and i != initial_choice][0]

    else:
        final_choice = initial_choice

    return doors[final_choice] == 'car' 


def simulate_game(num_games):
    num_wins_without_switching = sum([monty_hall_game(False) for _ in range(num_games)])
    num_wins_with_switching = sum([monty_hall_game(True) for _ in range(num_games)])
    return num_wins_without_switching , num_wins_with_switching

print(simulate_game(100))    

