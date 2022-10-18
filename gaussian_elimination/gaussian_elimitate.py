import numpy as np

class GaussianEliminate:
  
  def __init__(self, matrix) -> None:
    self.A = matrix


  def zeros_before(self):
    zeros = []
    for i,row in enumerate(self.A):
      cont = 0
      for number in row:
        if number == 0: cont +=1
        else: break
      zeros.append((i,cont))
    self.zeros = zeros


  def organize_vectors(self):
    self.zeros_before()
    self.zeros = sorted(self.zeros,key= lambda x: x[1])
    self.eschelon_matrix = [self.A[i[0]] for i in self.zeros]


  def eschelon(self):
    for i in range(len(self.A[0])):
      for k in range(i,len(self.A)):
        a = self.A[k][i]
        if a !=0:break

      if a == 0: continue
      for j in range(k+1,len(self.A)):
        
        b = self.A[j][i]
        if b == 0: continue
        for idx in range(i,len(self.A[j])):
          self.A[j][idx]= self.A[j][idx]*a - self.A[k][idx]*b
    
    self.organize_vectors()

  
  def get_nule_lines(self, matrix):
    matrix_post = 0

    for row in matrix:
      for col in row:
        if not (col == 0): matrix_post += 1; break

    return matrix_post


  def get_posts(self):
    self.main_matrix_post = self.get_nule_lines(self.eschelon_matrix)
    
    var_matrix = [row[:len(row) - 1] for row in self.eschelon_matrix]
    self.var_matrix_post = self.get_nule_lines(var_matrix)
    self.nb_var_matrix = len(self.A[0]) - 1
    

  def find_solutions(self, matrix):
    variables = [0]*(len(matrix[0])-1)
    for i,row in enumerate(matrix[::-1]):
      pos = len(matrix)-i -1
      variables[pos] = (row[-1] - np.dot(row[:-1],variables))/row[pos]
    return variables


  def possible_solutions(self):
    self.eschelon()
    self.get_posts()
    
    if self.var_matrix_post == self.main_matrix_post:
      if self.main_matrix_post == self.nb_var_matrix: 
        return self.find_solutions(self.eschelon_matrix)
        
      else: return "Infinity solutions."
      
    else: return "There is not real solution."
      

if __name__ == "__main__":
    A = [[1,2,3],
         [1,6,7]]
    
    model = GaussianEliminate(A)
    solutions = model.possible_solutions()

    print(solutions)
    
