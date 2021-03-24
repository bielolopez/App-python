from Base import Base

class Libro(Base):
	def __init__(self, nombre: "", anio = 0):
		self.__nombre = nombre
		self.__anio = anio

	@property
	def nombre(self):
		return self.__nombre
	@property
	def anio(self):
		return self.__anio
	@nombre.setter
	def nombre(self, nuevo_nombre):
		self.__nombre = nuevo_nombre
	@anio.setter
	def anio(self, nuevo_anio):
		self.__anio = nuevo_anio


# Los siguientes métodos usan los set y los get no los atributos.

	def __str__(self):
		return "Nombre del Libro: %s\nAño %i" % (self.nombre, self.anio)

	def Captura(self):
		self.nombre = input("Nombre del Libro")
		self.anio = int(input("Año del Libro"))

#  Los dos métodos están sobrecargados porque están en la clase base.





