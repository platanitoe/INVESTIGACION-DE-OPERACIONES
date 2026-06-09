from pulp import *

# Crear problema
prob = LpProblem("Almacenamiento", LpMinimize)

# Variables
x = LpVariable("Estandar", lowBound=0)
y = LpVariable("Premium", lowBound=0)

# Función objetivo
prob += 20*x + 60*y

# Restricciones
prob += x + 3*y >= 15
prob += x + y >= 7

# Resolver
prob.solve()

# Resultados
print("Estado:", LpStatus[prob.status])
print("TB Estandar =", value(x))
print("TB Premium =", value(y))
print("Costo mínimo =", value(prob.objective))