o = input("--create//-/-//open--  ")
a = 0
l = 0
while a == 0:
    if o == "create":
        n = input("name - ")
        open("proyects/" + n + ".bv", "x")
        a = a + 1
    elif o == "open":
        n = input("name - ")
        with open("proyects/" + n + ".bv", "r") as f
        print(f.read())
        a = a + 1
    else:
        print("I don't understand you. Can yo repeat?")
l = l + 1
with open("proyectos/" + n + ".bv", "a") as f
f.write(input(str(l) + " - "))
f.close()
while True:
    l = l + 1
    with open("proyectos/" + n + ".bv", "a") as f
    f.write("/n" + input(str(l) + " - "))
    f.close()
