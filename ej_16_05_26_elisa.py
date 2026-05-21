import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Ensamble_Computadoras", pulp.LpMaximize)

# 2. Definir Variables
# x1 = Computadoras de Escritorio
# x2 = Laptops

x1 = pulp.LpVariable("Escritorios", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Laptops", lowBound=0, cat='Integer')

# 3. Función Objetivo
# Maximizar ganancias
model += 2000 * x1 + 4000 * x2, "Ganancia_Total"

# 4. Restricciones

# Restricción de microprocesadores
model += x1 + x2 <= 60, "Procesadores_Disponibles"

# Restricción de horas de trabajo
model += 1 * x1 + 3 * x2 <= 100, "Horas_Disponibles"

# 5. Resolver y mostrar resultados
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Computadoras de Escritorio: {x1.varValue}")
print(f"Laptops: {x2.varValue}")
print(f"Ganancia Máxima: ${pulp.value(model.objective)} MXN")

#source .venv/bin/activate
