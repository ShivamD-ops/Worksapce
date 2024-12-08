to_copy = 0
with open('car.jpg','rb') as image_file:
    content = image_file.read()
    to_copy = content
    print(content)
    print(len(content))
with open('car_new.jpg','wb') as image_file:
    image_file.write(to_copy)
with open('car_new.jpg','rb') as image_file:
    content = image_file.read()
    print(content)
    print(len(content))