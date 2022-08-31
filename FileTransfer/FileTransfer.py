import os
import shutil
from time import sleep as wait

# VARIABLE EN UN ARCHIVO .TXT

with open("Extension_List.txt", "r") as extension_list:
	for linea in extension_list:
		None
	os.system("cls")

# with open("cmdtransfer.py", encoding="utf-8") as cmdtransfer:
# 	for linea in cmdtransfer:
# 		None
# 	os.system("cls")

wait(1.5)

menu = ("""

			    ______ _ _        _                        __          
			   |  ____(_) |      | |                      / _|         
			   | |__   _| | ___  | |_ _ __ __ _ _ __  ___| |_ ___ _ __ 
			   |  __| | | |/ _ \ | __| '__/ _` | '_ \/ __|  _/ _ \ '__|
			   | |    | | |  __/ | |_| | | (_| | | | \__ \ ||  __/ |   
			   |_|    |_|_|\___|  \__|_|  \__,_|_| |_|___/_| \___|_|   
				                                                         
            					Created by Unkown         


        """)


menu2 = (""" We need information about your directories, please response these questions...
""")


print(menu)
wait(2.5)

print(menu2)
wait(0.5)

# ASIGNACION DE VARIABLES

var_user = input(" [1] - What is your user`s name: ")
var_download_folder = input(" [2] - What is the folder`s name where are all files: ")
var_back_folder = input(" [3] - The folder`s name where want to be the folders? (Ej: Desktop, Documents, Music): ")
var_encripted = input(" [4] - The folder`s name where encripted files will be trasnfered: ")
var_photos = input(" [5] - The folder`s name where photos will be trasnfered: ")
var_setup = input(" [6] - The folder`s name where set ups files will be trasnfered: ")
var_others = input(" [7] - The folder`s name where the rest of files will trasnfer: ")


descargas = f"C:/Users/{var_user}/{var_download_folder}/"
documentos = f"C:/Users/{var_user}/{var_back_folder}/"
filetransfer = f"C:/Users/{var_user}/{var_back_folder}/FileTransfer/"
encriptados = f"C:/Users/{var_user}/{var_back_folder}/{var_encripted}/"
fotos = f"C:/Users/{var_user}/{var_back_folder}/{var_photos}/"
setup = f"C:/Users/{var_user}/{var_back_folder}/{var_setup}/"
otros = f"C:/Users/{var_user}/{var_back_folder}/{var_others}/"

# VERIFICACION DE LAS VARIABLES ANTERIORES

menu3 = f"""
 Before we do anything, let's check if the selected directories are correct.

 [1] - User -> {var_user}
 [2] - Disorder folder -> {descargas}
 [3] - Main folder -> {documentos}
 [4] - Encripted folder -> {encriptados}
 [5] - Gallery folder -> {fotos}
 [6] - Setup folder -> {setup}
 [7] - Leftovers folder -> {otros}

"""

print(menu3)

#  PRIMER TRANSLADO DE ARCHIVOS

if __name__ == "__main__":

	for filename in os.listdir(descargas):

		name, extension = os.path.splitext(descargas + filename)

		if extension in [".rar", ".iso", ".zip"]:
			os.rename(descargas + filename, documentos + filename)

		elif extension in [".exe"]:
			os.rename(descargas + filename, documentos + filename)

		elif extension in [".mp4", ".mov", ".wmv", ".avi", ".avchd", ".flv", ".mkv", ".webm", ".mp3", ".png", ".bmp", ".jpg", ".tif"]:
			os.rename(descargas + filename, documentos + filename)

		elif extension in [extension_list]:
			os.rename(descargas + filename, documentos + filename)

	# Crear los archivos y transladarlos a Documentos

	#Creacion de carpetas

	os.mkdir(var_encripted)
	os.mkdir(var_photos)
	os.mkdir(var_setup)
	os.mkdir(var_others)

	#Translado de carpetas

	shutil.move(var_encripted, documentos)
	shutil.move(var_photos, documentos)
	shutil.move(var_setup, documentos)
	shutil.move(var_others, documentos)

	wait(5)

	# SEGUNDO TRANSLADO DE ARCHIVOS >> DOCUMENTOS -> CARPETAS 

	for filename in os.listdir(documentos):

		name, extension = os.path.splitext(documentos + filename)

		# VARIABLES MKDIR/CARPETA

		if extension in [".rar", ".iso", ".zip"]:
			os.rename(documentos + filename, encriptados + filename)

		elif extension in [".exe"]:
			os.rename(documentos + filename, setup + filename)

		elif extension in [".mp4", ".mov", ".wmv", ".avi", ".avchd", ".flv", ".mkv", ".webm", ".mp3", ".png", ".bmp", ".jpg", ".tif"]:
			os.rename(documentos + filename, fotos + filename)

		elif extension in [extension_list]:
			os.rename(documentos + filename, otros + filename)
