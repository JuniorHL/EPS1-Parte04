# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:50:55 2022

@author: Joel Alanya
"""

def listar_personas():
    nom = open("nombre.txt", "r")
    ap = open("apellido.txt", "r")
    dn = open("dni.txt", "r")
    print("\n----Lista de Personas----\n")
    print("\n***Nombre   --   Apellido   --   Dni***\n")
    while(True):
     nombre = nom.readline()
     apellido = ap.readline()
     dni = dn.readline()
     nombre=nombre.strip('\n')
     apellido=apellido.strip('\n')
     dni=dni.strip('\n')
     print ("{:<15} {:<15} {:<10}".format(nombre,apellido,dni))
     if not nombre:
       break
    
    

def agregar_personas():
    newNombre = input("Nombre: ")
    archivoNombre = open("nombre.txt","at")
    archivoNombre.write("\n"+ newNombre)
    newApellido = input("Apellido: ")
    archivoApellido = open("apellido.txt","at")
    archivoApellido.write("\n"+ newApellido)
    newDni = input("Dni: ")
    archivoDni = open("dni.txt","at")
    archivoDni.write("\n"+ newDni)
    archivoNombre.close()
    archivoApellido.close()
    archivoDni.close()

def salir():
    print("Buen Parcial")