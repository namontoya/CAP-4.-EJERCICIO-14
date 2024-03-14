#Capitulo 4. Ejercicio resuelto 14

VD1 = float(input('Ingrese las ventas del departamento 1: '))
VD2 = float(input('Ingrese las ventas del departamento 2: '))
VD3 = float(input('Ingrese las ventas del departamento 3: '))
SALAR = float(input('Ingrese el salario de los vendedores: '))

TOTVEN = VD1 + VD2 + VD3
PORVEN = TOTVEN * 0.33

if VD1 > PORVEN:
  SALAR1 = SALAR + 0.2 * SALAR
else:
  SALAR1 = SALAR

if VD2 > PORVEN:
  SALAR2 = SALAR + 0.2 * SALAR
else:
  SALAR2 = SALAR

if VD3 > PORVEN:
  SALAR3 = SALAR + 0.2 * SALAR
else:
  SALAR3 = SALAR

print(f"SALARIO VENDEDORES DEPTO 1 {SALAR1}, SALARIO VENDEDORES DEPTO 2 {SALAR2}, SALARIO VENDEDORES DEPTO 3 {SALAR3}")
