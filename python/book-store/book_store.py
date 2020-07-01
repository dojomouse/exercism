PRICES = {
        1: 8*100,
        2: 8*2*0.95*100,
        3: 8*3*0.9*100,
        4: 8*4*0.8*100,
        5: 8*5*0.75*100
    }

def total(basket):
    # Basket is an array of ints.
    # One copy of any of the five books costs $8.
    # If, however, you buy two different books, you get a 5% discount on those two books.
    # If you buy 3 different books, you get a 10% discount.
    # If you buy 4 different books, you get a 20% discount.
    # If you buy all 5, you get a 25% discount.
    # Note: that if you buy four books, of which 3 are different titles, you get a 10% discount on the 3 that form part of a set, but the fourth book still costs $8.
    # Make 'bundles' an array of sets.
    bundles = []
    while len(basket) > 0:
        bundle = set(basket)
        for book in bundle:
            basket.remove(book)
        bundles.append(bundle)
    # The only improvement on max-first assignment advantage comes through making 3/5 pairs into 4/4 pairs.
    # How many 3's are there for which there's a 5?
    # num3's - max(0,(num_3s-num_5s)_
    bundle_sizes = {}
    for bundle in bundles:
        bundle_sizes[len(bundle)] = bundle_sizes.get(len(bundle),0) + 1
    discount = (PRICES[3]+PRICES[5]-2*PRICES[4]) * (bundle_sizes.get(3,0) - max(bundle_sizes.get(3,0) - bundle_sizes.get(5,0),0))
    price = sum(PRICES[len(s)] for s in bundles) - discount
    return price