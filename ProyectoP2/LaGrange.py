#Caso1
points_caso1 = [19, 21, 22, 23]
values_caso1 = [998, 999.2, 999.4625, 999.5]

#Caso1
points_caso2 = [0, 10, 20, 50]
values_caso2 = [17.94, 13.10, 10.09, 12.04]

##Descripcion genereal del algoritmo utilizado
""""
1. Recibir como entrada un conjunto de puntos (points), valores (values) y 
    un punto específico (x) para el cual se desea calcular la aproximación de la función.
2. Inicializar una variable para almacenar el valor de la aproximación (Px) 
    y otra para almacenar la expresión polinómica (P).
3. Iterar sobre cada punto del conjunto (i)
4. Calcular el factor Li para el punto actual, que se basa en los puntos 
    restantes del conjunto (j) y en el punto específico (x) para el cual 
    se está calculando la aproximación.
5. Actualizar el valor de Px sumando el producto de Li y el valor 
    correspondiente del punto (values[i]).
6. Actualizar la expresión polinómica P con el término correspondiente al punto actual.
7. Retornar el valor de Px y la expresión polinómica P.
"""

def Lagrange_interpolation(points, values, x):
    n = len(points)
    Px = 0
    P = ""
    for i in range(n):
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (x - points[j])/(points[i] - points[j])
        Px += Li * values[i]
        if i == 0:
            P = f"{Li * values[i]}"
        else:
            P += f" + ({Li * values[i]})*x^{i} "
    return Px, P