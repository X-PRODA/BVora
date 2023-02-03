import time as tm
import tkinter as tk
import os
import random as rd
import socket as sk
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
def send(host, port, message):
    obj = sk.socket()
    obj.connect((host, port))
    while True:
        mens = raw_input(message)
        obj.send(mens)
        obj.close()
    return True
def recive(server, port):
    ser = sk.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser.bind((server, port))
    ser.listen(1)
    cli, addr = ser.accept()
    while True:
        recibido = cli.recv(1024)
        return str(addr[0]), str(addr[1])
        cli.send("Message recived")
    cli.close()
    ser.close()
print("Conexiones cerradas")
a = open("proyects/" + input("archivo - ") + ".bv", "r")
exec(a.read())
c = open("changefiles/endtext.bvm", "r")
print(c.read())
e = open("changefiles/enddelay.bvv", "r")
tm.sleep(int(e.read()))
