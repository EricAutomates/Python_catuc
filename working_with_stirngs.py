#working with strings 

first_name = "ngwa"
last_name ="jude"
print (first_name.upper()) # turn to uppercase 
print ( last_name.title()) # adds first letter as title
food = "RICE"
print(food.lower())
print (food[2])
count = len(food)
print(count)
#long ahh string
languages ="\n\nPython\nC\nJava\nC++"
print(languages)

#char
character = 'j'
if character in last_name:
    print(f"the letter {character} exist in {last_name}")