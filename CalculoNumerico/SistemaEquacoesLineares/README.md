# Soluções para Sistemas com Matrizes Triangulares:
*(resolucao_triangular.py)*
 - Encontra um vetor x solução do sistema linear Ax = b.

# Eliminação Gaussiana:
*(gauss_elim.py)*
 - Transforma a matriz A do sistema Ax = b numa matriz triangular e, desse modo, é possível encontrar um vetor x através das soluções triangulares desenvolvidas.

# Eliminação Gaussiana com Pivoteamento Parcial:
*(gauss_elim_partial_pivot)*
 - Consiste numa forma de reduzir a propagação de erros por arredondamento, devido às limitações de conversão do ponto flutuante;
 - Para tanto, é realizada uma troca entre as linhas da matriz de modo que na posição A[1][1] esteja o maior valor possível entre os valores de A[i][1].

# Decomposição LU
*(lu_decomp.py)*
- Trata-se de uma forma de resolver a equação Ax = b, realizando a decomposição de A em L e U, onde L é uma matriz triangular inferior e U uma matriz triangular superior;
- Com a decomposição, o problema reduz-se à: L*U*x = b, fazendo Ux = y, tem-se Ly = b;
- Resolver Ly = b, obtém-se y. Substituindo em Ux = y, chega-se ao valor de x, resultado da equação Ax = b.