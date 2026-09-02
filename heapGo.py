G = [ [('w', 9), ('b', 12), ('w', 5)],  [('b', 6), ('b', 9)] ]
currentPlayer = 'b'

'''
g -> HeapGo Game
n -> Heap Number

return -> Game with move played
'''
def playHeap(g, n):
    pass

'''
currentPlayer -> The current player either 'w' or 'b'

return -> The opposite of current player
'''
def swapPlayer(currentPlayer):
    if (currentPlayer == 'w'): return 'b'
    if (currentPlayer == 'b'): return 'w'

    print("ERROR: Invalid Current player")
    return '0'

print("Welcome to HeapGo")

while True:
    print("Enter your command:")
    command = input()
    command = command.split()

    match command[0]:
        case "show":
            print(G)

        case "play":
            heapNumber = int(command[1])
            if (heapNumber < 1 or heapNumber > len(G)):
                print("Invalid \"Heap Number\", command ignored")
                continue
            
            G = playHeap(G, heapNumber)
            currentPlayer = swapPlayer(currentPlayer)

        case "score":
            pass
        case "winner":
            pass
        
        case "quit":
            break
        case _:
            print("Unknown command:", command[0])
