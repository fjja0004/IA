class Alumno:
    def __init__(self, nombre, apellido, dni, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_dni(self):
        return self.__dni

    def get_correo(self):
        return self.__correo

    @staticmethod
    def crea_alumno(self):
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        correo = input("Correo: ")
        return Alumno(nombre, apellido, dni, correo)

    def muestra_alumno(self):
        print("Datos del alumno:")
        print("Nombre: " + self.get_nombre())
        print("Apellido: " + self.get_apellido())
        print("DNI: " + self.get_dni())
        print("Correo: " + self.get_correo())


class AlumnoIA(Alumno):
    def __init__(self, nombre, apellido, dni, correo, grupoT, grupoP, lista_notas=None):
        Alumno.__init__(self, nombre, apellido, dni, correo)
        self.__grupoT = grupoT
        self.__grupoP = grupoP
        self.__lista_notas = lista_notas

    def get_grupoT(self):
        return self.__grupoT

    def get_grupoP(self):
        return self.__grupoP

    def get_lista_notas(self):
        return self.__lista_notas

    def nuevas_notas(self):
        notas = []
        notas.append(int(input("Nota de la practica 1: ")))
        notas.append(int(input("Nota de la practica 2: ")))
        notas.append(int(input("Nota de la practica 3: ")))
        notas.append(int(input("Nota de la practica 4: ")))
        self.__lista_notas = notas

        suma = 0
        for nota in notas:
            suma = suma + nota
        print("La media de la practica es: " + str(suma / 4))


def main():
    nombre_fichero = "datos1.txt"
    modo = "rt"
    alumnos_impares = []

    fichero = open(nombre_fichero, modo)
    lista_fichero = fichero.readlines()
    fichero.close()

    for linea in lista_fichero:
        lista_linea = linea.strip().split(",")
        dni = int(lista_linea[1])
        if dni % 2 == 1:  # El alumno tiene un dni impar
            alumnos_impares.append(linea)

    nombre_fichero = "impares.txt"
    modo = "wt"
    fichero = open(nombre_fichero, modo)
    fichero.writelines(alumnos_impares)
    fichero.close()


main()
