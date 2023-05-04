import os
# ver si existe el archivo
if os.path.exists("recetas.md"):
#Abrimos el archivo recetas.md
    archivo = open("recetas.md", "r")

    #Leemos el archivo
    contenido = archivo.read()

    #Imprimimos el contenido del archivo
    print(contenido)
else:
    print("El archivo no existe")