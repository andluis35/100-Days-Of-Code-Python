import art

def fill_dictionary(dictionary):
    while True:
        print("---------------------------------")
        bidder_name = input("What's your name?: ")
        bid = float(input("What's your bid?: "))
        print("---------------------------------")
        dictionary[bidder_name] = bid

        choice = int(input("Are there any other bidders?\n[1] Yes\n[2] No\nR: "))
        if choice != 1:
            print("\n" * 100)
            return dictionary

        print("\n" * 100)

def find_biggest_bidder(dictionary):
    major_bidder = ""
    major_bid = -1

    for key in dictionary:
        if dictionary[key] > major_bid:
            major_bidder = key
            major_bid = dictionary[key]

    return major_bidder


bids = {}

print(art.logo)
print("Welcome to the secret auction program.")

bids = fill_dictionary(bids)
biggest_bidder = find_biggest_bidder(bids)
biggest_bid = bids[biggest_bidder]

print("=-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-=-=-=")
print(f"The biggest bid was ${biggest_bid} from {biggest_bidder}!")
print("=-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-=-=-=")
