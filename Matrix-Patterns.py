def create_matrix(rows,columns):
 matrix =[]
 num =1
 for a in range(rows):
     rows.append(num)
     num +=1+a
     matrix.append(rows)
     return matrix
 rows=int(input("enter the number of rows:"))
 columns=int(input("enter the number of columns:"))
 matrix=create_matrix(rows,columns)
 for row in matrix:
     print(row)

