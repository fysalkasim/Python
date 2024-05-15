# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values
# that are returned.
def city_country(city,country):
    location = f"{city}, {country}"
    return location.title()

kochi = city_country("Kochi","India")
Delhi = city_country("Delhi","India")
London = city_country("London","India")
print(kochi)
print(Delhi)
print(London)

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.

def make_album(name,title):
    albumsong = {"Artist":name,"Song name":title}
    return albumsong
perfect = make_album("Ed sheeran","Perfect")
blank_space = make_album("Taylor Swift", "blank_space")
baby = make_album("Justin Beiber","Baby")
print(perfect)
print(blank_space)
print(baby)
def maker_album(name,title,number = None):
    albumsong = {"Artist":name,"Song name":title}
    if number:
        albumsong["Number of song"] = number 
    return albumsong
perfect = maker_album("Ed sheeran","Perfect",5)
blank_space = maker_album("Taylor Swift", "blank_space",6)
baby = maker_album("Justin Beiber","Baby")
print(perfect)
print(blank_space)
print(baby)


# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def mak_album(name,title):
    albumsong = {"Artist":name,"Song name":title}
    print(albumsong)
while True:
    print("You are welcome to album maker")
    print("\n You can type 'q' to close the application")
    nam = input("Enter the name of the artist: ")
    if nam == 'q':
        break
    song = input("Enter the song titile")
    if song == 'q':
        break
    mak_album(nam,song)