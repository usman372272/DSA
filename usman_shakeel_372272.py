spicy_foods = [
 {
 "name": "Green Curry",
 "cuisine": "Thai",
 "heat_level": 9,
 },
 {
 "name": "Buffalo Wings",
 "cuisine": "American",
 "heat_level": 3,
 },
 {
 "name": "Mapo Tofu",
 "cuisine": "Sichuan",
 "heat_level": 6,
 },
]

#1.
my_list=[]
def get_names(spicy_foods):
    for i in spicy_foods:
        my_list.append((i["name"]))
            
get_names(spicy_foods)
print(my_list)

#2.
my_list1=[]
def get_spiciest_foods(spicy_foods):
    for i in spicy_foods:
        if i["heat_level"] > 5:
            my_list1.append(i)
#3.            
get_spiciest_foods(spicy_foods)
print(my_list1)

#4.
def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        print(i["name"],"(",i["cuisine"],")","| Heat Level:",i["heat_level"]* "🌶")
    
#5.
print_spicy_foods(spicy_foods)


#6.
def get_spicy_food_by_cuisine(spicy_foods,x):
    for i in spicy_foods:
        if i["cuisine"]==x:
            print(i)
            break
                   
get_spicy_food_by_cuisine(spicy_foods,"American")

#7.
get_spicy_food_by_cuisine(spicy_foods,"Thai")

#8.
def print_spiciest_foods(spicy_foods):
    for i in spicy_foods:
        if i["heat_level"] > 5:
            print(i["name"],"(",i["cuisine"],")","| Heat Level:",i["heat_level"]* "🌶")
#9.
print_spiciest_foods(spicy_foods)

#10.
def get_average_heat_level(spicy_foods):
    count = 0
    x=0
    
    for i in spicy_foods:
        count = i["heat_level"] + count
        x=x+1

    print("average_heat_level is",count/x)


get_average_heat_level(spicy_foods)


#11.
new_spicy_food=[{'name': 'Griot','cuisine': 'Haitian','heat_level': 10}]
def create_spicy_food(spicy_foods,new_spicy_food):
    print(spicy_foods,new_spicy_food)
    
create_spicy_food(spicy_foods,new_spicy_food)


