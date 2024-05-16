from random import choice
def winning_ticket(possibilities):
    selected = []
    while len(selected) < 4:
        s1 = choice(possibilities)
        if s1 not in selected:
            selected.append(s1)
    return selected


def checking_ticket(specific_ticket, winner_ticket):
    for elements in specific_ticket:
        if elements not in winner_ticket:
            return False
        
    return True

def random_ticket(possibilities):
    my_ticket = []
    while len(my_ticket) < 4:
        s2 = choice(possibilities)
        if s2 not in my_ticket:
            my_ticket.append(s2)
    return my_ticket

def analysis(possibilities):
    plays = 0
    won = False
    winner = winning_ticket(possibilities)
    while not won:
        my_ticket = random_ticket(possibilities)
        won = checking_ticket(my_ticket,winner)
        plays += 1
        if plays > 1000000:
            break
    if won:
        print("We have a winning ticket!")
        print(f"Your ticket: {my_ticket}")
        print(f"Winning ticket: {winner}")
        print(f"It only took {plays} tries to win!")
    else:
        print(f"Tried {plays} times, without pulling a winner. :(")
        print(f"Your ticket: {my_ticket}")
        print(f"Winning ticket: {winner}")

      

