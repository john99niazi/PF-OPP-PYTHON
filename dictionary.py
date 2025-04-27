#dictionary    type

'''car={"brand":"honda","MODEl":"2005","price":"900000RS"}
print(car)
print(type(car))'''


#bulit in funcation (((get))))
car={"brand":"honda","model":"2006","price":"222222","milge":"0"}
print(car.get("price"))

#print all funcation of keys
print(car.keys())

#printing all value of dicitionary
print(car.values())

###update key valued
car["brand"]="BMW"
car["model"]="2005"
print(car)

#add new key to the existing dictionary
car["type"]="aucation"
print(car)

#for each loop keys,valued
for k in car:
    print(k)

for k in car.keys():
    print(k,car.get(k))

for v in car.values():
    print(  v)

#pop key  delte key
car.pop("brand")
print(car)


del car["price"]

print(car)


#removimg last item in dicitionary
car.popitem()
print(car)

#length of tdicitionary and clear the dicitionary 


print(len(car))


#comaparing ditionary == , !=
b={"name":"junaid","car_name":"honda"}
print(car==b)