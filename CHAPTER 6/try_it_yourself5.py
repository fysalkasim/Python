fysal = {
    "First Name": "Fysal",
    "Last Name": "Kasim",
    "Age":24,
    "Place":"Karunagappally",
}

faayiz = {
    "First Name": "Faayiz",
    "Last Name": "Kasim",
    "Age":27,
    "Place":"Mynagappally",    
}
peoples = [fysal,faayiz]
for people in peoples:
    print(people)

fav_places = {
    "Fysal":["kozhikkodu","Idukki","Ernakulam"],
    "Faayiz":["Idukki","Kollam","Kannur"]
}

for k,v in fav_places.items():
    print(f"\n{k.title()}'s favourite places are")
    for i in v:
        print(f"\t{i.title()}")
