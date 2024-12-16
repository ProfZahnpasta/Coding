import random
import os
import time

def main():
    print("Welcome to White Jack.")
    user_cards = random.randint(0, 10)
    user_cards_total = int(user_cards)
    dealer_cards = random.randint(11, 21)
    print("Your Cards:", user_cards) 
    hit_or_stay = input("Do you want to hit or stay and reveal the cards of the dealer? h/s ")
    
    def hit():
        nonlocal user_cards_total
        user_cards = random.randint(0, 10)
        user_cards_total += int(user_cards)
        print("Your Card:", user_cards)
        print("Your total:", user_cards_total)
        if user_cards_total >= 21:
            print("You're total card count has gone greater than 21. You've lost.")
            print("You've lost! The game will delete itself now. Bye Bye!")
            time.sleep(3)
            os.remove("./White Jack.py")
        else:
            hit_or_stay = input("Do you want to hit or stay and reveal the cards of the dealer? h/s ")
            if hit_or_stay == "h":
                hit()
            elif hit_or_stay == "s":
                print("Your total cards:", user_cards_total)
                print("Dealer's total cards:", dealer_cards)
                if user_cards_total > dealer_cards:
                    play_again = input("You've won! Do you want to play again? y/n ")
                    if play_again == "y":
                        main()
                elif user_cards_total < dealer_cards:
                    print("You've lost! The game will delete itself now. Bye Bye!")
                    time.sleep(3)
                    os.remove("./White Jack.py")
    
    if hit_or_stay == "h":
        hit()
    elif hit_or_stay == "s":
        print("Your total cards:", user_cards_total)
        print("Dealer's total cards:", dealer_cards)
        if user_cards_total > dealer_cards:
            play_again = input("You've won! Do you want to play again? y/n ")
            if play_again == "y":
                os.system("cls")
                main()
        elif user_cards_total < dealer_cards:
            print("You've lost! The game will delete itself now. Bye Bye! ")
            time.sleep(3)
            os.remove("./White Jack.py")

main()