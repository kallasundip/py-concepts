'''
    --- we can store information in key, value pairs
    --- we get the value by using key
    --- key value is not availabel in list we can print user defined value
    ---  we can new key and value to the list
    ---

'''


customer = {
    "name" : "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
customer["birth_date"] = "01-aug-1990"
print(customer["birth_date"])
print(customer.get("birth_data", "Birth data is not avalible in the list"))


phone = input("Phone: ")
digits_maping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"

}
output=""
for ch in phone:
    output += digits_maping.get(ch, "!") + " "
print(output)

