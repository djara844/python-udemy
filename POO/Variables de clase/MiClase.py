class MiClase:

    variable_clase = "Valor variable de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # Métdodo estático
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # Método clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

