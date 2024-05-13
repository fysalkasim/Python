motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append("ducati")  #Using append method
print(motorcycles)
motorcycles.insert(2,"hero")  #using insert method
print(motorcycles)
#Removing an Item Using the del Statement
del motorcycles[2]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)