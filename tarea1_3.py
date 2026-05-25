from pulp import *

# Crear problema
problema = LpProblem("Optimizacion_Contenedores", LpMaximize)

x = LpVariable("Backend", lowBound=0, cat='Integer')
y = LpVariable("DataWorker", lowBound=0, cat='Integer')

problema += 300 * x + 250 * y, "Rendimiento_Total"

problema += 2 * x + y <= 16, "Memoria_RAM"
problema += x + 2 * y <= 17, "Almacenamiento"
problema += x <= 6, "Limite_Backend"
problema += y <= 7, "Limite_DataWorker"

problema.solve()

print("Estado:", LpStatus[problema.status])


print("Contenedores Backend:", x.varValue)
print("Contenedores Data Worker:", y.varValue)

print("Rendimiento máximo: $", value(problema.objective), "USD por hora")