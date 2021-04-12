hw = "Hello, World!"
print(hw)

number = 13
print(number + 13)

print(f"{hw} {number}")

names = ["Kahwi", "Lebron", "Giannis"]

print(f"Hello, {names[2]}")
names.append("Federer")
print(f"names after we appended Federer{names}") #Or use comments
names.reverse()
print(f"names after we reverse names {names}")
names.clear()
print(f"names after we clear {names}")

#count(), extend(), pop(), remove()

tennis = ["Roger", "Rafeal", "Dojo"]
for i in range(3):
    print(f"Hello {tennis[i]}")

namesandnumbers = ("Kahwi", 2, "Lebron", 23, "Giannis", 34, "Kahwi")
print(namesandnumbers)

clount = namesandnumbers.count("Kahwi")
twoindex = namesandnumbers.index(2)
print(f"Number of elements in namesandnumbers:{clount} Position of Two: {twoindex}")
