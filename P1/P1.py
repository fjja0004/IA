

class Alumno:
    def __init__(self, nombre, apellido, dni, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__correo = correo

    def getnombre(self):
        return self.__nombre
    def getapellido(self):
        return self.__apellido
    def getdni(self):
        return self.__dni
    def getcorreo(self):
        return self.__correo

    def creaAlumno(self):
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        correo = input("Correo: ")
        return Alumno(nombre, apellido, dni, correo)

    def muestraAlumno(self):
        print("Datos del alumno:")
        print("Nombre: " + self.getnombre())
        print("Apellido: " + self.getapellido())
        print("DNI: " + self.getdni())
        print("Correo: " + self.getcorreo())


class AlumnoIA(Alumno):
    def __init__(self, nombre, apellido, dni, correo, grupoT, grupoP, listanotas):
        Alumno.__init__(self, nombre, apellido, dni, correo)
        self.__grupoT = grupoT
        self.__grupoP = grupoP
        self.__listanotas = listanotas

    def getgrupoT(self):
        return self.__grupoT
    def getgrupoP(self):
        return self.__grupoP
    def getlistanotas(self):
        return self.__listanotas

    def nuevasNotas(self):
        notas = []
        notas.append(int(input("Nota de la practica 1: ")))
        notas.append(int(input("Nota de la practica 2: ")))
        notas.append(int(input("Nota de la practica 3: ")))
        notas.append(int(input("Nota de la practica 4: ")))
        self.listanotas = notas

        suma=0
        for nota in notas:
            suma=suma+nota
        print("La media de la practica es: " + suma/4)


def main():
    nombrefichero = "datos1.txt"
    modo = "rt"
    fichero = open(nombrefichero, modo)
    listafichero = fichero.readlines()

    for linea in listafichero:
        print(linea.strip())
        print("hoa")





main()






