

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        
    def __str__(self):
        cadena = "Grupo de estudiantes: "+str(self._grupo)
        return cadena

    def listadoAsignaturas(self, **kwargs):
        if(self._asignaturas is None):
            lista = []
            for x in kwargs.values():
                lista.append(Asignatura(x))
            self._asignaturas = lista
        else:
            for x in kwargs.values():
                self._asignaturas.append(Asignatura(x))
        
    def agregarAlumno(self, alumno, lista=None):
        if(lista is None):
            self.listadoAlumnos = [alumno]
        else:
            lista.append(alumno)
            self.listadoAlumnos = lista
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

