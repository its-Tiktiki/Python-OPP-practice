from art import logo

print(logo)
print("Welcome to the Secret Auction Program.")

bidders_dict = {}
on = True

while on:

    have_bidders = True
    while have_bidders:
        
        name = input("What's your name?: ")
        bid = int(input("What's your bid?: $"))

        bidders_dict[name] = bid

        user_input = input("Are there any other bidders? (yes/no): ").lower()
        if user_input != "yes":
            have_bidders = False

    winner_bet = 0
    winner_name = None
    for (key, value) in bidders_dict.items():
        if value > winner_bet:
            winner_bet = value
            winner_name = key

    print(f"The winner is {winner_name} with a bid of {winner_bet}")
    
    if_again = input("Do want to start again? (yes/no): ")
    if if_again != "yes":
        on = False


