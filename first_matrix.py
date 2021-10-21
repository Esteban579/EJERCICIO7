""" lits example """

n = int(input("Dimension matrices a sumar: "))
m1 = []
for i in range(n):
        fila = []
        for j in range(n):
                print("Elemento" ,i, ",", j)
                elem = float (input("Elem: "))
                fila.append(elem)
        m1.append(fila)
print("Matriz 1 leida:\n", m1)

m2 = []
for i in range(n):
        fila = []
        for j in range(n):
                print("Elemento" ,i, ",", j)
                elem = float (input("Elem: "))
                fila.append(elem)
        m2.append(fila)
print("Matriz 1 leida:\n", m2)
def suma_matrices(m1,m2):
    m_suma =[]
    for i in range(n):
        elem = m1[i][j] + m2[i][j]
        fila.append(elem)
        m_suma.append(fila)
    print("Matriz suma:\n", m_suma)
    return m_suma