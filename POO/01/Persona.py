class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
            return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre}, {self.apellido}, {self.edad}')

    def __del__(self):
        print(f'Persona: {self._nombre}')

if __name__ == '__main__':
    persona1 = Persona('Diego', 'Jaramillo', 32)
    persona2 = Persona('Alex', 'Jaramillo', 39)
    persona1.nombre = "Carlos"
    print(persona1.nombre)