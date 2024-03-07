############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

###############################################
import random
art = """
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝"""
print(art)
def again():
    loop = True
    while loop == True:
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card_len = len(cards)
        
        player_money = 1000
        computer_money = 1000
        
        all_card_Computer_list = []


        def Computer_cards():
            for card in range(0, 2):
                Computer_card = random.randint(0, card_len)
                index = int(cards[Computer_card - 1])
                all_card_Computer_list.append(index)


        Computer_cards()
        total_card_computer = sum(all_card_Computer_list)


        all_card_player_list = []


        def player_cards():
            for card in range(0, 2):
                player_card = random.randint(0, card_len)
                index = int(cards[player_card - 1])
                all_card_player_list.append(index)


        player_cards()
        total_card_player = sum(all_card_player_list)
        print(
        f"Your cards is {all_card_player_list}, your total card is {total_card_player}")
        print(f"the computer card is {all_card_Computer_list[0]}")
        ask1 = input("Do you want 'Wit' or 'Stand' ")
        lower_ask1 = ask1.lower()
        while lower_ask1 == "wit":
            for card in range(0, 1):
                player_card = random.randint(0, card_len)
                index = int(cards[player_card - 1])
                all_card_player_list.append(index)
                total_card_player = sum(all_card_player_list)
                print(f"Your cards is {total_card_player}")
            if total_card_player > 21:
                print("you lost!")
                lower_ask1 = "Stand"
            if total_card_player <= 21:
                ass = input("Do you want 'Wit' or 'Stand' ")
                lower_ask1 = ass   
        loop = False
        if lower_ask1 == "stand":
            print(f"your total card is {total_card_player}")

        random_choose = random.randint(0, 1)
        while random_choose == 0:
            for card in range(0, 1):
                Computer_card = random.randint(0, card_len)
                index = int(cards[Computer_card - 1])
                all_card_Computer_list.append(index)
                random_choose = random.randint(0, 1)
        total_card_computer = sum(all_card_Computer_list)
        if random_choose == 1:
            print(f"Computer cards is {total_card_computer}")
            if total_card_computer > 21:
                print(f"You Win!")
                loop = False
        if total_card_computer <= 21:
            if total_card_computer > total_card_player:
                print("you lost! ")
        if total_card_player <= 21:
            if total_card_computer < total_card_player:
                print(f"You Win!")
        if total_card_computer == total_card_player:
            print("drow")
        #print(f"you have {player_money}")
        #print(f"the computer have {computer_money}")
        ask2 = input("Do you want another round? ")
        if ask2 == "yes":
            again()
        else:
            print("Good Game")    
again()

