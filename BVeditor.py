o = input("--crear//-/-//abrir--  ")
a = 0
l = 0
while a == 0:
    if o == "crear":
        n = input("nombre")
        open("proyectos/" + n + ".bv", "x")
        a = a + 1
    elif o == "abrir":
        n = input("nombre")
        f = open("proyectos/" + n + ".bv", "r")
        print(f.read())
        a = a + 1
    else:
        print("No le he entendido")
l = l + 1
f = open("proyectos/" + n + ".bv", "a")
f.write(input(str(l) + " - "))
f.close()
while True:
    l = l + 1
    f = open("proyectos/" + n + ".bv", "a")
    f.write("/n" + input(str(l) + " - "))
    f.close()
