from Personas import Persona, Estudiante, EstCompu, Asistente
import os


class Lectura:
	def LeeDatosPersona(self):
		persona = Persona()
		os.system('cls')      #os.systema('cls') #en windows
		persona.Captura()
		return persona

	def LeeDatosEstudiante(self):
		estudiante = Estudiante(nombre="")
		os.system('cls')
		estudiante.Captura()
		return estudiante

	def LeeDatosEstCompu(self):
		estudianteC = EstCompu()
		os.system('cls')
		estudianteC.Captura()
		return estudianteC

	def LeeDatosAsistente(self):
		asistente = Asistente()
		os.system('cls')
		asistente.Captura()
		return asistente


