from random import randint, choice
import art
import game_data

data = game_data.data

def print_statement(person1,person2,score):
    print(f"Current score is {score}")
    print(f"Compare A: {person1['name']}, {person1['description']} from {person1['country']}")
    print(art.vs)
    print(f"Against B: {person2['name']}, {person2['description']} from {person2['country']}")

def is_higher(person1,person2):
    if person1['follower_count'] < person2['follower_count']:
        return 'b'
    elif person1['follower_count']>person2['follower_count']:
        return 'a'

def game():
    print(art.logo)

    person1 = choice(data)
    person2 = choice(data)
    while person2==person1:
        person2= choice(data)

    game_over=False
    score=0

    while not game_over:
        print_statement(person1,person2,score)
        answer=input("Who has more followers ? A or B  ").lower()
        guess = is_higher(person1,person2)
        if answer==guess:
                print("\n\n\nCorrect answer! On to the next one...\n\n\n")
                score+=1
                if guess=='a':
                    person1=person1
                    temp=person2
                    while person2 == person1 or person2==temp:
                        person2 = choice(data)

                elif guess=="b":
                    person1=person2
                    while person2 == person1:
                        person2 = choice(data)
        else:
            game_over = True
            if guess=='b':
                print(f"Wrong answer! {person2['name']} had more followers!")
            elif guess=='a':
                print(f"Wrong answer! {person1['name']} had more followers!")

    cont = input("\n\n\nDo you want to continue? yes or no\n")
    if cont=='yes':
        game()
    elif cont=='no':
        print(f"Your final score is {score}")

game()
