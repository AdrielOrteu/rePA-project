from contents import Movie, Book
from ratings import SimpleRating, CollaborativeRating

chosen_db = input("Do you want to view movies (m) or books (b)?\n")
if chosen_db == "m":
    content = Movie()
elif chosen_db == "b":
    content = Book()
else:
    raise ValueError
content.load_content()
print(content.content_dict)

chosen_ratings = input("Which rating method do you prefer? (simple s, collaborative c)\n")
if chosen_ratings == "s":
    pass
elif chosen_ratings == "c":
    pass
else:
    raise ValueError

