"""
    Program 2: Dictionary Review
    Student Name: Staci Williams
    Course: CSCI 409 D1
"""

# Use the below dictionary to answer the following questions
flight = {
    "origin": "MYR",
    "destination": "ATL",
    "aircraft": "CR9"
}

# 1. Use the get method to retrieve the aircraft being used
print(flight)

# 2. Change the aricraft from CR9 to B747
flight["aircraft"] = "B747"
print(flight)

# 3. Add the key departure with a value of "0600" to the flight dictionary
flight.update({"departure": "0600"})
print(flight)

# 4. Use the pop method to remove the aircraft from the dictionary
flight.pop("aircraft")
print(flight)

# 5. Use the clear method to empty the dictionary
flight.clear()
print(flight)