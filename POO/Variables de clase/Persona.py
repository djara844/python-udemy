class Persona:
    contado_personas = 0

    def __init__(self, nombre, edad):
        Persona.contado_personas += 1
        self.id_persona = Persona.contado_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona {self.id_persona} {self.nombre} {self.edad}'

persona1 = Persona('Juan', '32')

print(persona1)