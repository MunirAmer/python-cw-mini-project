# write your code here
cost = ""
def padel_court_cost(court_type):
    if court_type == "indoor":
        return print(30)
    
    elif court_type == "outdoor":
        return print(20)  
              

def rackets_cost(racket_brand):
    if racket_brand == "Bullpadel":
        return print(100)
    elif racket_brand == "Nox":
        return print(140)
    elif racket_brand == "Siux":
        return print(200)

def padel_balls_cost(ball_boxes):
    if  ball_boxes == 1:
        return print(2)
    elif ball_boxes == 2:
        return print(3.5)
    elif ball_boxes == 3:
        return print(5)
    

def padel_game_cost():
    hours = input("How many hours do you want to spend: ")
    court_type = input("Enter court type:")
    racket_brand = input("Enter racket company: ")
    ball_boxes = input("Enter ball boxes number: ")
    return print(f'''hours:{hours}\n 
Court type: {court_type}\n
Racket brand: {racket_brand}\n 
ball boxes: {ball_boxes}
''')
    
padel_game_cost()








