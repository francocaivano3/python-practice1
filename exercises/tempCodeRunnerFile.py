Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno no tiene examenes aprobados.
Restricción: Utilizar el método any
"""

notas = [False, False, False, False, False, False, False, False, False]

# COMPLETAR - INICIO
no_tiene_examenes_aprobados = any(notas)
print(no_tiene_examenes_aprobados)
# COMPLETAR - FIN

assert no_tiene_examenes_aprobados
