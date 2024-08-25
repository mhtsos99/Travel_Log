# Prompt the user to input the name of the country they have visited, the number of times they have visited this country and 
# a list of cities they have visited in this country, starting with their favorite city. 
country = input("Which country have you visited and you want to add to travel_log? ") 
visits = int(input("How many times have you visited this country? ")) 
list_of_cities = eval(input("Which cities have you visited, starting with your favourite. Give them in the form of a list. ")) 

# Predefined travel log with some example entries
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# Write the function that will allow new countries to be added to the travel_log. 

def add_new_country(name, times_visited, cities_visited): 
  # Create a dictionary for the new country with its details
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  # Append the new country to the travel log
  travel_log.append(new_country) 

# Call the function to add the new country provided by the user
add_new_country(country, visits, list_of_cities)

# Print details about the newly added country
print(f"\nI've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

# Print the updated travel log
print(f"\nThe new travel log is {travel_log}.")