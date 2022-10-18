import numpy as np

def zeros_before(A):
  zeros = []
  for i,row in enumerate(A):
    cont = 0
    for number in row:
      if number == 0: cont +=1
      else: break
    zeros.append((i,cont))
  return zeros


def organize_vectors(A):
  zeros = zeros_before(A)
  zeros = sorted(zeros,key= lambda x: x[1])
  A = [A[i[0]] for i in zeros]
  return A


def eschelon(A):
  for i in range(len(A[0])):
    
    for k in range(i,len(A)):
      a = A[k][i]
      if a !=0:break

    if a == 0: continue
    
    for j in range(k+1,len(A)):
      
      b = A[j][i]
      if b == 0: continue
      
      for idx in range(i,len(A[j])):
        A[j][idx]= A[j][idx]*a - A[k][idx]*b
  
  A = organize_vectors(A)
  return A


def get_post_matrix(matrix):
  matrix_post = 0

  for row in matrix:
    for col in row:
      if not (col == 0): matrix_post += 1; break

  return matrix_post


def find_solutions(matrix):
  variables = [0]*(len(matrix[0])-1)
  for i,row in enumerate(matrix[::-1]):
    pos = len(matrix)-i -1
    variables[pos] = (row[-1] - np.dot(row[:-1],variables))/row[pos]
  return variables


def possible_solutions(matrix_post, var_eschelon_post, n_var):
  if var_eschelon_post == matrix_post:
    if matrix_post == n_var: 
      solutions = find_solutions(eschelon_matrix)
      print(solutions)
    else: print("Infinity solutions.")
  else:
    print("There is not real solution.")


if __name__ == "__main__":
    A = [[1,2,3],
         [1,7,6]]
    
    eschelon_matrix = eschelon(A)
    
    var_matrix = [row[:len(row) - 1] for row in eschelon_matrix]
    
    matrix_post = get_post_matrix(eschelon_matrix)
    var_eschelon_post = get_post_matrix(var_matrix)
    n_var = len(A[0]) - 1
    
    possible_solutions(matrix_post, var_eschelon_post, n_var)

    