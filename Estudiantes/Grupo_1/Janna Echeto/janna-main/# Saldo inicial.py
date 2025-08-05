# Saldo inicial
saldo_final = 500
print(f"Saldo inicial: ${saldo_final}")

# 1. depositar(200)
saldo_final += 200
print(f"Después de depositar 200: ${saldo_final}")

# 2. retirar(800)
# Asumiendo una resta directa sin validación de saldo negativo para este análisis
saldo_final -= 800
print(f"Después de retirar 800: ${saldo_final}")

# 3. retirar(700)
saldo_final -= 700
print(f"Después de retirar 700: ${saldo_final}")

print(f"\nEl valor final del saldo es: ${saldo_final}")