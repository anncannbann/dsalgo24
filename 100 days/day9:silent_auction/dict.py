programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                           "Function": "A piece of code that you can easily call over and over again."}



print(programming_dictionary['Function'])

programming_dictionary['New'] = "something something"



#print(programming_dictionary['New'])


programming_dictionary['New'] = "something s"

#print(programming_dictionary)


for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

travel_log = {
  "France": {"visited":["Paris", "Lille", "Dijon"],"total": 23},
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

travels ={

}
#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5
}
]