from pulp import *

# Crear problema
prob = LpProblem("Videojuegos", LpMaximize)

# Variables
x = LpVariable("Personajes", lowBound=0)
y = LpVariable("Escenarios", lowBound=0)

# Función objetivo
prob += 80*x + 60*y

# Restricciones
prob += 2*x + y <= 12
prob += x + 2*y <= 14

# Resolver
prob.solve()

# Resultados
print("Estado:", LpStatus[prob.status])
print("Personajes =", value(x))
print("Escenarios =", value(y))
print("Valor máximo =", value(prob.objective))