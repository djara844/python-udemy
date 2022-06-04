pago = float(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione el monto del impuesto: '))


def calculadora_de_impuestos(pago, impuesto):
    pago_total = pago + pago * (impuesto / 100)
    return pago_total


pago_con_impuesto = calculadora_de_impuestos(pago, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')
