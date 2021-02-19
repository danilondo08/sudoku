import json
import copy


class Board:

    def __init__(self, squares, emptySquares, squaresByColumns, squaresBySquares):
        self.squares = squares
        self.emptySquares = emptySquares
        self.squaresByColumns = squaresByColumns
        self.squaresBySquares = squaresBySquares

    def initializeSquares(self):
        with open("sudoku.txt", "r") as archivo:
            self.squares = [i.strip().split(',') for i in archivo.readlines()]

    def sudokuBoard(self):
        cont1 = 0
        cont = 0
        print('----------------------------------------------------------------')
        for row in range(9):
            for column in range(9):
                if self.squares[row][column] == '':
                    self.squares[row][column] = ' '
                print(self.squares[row][column], end=('   '))
                cont += 1
                if cont % 18 == 0 or cont % 9 == 0 or cont % 27 == 0:
                    print("|")
            # print(end=" \n")
            print('----------------------------------------------------------------')
            cont1 += 1
            # if cont1 % 3 == 0:
            #     print('----------------------------------------------------------------')

    def initializeEmptySquares(self):
        self.emptySquares = copy.deepcopy(self.squares)
        for row in range(9):
            for column in range(9):
                if self.emptySquares[row][column] == ' ':
                    self.emptySquares[row][column] = [
                        '1', '2', '3', '4', '5', '6', '7', '8', '9']
                else:
                    self.emptySquares[row][column] = []

    def __possibleNumbers(self, list1, list2):
        possibleNumbers = [elem for elem in list1 if elem not in list2]
        return possibleNumbers

    def discardByRows(self):
        for row in range(9):
            for column in range(9):
                if self.squares[row][column] == ' ':
                    self.emptySquares[row][column] = self.__possibleNumbers(
                        self.emptySquares[row][column], self.squares[row])

    def initializeSquaresByColumns(self):
        sudokuByColumns = []
        cont = 0
        for row in range(9):
            for column in self.squares:
                sudokuByColumns.append(column[row])
        while cont < len(sudokuByColumns):
            self.squaresByColumns.append(sudokuByColumns[cont:cont+9])
            cont += 9

    def discardByColumns(self):
        for row in range(9):
            for column in range(9):
                if self.squares[row][column] == ' ':
                    # print(self.emptySquares[row][column])
                    # print(self.squaresByColumns[column])
                    self.emptySquares[row][column] = self.__possibleNumbers(
                        self.emptySquares[row][column], self.squaresByColumns[column])
                    # print(prueba)

    def initializeSquaresBySquares(self):
        sudokuBySquares = []

        for row in range(3):
            for column in range(3):
                sudokuBySquares.append(self.squares[row][column])

        for row in range(3):
            for column in range(3, 6):
                sudokuBySquares.append(self.squares[row][column])

        for row in range(3):
            for column in range(6, 9):
                sudokuBySquares.append(self.squares[row][column])

        for row in range(3, 6):
            for column in range(3):
                sudokuBySquares.append(self.squares[row][column])

        for row in range(3, 6):
            for column in range(3, 6):
                sudokuBySquares.append(self.squares[row][column])

        for row in range(3, 6):
            for column in range(6, 9):
                sudokuBySquares.append(self.squares[row][column])

        for row in range(6, 9):
            for column in range(3):
                sudokuBySquares.append(self.squares[row][column])

        for row in range(6, 9):
            for column in range(3, 6):
                sudokuBySquares.append(self.squares[row][column])

        for row in range(6, 9):
            for column in range(6, 9):
                sudokuBySquares.append(self.squares[row][column])

        conta = 0
        while conta < len(sudokuBySquares):
            self.squaresBySquares.append(sudokuBySquares[conta:conta+9])
            conta += 9

    def printBoard(self, tablero):
        cont1 = 0
        cont = 0
        print('---------------------------------------')
        for row in range(9):
            for column in range(9):
                print(tablero[row][column], end=('   '))
                cont += 1
                if cont == 0 or cont % 3 == 0:
                    print("|", end='')
            print(end=" \n")

            cont1 += 1
            # print("| " , end='')
            if cont1 % 3 == 0:
                print('---------------------------------------')
    
    def replaceNumbersOnTheBoard(self):
        variable=''
        for row in range(9):
            for column in range(9):
                if self.squares[row][column]==' ':
                        if len(self.emptySquares[row][column])==1:
                            self.squares[row][column]=self.emptySquares[row][column]

    def discardBySquares(self):
        # for row in range(3):
        #     for column in range(3):
        #         if self.squares[row][column] == ' ':
        #             # print(self.emptySquares[row][column])
        #             # print(self.squaresBySquares[0])
        #             prueba = self.__possibleNumbers(
        #                 self.emptySquares[row][column], self.squaresBySquares[0])
                    # print(prueba)
        # for row in range(3):
        #     for column in range(3, 6):
        #         if self.squares[row][column] == ' ':
        #             print(self.emptySquares[row][column])
        #             print(self.squaresBySquares[1])
        #             prueba2 = self.__possibleNumbers(
        #                 self.emptySquares[row][column], self.squaresBySquares[1])
        #             print(prueba2)
        for row in range(3):
            for column in range(6, 9):
                if self.squares[row][column] == ' ':
                    print(self.emptySquares[row][column])
                    print(self.squaresBySquares[2])
                    prueba= self.__possibleNumbers(
                        self.emptySquares[row][column], self.squaresBySquares[2])
                    print(prueba)

        for row in range(3, 6):
            for column in range(3):
                if self.squares[row][column] == ' ':
                    self.emptySquares[row][column] = self.__possibleNumbers(
                        self.emptySquares[row][column], self.squaresBySquares[3])

        for row in range(3, 6):
            for column in range(3, 6):
                if self.squares[row][column] == ' ':
                    self.emptySquares[row][column] = self.__possibleNumbers(
                        self.emptySquares[row][column], self.squaresBySquares[4])

        for row in range(3, 6):
            for column in range(6, 9):
                if self.squares[row][column] == ' ':
                    self.emptySquares[row][column] = self.__possibleNumbers(
                        self.emptySquares[row][column], self.squaresBySquares[5])

        for row in range(6, 9):
            for column in range(3):
                if self.squares[row][column] == ' ':
                    self.emptySquares[row][column] = self.__possibleNumbers(
                        self.emptySquares[row][column], self.squaresBySquares[6])

        for row in range(6, 9):
            for column in range(3, 6):
                if self.squares[row][column] == ' ':
                    self.emptySquares[row][column] = self.__possibleNumbers(
                        self.emptySquares[row][column], self.squaresBySquares[7])

        for row in range(6, 9):
            for column in range(6, 9):
                if self.squares[row][column] == ' ':
                    self.emptySquares[row][column] = self.__possibleNumbers(
                        self.emptySquares[row][column], self.squaresBySquares[8])


sudoku = Board([], [], [], [])
sudoku.initializeSquares()
sudoku.sudokuBoard()
sudoku.initializeEmptySquares()
# sudoku.emptySquaresBoard()
sudoku.discardByRows()
# sudoku.emptySquaresBoard()
# sudoku.emptySquaresBoard()
sudoku.initializeSquaresByColumns()
# print(sudoku.emptySquares[0][5])
sudoku.discardByColumns()
# print(sudoku.squaresByColumns[5])
# print()

# print('*'*124)
# sudoku.emptySquaresBoard()
sudoku.printBoard(sudoku.emptySquares)
sudoku.replaceNumbersOnTheBoard()
sudoku.sudokuBoard()
sudoku.initializeSquaresBySquares()
sudoku.discardBySquares()
# print(sudoku.squaresBySquares)
# sudoku.printBoard(sudoku.squaresBySquares)
sudoku.printBoard(sudoku.emptySquares)
# sudoku.printBoard(sudoku.squaresByColumns)
