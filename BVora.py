from time import sleep
a = open(input("archivo"), "r")
b = compile(a.read(), "BV", "exec")
exec(b)
c = open("endtext.bvm", "r")
print(c.read())
sleep(3)
