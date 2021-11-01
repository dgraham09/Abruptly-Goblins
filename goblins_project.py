gamers = []


def add_gamer(gamer, gamers_list):
    if "name" and "availability" in gamer:
        gamers_list.append(gamer)
    else: 
        return false
    
add_gamer({"name": "David", "availability": "Monday"}, [])
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
add_gamer({"name": "Kimberly Warner", "availability": ["Monday","Thursday", "Sunday"]}, gamers)


def build_daily_frequency_table():
    return {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:  
        for day in gamer['availability']: 
            available_frequency[day] += 1

calculate_availability(gamers, count_availability)
# print(count_availability)

def find_best_night(availability_table): 
    return max(availability_table, key=availability_table.get)

game_night = find_best_night(count_availability)

def available_on_night(gamers_list, day): 
    attending_game_night = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            attending_game_night.append(gamer['name'])
        else:
            pass
    return attending_game_night

attending_game_night = available_on_night(gamers, game_night)

def send_email(attending_game_night, day_of_week, game): 
    for gamer in attending_game_night:
        name = gamer
        print(f'Greetings {name}! The {game} game will be played this week on {day_of_week}.')
#       print(form_email.format(name=gamers['name'], day_of_week=day, game=game))
        
send_email(attending_game_night, game_night, "Abruptly Goblins")
        
def unable_to_attend_generator(gamers_list):
    unable_to_attend_best_night = []
    for gamer in gamers:
        if game_night not in gamer['availability']:
            unable_to_attend_best_night.append(gamer)
    return unable_to_attend_best_night

unable_to_attend_best_night = unable_to_attend_generator(gamers)
print(unable_to_attend_best_night)

second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

available_second_night_game = available_on_night(gamers, second_night)

send_email(available_second_night_game, second_night, "Abruptly Goblins")
