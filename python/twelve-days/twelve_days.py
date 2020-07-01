lines = [  "twelve Drummers Drumming, ",
            "eleven Pipers Piping, ",
            "ten Lords-a-Leaping, ",
            "nine Ladies Dancing, ",
            "eight Maids-a-Milking, ",
            "seven Swans-a-Swimming, ",
            "six Geese-a-Laying, ",
            "five Gold Rings, ",
            "four Calling Birds, ",
            "three French Hens, ",
            "two Turtle Doves, and ",
            "a Partridge in a Pear Tree."]

days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

def verse(day):
    verse = []
    verse += "On the {} day of Christmas my true love gave to me: ".format(days[day-1])
    verse += lines[-day:]
    return "".join(verse)

def recite(start_verse, end_verse):
    response = []
    for day in range(start_verse, end_verse+1):
        response.append(verse(day))
    return response
