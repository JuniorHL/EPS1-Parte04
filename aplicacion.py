# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:20:34 2022

@author: Cosme
"""

import metodos

def menu():
    print("\n\n*************MENU************\n"+
          "1. Listar Personas\n"+
          "2. Agregar Personas\n"+
          "3. Salir\n")

    opcion = int(input("\n Elija una opcion: "))
    return opcion



def leerArchivo(nombre):
    archivo = open(nombre, "rt", encoding = "utf8")
    contenido = archivo.read()
    contenido = contenido.split('\n')
    return contenido




LoginUsuario = leerArchivo('login.txt')
claveUsuario = leerArchivo('clave.txt')

bandera = True
contador = 0

while bandera == True:
    usuario = input('Ingresa el usuario: ')
    clave = input('Ingresa la clave: ')

    if contador == 2: 
        print('\n Pasaste el limite de intentos')
        bandera = False
    
    opcion=1

    for usuarioItem in LoginUsuario:
        if usuario == usuarioItem:
            for claveoItem in claveUsuario:
                if clave == claveoItem:
                    bandera = False
                    while opcion!=3:
                     opcion = menu()
                     if opcion == 1:
                         metodos.listar_personas()
                     if opcion == 2:
                         metodos.agregar_personas()
                     if opcion == 3:
                         metodos.salir()
                     if opcion<1 or opcion>3:
                        print("Opción inválida")


    if bandera == True:
        print('Usuario y/o contraseña errada')
        contador = contador + 1 
    
    print('\n ')
    
    
