import time as tm
import tkinter as tk
import os
import random as rd
d = open("changefiles/intext.bvm", "r")
print(d.read())
def evr(iterable):
    all(iterable)
def ning(iterable):
    any(iterable)
def crear(titulo, extensión):
    e = open(titulo + "." + archivo, "x")
def codificar(archivo, codificacion):
    e = open(archivo, "rb")
    f = open(archivo, "wb")
    f.write(e.read() * (10 ** codificacion))
def codavanze(archivo, num1, num2):
    e = open(archivo, "rb")
    f = open(archivo, "wb")
    num = rd.randint(10 ** (num1 ** num2)/num1 - num2)
    f.write(e.read() * num)
    open("key.txt", "x")
    q = open("key.txt", "w")
    g.write(num)
    g.close()
def decodeavanze(archivo):
    e = open("key.txt", "r")
    f = open(archivo, "wb")
    g = open(archivo, "rb")
    f.write(g.read() / e.read())
    f.close()
def decode(archivo, codificación):
    f = open(archivo, "wb")
    g = open(archivo, "rb")
    f.write(g.read() / (10 ** codificación))
    f.close()
def out(string):
    print(string)
def inp(string):
    return input(string)
def ejec(comando):
    os.system(comando)
a = open("proyects/" + input("archivo - ") + ".bv", "r")
exec(a.read())
c = open("changefiles/endtext.bvm", "r")
print(c.read())
tm.sleep(3)
