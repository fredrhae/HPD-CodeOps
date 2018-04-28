oJogo = {'cima-E': 'O', 'cima-M': 'O', 'cima-D': 'X', 'meio-E': 'X', 'meio-M': 'X','meio-D': 'X', 'baixo-E': 'X', 'baixo-M': 'O', 'baixo-D': 'X '}

def printBoard(board):
    print(board['cima-E'] + '|' + board['cima-M'] + '|' + board['cima-D'])
    print('-+-+-')
    print(board['meio-E'] + '|' + board['meio-M'] + '|' + board['meio-D'])
    print('-+-+-')
    print(board['baixo-E'] + '|' + board['baixo-M'] + '|' + board['baixo-D'])

printBoard(oJogo)
