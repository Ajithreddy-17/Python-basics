#Dictionary are key value pairs
info ={
    "key" : "value",
    "name" : "ajith",
    "learning" : ["python","java","c"],
    "age" : 35,
    "marks" : 78.6,
    }
info["name"] = "ajithreddy"
print(info["name"]) #muttbale
print(info["learning"])
 
#nested dictionary
student = {
    "peru" : "maanas",
    "subject" : {
        "phy" : 77,
        "che" : 88,
        "eng" : 22,
    }
}
print(student["subject"]["che"])