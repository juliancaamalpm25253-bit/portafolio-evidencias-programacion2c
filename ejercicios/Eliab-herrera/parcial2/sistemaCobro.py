# Función para calcular el subtotal
def calcular_subtotal(precio, cantidad):
    return precio * cantidad
"""
calcular_subtotal

parametros:
precio(float):precio unitario del producto
cantidad(int):cantidad comprada

retorna:
float:subtotal de la compro
"""

# Función para calcular el descuento
def calcular_descuento(subtotal):
    if subtotal > 1000:
        descuento = subtotal * 0.10
        print(f"Se aplicó un descuento del 10%: -${descuento:.2f}")
        return descuento
    return 0

# Función para calcular el IVA
def calcular_iva(subtotal_con_descuento):
    return subtotal_con_descuento * 0.16
"""
calcular el IVA

parametros:
subtotal_con_descuento (float):subtotal del descuento

retorna:
float:monto del descuento aplicado
"""
# Función para calcular el total final
def calcular_total(subtotal_con_descuento, iva):
    return subtotal_con_descuento + iva

# Función para imprimir el ticket
def imprimir_ticket(producto, subtotal, iva, total):
    """
    imprime el tiket de compra

    parametros:
    producto (str):nombre del producto
    subtotal (float)
    iva (float)
    total(float)

    retorna.:
    none
    """
    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("----------------------")



# Función principal
def main():
    """
    controlar el flujo del programa completo
    permite realizar multiples cobros sin repetir codigo
    """
    print("--- Sistema de Cobro v1.0 ---")
    
    producto = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    
    subtotal = calcular_subtotal(precio, cantidad)
    descuento = calcular_descuento(subtotal)
    subtotal_con_descuento = subtotal - descuento
    iva = calcular_iva(subtotal_con_descuento)
    total = calcular_total(subtotal_con_descuento, iva)
    
    imprimir_ticket(producto, subtotal, iva, total)

# Ejecutar el programa
if __name__ == "__main__":
    main()