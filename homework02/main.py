#!/usr/bin/env python3

# For completion of Homework 02 at pirple.com
# Walter Spicer

""" 
Homework Question:
Let's return to the music example from assignment one. Pick 3 of the attributes you listed. For our example we're going to say "Genre", "Artist" and "Year". Create a new Python file and create 3 functions with the same name as those attributes. So in this example we'd have one function named "genre" another named "artist" and another called "year".

When someone calls any of those functions, that function should return the corresponding value for that attribute. For example, if we call the "Artist" function our function would return "Dave Brubeck". Yours should return whatever values make sense for your music choice.
"""

# I did books, so the equivalent is genre, author, year
# However this pollutes the variable scope or looks confusing as they are the same as variables used.
# Thus the verb-function convention was used instead in order to describe WHAT the function does
# Therefore functions were renamed
#   print_genre
#   print_author
#   print_year
#
# Additionally made a larger single function that takes three paramatres with defaults.
#   print_book_data
#
# I followed the PEP-8 naming convention of lowercase and snake_case.


# For Homework02

def print_genre(genre):
    print(genre)


def print_author(author):
    print(author)


def print_year(year):
    print(year)


def print_asterisks():
    """
    Single location to change the format padding of astericks
    """
    print("*" * 20)


def print_book_data(genre="Science Fiction", author="David Brin", year=1992):
    """
    Print the book data for genre, author, and year all in one function.
    """
    print("Print Book Data")
    print(">>>", genre)
    print(">>>", author)
    print(">>>", year)


author = "David Brin"
title = "Glory Season"
genre = "Science Fiction"
rating = 8.5
year = 1992
bsfa_award = False
nebula_award = False
isbn_10 = "0785754318"
isbn_13 = "978-0-7857-5431-2"
asin = "B00AA2O5RW"
quick_review = "Questions society about clones and gender roles.  Has an interesting puzzle and mystery solving dynamic that I enjoyed but the ending was not fulfilling. Could have been the first book of a trilogy."


print_asterisks()

print_genre(genre)
print_author(author)
print_year(year)

print_asterisks()

print_book_data(genre, author, year)

print_asterisks()


author = "Robert Silverberg"
title = "Lord Valentine's Castle"
genre = "Fantasy"
rating = 10.0
year = 1980
bsfa_award = False
nebula_award = False
isbn_10 = "1125594047"
isbn_13 = "978-1125594049"
asin = "B01A64FH4I"
quick_review = "Was initially a trilogy then spawned another trilogy on the same planet at a different time.  Follow a juggler as he finds out he's Coronal and brings his world of Majipoor together. Great word salad terms yet you remain capitvated by the story and wish you could visit. "

print_genre(genre)
print_author(author)
print_year(year)

print_asterisks()

print_book_data(genre, author, year)

print_asterisks()


author = "Kim Stanley Robinson"
title = "Red Mars"
genre = "Hard Science Fiction"
rating = 9.5
year = 1992
bsfa_award = True
nebula_award = True
isbn_10 = "0553560735"
isbn_13 = "978-0553560732"
asin = "B00HS7LI4A"
quick_review = "Best novel on human colonization of Mars.  Gives a real sense of what it would take technically, the politics of environment, all in a realistic future.  Trilogy with Green Mars, Blue Mars."

print_genre(genre)
print_author(author)
print_year(year)

print_asterisks()

print_book_data(genre, author, year)

print_asterisks()

# Show default
print_book_data()

print_asterisks()
