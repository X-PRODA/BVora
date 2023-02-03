from os import remove
a = 0
l = 0
while a == 0:
    o = input("--create//-/-//open//-/-//delete--  ")
    if o == "create":
        n = input("name - ")
        open("proyects/" + n + ".bv", "x")
        a = a + 1
    elif o == "open":
        n = input("name - ")
        f = open("proyects/" + n + ".bv", "r")
        print(f.read())
        a = a + 1
    elif o == "delete":
        n = input("name - ")
        remove("proyects/" + n + ".bv")
    elif o == "config":
        n = input("configuration - ")
        f = open("changefiles/" + n, "r")
        print(f.read())
        f = open("changefiles/" + n, "w")
        f.write(input("texto - "))
    elif o == "funtions":
        f = open("changefiles/funtions", "r")
    else:
        print("I don't understand you. Can yo repeat?")
while True:
    l = l + 1
    f = open("proyects/" + n + ".bv", "a")
    f.write(input(str(l) + " - "))
    f.write("\n")
    f.close()
