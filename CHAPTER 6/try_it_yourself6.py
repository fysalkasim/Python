fav_num = {
    "Fysal":[3005,3008],
    "Abin": [2509,2805],
    "Gokul":[606,2001],
    "Haritha":[407,2000]
}
print(fav_num)
for name,nums in fav_num.items():
    print(f"The {name}'s favorite numbers are")
    for num in nums:
        print(f"{num}")

cities = {
    "London":{
        "Country": "UK",
        "Famous for":"Big ben"
        },
    "Tokyo":{
        "Country": "JAPAN",
        "Famous for": "Technological advancement"
            },
    "Delhi":{
        "Country":"INDIA", 
        "Famous for":"POLLUTION"
        },
}

for name,infos in cities.items():
    print(f"\n {name.title()} ")
    country = infos["Country"]
    famous = infos["Famous for"]           
    print(f"in {country},{name} is famous for {famous}")


# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range (30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Show the first 5 aliens.
for alien in aliens[:5]:
 print(alien)
print("...")