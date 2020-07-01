drops = (("Pling", 3), ("Plang", 5), ("Plong", 7))

def convert(n):
    noise = [s for s, f in drops if n % f == 0]
    return "".join(noise) or str(n)    