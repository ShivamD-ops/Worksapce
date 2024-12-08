list1 = ["Tiger", "Lion", "Jackal", "Bear"]
for item in list1:
    print(f'{item} ')

#2
for item in list1:
    print(f'{item} len=> {len(item)}')

dict1 = {
    "Tiger":"India",
    "Lion":"Africa",
    "Jackal": "South America",
    "Bear": "Russia"
}
for i in dict1:
    print(f'{i}->{dict1[i]}-len->{len(i)}')