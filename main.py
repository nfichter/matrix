from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(4,1)

matrix = add_edge(matrix,250,250,0,450,350,0)
matrix = add_edge(matrix,250,250,0,350,450,0)
matrix = add_edge(matrix,250,250,0,150,450,0)
matrix = add_edge(matrix,250,250,0,50,350,0)
matrix = add_edge(matrix,250,250,0,50,150,0)
matrix = add_edge(matrix,250,250,0,150,50,0)
matrix = add_edge(matrix,250,250,0,350,50,0)
matrix = add_edge(matrix,250,250,0,450,150,0)

draw_lines( matrix, screen, color )
display(screen)