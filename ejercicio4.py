SUDOKU = [
    [0,4,0,0],
    [0,0,0,4],
    [0,0,2,3],
    [2,3,0,0],
]

# lista
def comprobe_column(sudoku,col,value):
    column = []
    for row in sudoku:
        column.append(row[col])
    
    if value not in column:
        #for i in column:
            #print(f'|{i}|')
        return True

    else:
        #for i in column:
        #    print(f'|{i}|')
        return False


def comprobe_row(sudoku,row, value):
        if value not in sudoku[row]:
            #print(row)
            return True
        else:
            #print(row)
            return False


def comprobe_grid(sudoku,row,column,value):
    grid = []
    # cuadrante 1 y 2
    if -1<row<2:
        if -1<column<2:
            for i in sudoku[:2]:
                grid.extend(i[:2])

        elif 1<column<4:
            for i in sudoku[:2]:
                grid.extend(i[2:])
    
    # cuadrante 3 y 4
    elif 1<row<4:
        if -1<column<2:
            for i in sudoku[2:]:
                grid.extend(i[:2])

        elif 1<column<4:
            for i in sudoku[2:]:
                grid.extend(i[2:])
    
    if value not in grid:
        return True

    else:
        return False


def print_s(sudoku):
    for i in sudoku:
        print(i)
    print('\n')


def solution(sudoku):
    c = 0
    for row in range(4):
        for col in range(4):
            if sudoku[row][col]!= 0:
                c += 1
    if c == 16:
        return True
    else:
        return False


def sudoku_solver(sudoku):
    # recorrer sudoku
    for row in range(4):
        for col in range(4):
            if sudoku[row][col]== 0:

                # intentar valor
                for option in range(1,5):
                    if comprobe_column(sudoku,col,option) and comprobe_row(sudoku,row,option) and comprobe_grid(sudoku,row,col,option):
                        sudoku[row][col] = option
                        sudoku_solver(sudoku)

                        # muestra la primera solucion posible, para ver todas las soluciones comentar, y descomentar la opcion debajo
                        if solution(sudoku): #
                            return  #

                        sudoku[row][col] = 0

                # muestra todas las soluciones posibles. para ver, descomentar, y comentar la opción de arriba
                #return
    
    for i in sudoku:
        print(i)
    print('\n')
    return


sudoku_solver(SUDOKU)