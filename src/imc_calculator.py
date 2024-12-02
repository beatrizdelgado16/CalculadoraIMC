def calculate_imc(weight, height):
    """Calcula o Índice de Massa Corporal (IMC) dado o peso e altura."""
    if height <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    return weight / (height ** 2)
