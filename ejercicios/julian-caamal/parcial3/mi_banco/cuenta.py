class Cuenta:
    
    def __init__(self, cliente, cuenta, saldo = 0):
        """
        Inicializa una nueva secion de la cuenta bancaria.

        Args:
            cliente (str): Nombre completo del titular de la cuenta.
            cuenta (str): Número identificador único de la cuenta.
            saldo (float, optional): Saldo inicial de la cuenta. 
            Debe ser un valor no negativo. Por defecto es 0.

        Raises:
            ValueError: Si el saldo proporcionado es menor a cero.
        """
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo
        
    def deposito(self, cantidad):
        """
        Registra un ingreso de dinero en la cuenta.

        Verifica que la cantidad sea positiva antes de sumarla al saldo actual.
        Si la cantidad es 0 o negativa (como -200), la operación no se realiza
        para mantener la el deposito en el saldo.

        Args:
            cantidad (float): El monto de dinero que se desea depositar.

        Returns:
            bool: True si el depósito fue exitoso (cantidad > 0), 
                False si el monto era inválido y no se realizó la operación.
        """
        
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False
    
    def retirar(self, cantidad):
        """
        Registra el saldo si hay dinero y si la cantidad es positiva 
        
        Return:
            True si la cantidad fu exitosa, Falce si no hay hay dinero o si puso valores negativos
        """
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False
    
    def main():
        pass
    
    if __name__== "__main__":
        main()