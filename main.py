# Manejo de archivos de texto en Python: permite, desde el código, crear, abrir, leer, editar archivos de texto
print("Manejo de archivos de texto en python y uso de métodos")

# Abriremos nuestro primer archivo, como este aún no está creado, basta con usar la función open, que sirve para abrir un archivo, y no existe, en su defecto, crearlo
print("\n- Creación del archivo: 'primerarchivo.txt'")
import files

# La función open recibe dos valores: el primero es el referente al nombre del archivo, y el segundo se trata de la modalidad en que se desea abrir tal archivo, es decir, en modo lectura, modo escritura, escritura al final del archivo, o combinar los anteriormente mencionados

# Abriremos el archivo de texto en el modo 'w', de escritura
print("\n- Abrir archivo en modo escritura")
# 'primerarchivo.txt' lo abriremos en primera instancia con el permiso de escribir y allí dejaremos un primer mensaje
my_file = open('primerarchivo.txt', 'w')

# Localización del comento creado previamente
print("\nEn files (a la izquierda), ya puede visualizarse el documento y el mensaje")

# Para  dejar un mensaje, utlizamos el método write()
my_file.write("¡Bienvenidos! A este primer archivo de texto creado desde la plataforma replit apartir de código en Pyhton")
my_file.write("\nEste archivo será entretenido, pues aquí, contaremos historias...")
my_file.write("\nComencemos")

# Uso del write()
print("\nAquí utilizamos el método write()")

# Es una buena práctica cerrar el archivo, para evitar que este pueda ser modificado sin autorización previa
my_file.close()

print()
print("---------"*8)

# Abriremos el archivo en el modo 'r', de lectura
print("\n- Abrir archivo en modo lectura")
# De esta otra forma, podemos abrir el archivo en modo lectura, es decir, no se permitirán modificaciones
my_file = open('primerarchivo.txt', 'r')

# Imprimiremos el texto que hemos creado con write()
print("\nTexto")
print(my_file.read())

# Cerraremos el archivo
my_file.close()

# Entraremos de nuevo al archivo para observar algunos métodos que podemos aplicar
my_file = open('primerarchivo.txt', 'r')

# read(): permite indicar la cantidad de bytes del mensaje que queremos mostrar. Si lo indicamos vacio o con -1, se mostrará todo el texto
print("\nMétodo read():")
print("\n52 bytes del texto")
print(my_file.read(52))

# readline(): retorna una linea del archivo
print("\nMétodo readline():")
print(my_file.readline())

# readable(): retorna True si el texto es legible, es decir, se deja leer; por el contrario, retornará False
print("\nMétodo readable():")
print(my_file.readable())

# readlines(): retorna una lista que contiene cada línea del archivo como un elemento de la misma
print("\nMétodo readlines():")
print(my_file.readlines())

# Anotación
print("\nPudimos observar que usando los diferentes métodos de read, en cada uno, se imprimió una línea diferente del texto, en orden, hasta abarcarlo todo")

# Cerramos el archivo
my_file.close()

print()
print("---------"*8)

# Abriremos el archivo en la modalidad 'a', escritura al final del archivo
print("\n- Abrir archivo en modo escritura, al final del archivo")
# Abriremos el archivo, agregaremos unas cuantas líneas de texto que irán al final de este
my_file = open('primerarchivo.txt', 'a')

# writable(): retornará True si el archivo es escribible, se deja escribir y agregar líneas; por lo contrario, retornará False. Puede retornar False, si se cierra el archivo antes de llamar este método
print("\nMétodo writable():")
print(my_file.writable())

# Cerramos el archivo
my_file.close()

print("\nAñadimos texto con write()")
# Añadimos la línea
my_file = open('primerarchivo.txt', 'a')
my_file.write(" ")
my_file.write("\nEsta es una historia, nunca antes contada.")

# Mostrar el texto después de agregar una nueva linea
my_file = open('primerarchivo.txt', 'r')
print(my_file.read())

# Cerramos el archivo
my_file.close()

# Agregatremos otra línea de texto con el método writelines
my_file = open('primerarchivo.txt', 'a')

# writelines(): se introducen nuevas lineas al texto, usando el formato de la lista
print("\nMétodo writelines():")
my_file.writelines([" Es posible que hayan historias parecidas,", " pero ninguna como esta."])
my_file.close()

# Mostrar el texto después de agregar más texto
my_file = open('primerarchivo.txt', 'r')
print(my_file.read())

# Cerramos el archivo
my_file.close()

# Existe un método llamado truncate(), que modifica el tamaño del archivo de texto, esto provoca que el texto quede modificado del todo, y porque seguiremos aplicando más métodos para leer, no lo aplicaremos

print()
print("---------"*8)

# Abriremos de nuevo el archivo en modo lectura para ver otros métodos
print("\n- Abrir archivo en modo lectura")
my_file = open('primerarchivo.txt', 'r')

# fileno(): retorna el número de líneas que va ocupando el texto según la forma en que se ingresaron 
print("\nMétodo fileno():")
print(my_file.fileno())

# tell(): devuelve la posición del archivo de texto en una secuencia de archivos
print("\nMétodo tell():")
print(my_file.tell())

# seekable(): retorna True si el archivo se puede buscar: en caso contrario, retornará True
print("\nMétodo seekable():")
print(my_file.seekable())

# seek(): reubicar el puntero para encontrar alguna parte específica del texto
print("\nMétodo seek():")
my_file.seek(128)
print(my_file.readline())

# Cerramos el archivo
my_file.close()
