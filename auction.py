bidders_details = {}
def auction(name,price):
    bidders_details[name] = price

def highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        total_price = bid_record[bidder]
        if total_price > highest_bid:
            highest_bid = total_price
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")        


while True:   
    name_of_the_person=input("What's your name? ")
    bid_price=int(input("What's your bid? $"))
    auction(name=name_of_the_person,price=bid_price)
    next_person=input("Are there any other bidders? Type 'yes' or 'no'")
    
    if next_person == 'yes':
        continue
    else:
        highest_bidder(bidders_details)
        
        
