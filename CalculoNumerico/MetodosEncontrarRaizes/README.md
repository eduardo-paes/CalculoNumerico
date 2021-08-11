# 1. Método da Bisseção: 
*(bisec.py)*
 - Encontra a raiz variando entre a e b até encontrar um f(x) > ERRO.

# 2. Método da Secante: 
*(secante.py)*
 - Traça uma secante entre dois pontos e exclui o ponto mais antigo, vai assim se aproximando de um f(x) > ERRO.

# 3. Método Regula-Falsi:
*(regula_falsi.py)*
 - União dos métodos da Bisseção e Secante, a ideia é traçar uma secante e ir substituindo o ponto que mais se distancia de um f(x) > ERRO.

# 4. Método Iterativo Linear:
*(iterativo_linear.py)*
 - Transforma o problema de encontrar raízes num problema de ponto fixo (ponto fixo é equivalente à f(x) = x, psi(x));
 - Através de psi(x) é realizado um loop para identificação de um f(x) < ERRO.

# 5. Método de Newton:
*(metodo_newton.py)*
 - Identifica uma função psi(x) ideal, que será utilizada para obter o x que soluciona f(x) > ERRO.