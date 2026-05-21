import pulp

# Crear modelo
modelo = pulp.LpProblem("Firewall_Seguridad", pulp.LpMaximize)

# Variables
x1 = pulp.LpVariable("Inspeccion_Basica", lowBound=0)
x2 = pulp.LpVariable("Inspeccion_Profunda", lowBound=0)

# Función objetivo
modelo += 2*x1 + 5*x2

# Restricciones
modelo += x1 + 3*x2 <= 18
modelo += x1 + x2 <= 8

# Resolver
modelo.solve()

# Resultados
print("Estado:", pulp.LpStatus[modelo.status])

print("GB Inspección Básica:", x1.varValue)
print("GB Inspección Profunda:", x2.varValue)

print("Seguridad máxima:", pulp.value(modelo.objective))