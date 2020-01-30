students = {
    "male":["Ade", "Sunkanmi", "Kunle", "Wale", "Feyi"],
    "female":["Ada", "Funke", "Bimpe", "Seyi", "Aramide"]

    }
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
    
