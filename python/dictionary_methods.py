#dictionary methods
student = {
    "name" : "ajithreddy",
    "roll_no" : 21,
    "marks" : 16.6
}
print(len(student)) #no.of keys
print(student.keys()) #dict_keys
print(student.values()) #dict_values
print(student.items()) #to get key:value pairs
print(student.get("name"))