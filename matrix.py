import math

def print_matrix( matrix ):
	s = "%s x %s\n[" %(len(matrix),len(matrix[0]))
	for r in range(0,len(matrix)):
		if r > 0:
			s += " "
		s += "["
		for c in range(0,len(matrix[0])):
			s+=str(matrix[r][c])+","
		s = s[:-1]
		s += "]\n"
	s = s[:-1]
	s += "]"
	print s

def ident( matrix ):
    ret = new_matrix(len(matrix),len(matrix[0]))
    for r in range(0,len(matrix)):
    	for c in range(0,len(matrix[0])):
    		if c == r:
    			ret[r][c] = 1
    return ret

def scalar_mult( matrix, s ):
    ret = new_matrix(len(matrix),len(matrix[0]))
    for r in range(0,len(matrix)):
    	for c in range(0,len(matrix[0])):
    		ret[r][c] = matrix[r][c]*s
    return ret

#m1 (4x4) * m2 (4xN) -> m2 (4xN)
def matrix_mult( m1, m2 ):
	ret = new_matrix(4,len(m2[0]))
	for r in range(0,4):
		for c in range(0,len(m2[0])):
			current_sum = 0
			for r2 in range(0,4):
				current_sum += (m1[r][r2] * m2[r2][c])
			ret[r][c] = current_sum
	return ret

def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m

#len(matrix[0]) = cols = num of elements in each sublist
#len(matrix) = rows = num of lists

m1 = [[1,2,3,4,5],
	  [5,6,7,8,9],
	  [9,10,11,12,13],
	  [13,14,15,16,17]]

m2 = [[1,1,1,1],
	  [2,2,2,2],
	  [3,3,3,3],
	  [4,4,4,4]]

print_matrix(m1)
print_matrix(m2)
print_matrix(matrix_mult(m2,m1))