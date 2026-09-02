G = [ [('w', 5), ('b', 12), ('w', 9)],  [('b', 9), ('b', 6)] ] # Token order is opposite relative to 'Rules of HeapGo' on canvas
currentPlayer = 'b'
blackScore = 0 # Once komi is added, this should default to -komi

def oppositePlayer(player):
    if player == 'b': return 'w'
    if player == 'w': return 'b'

    print("Invalid player")
    return '0'

'''
g -> HeapGo Game
n -> Heap Number

return -> Game with move played
'''
def playHeap(g, n):
    takeAllofOwnColour = False
    takeOneofOpponentColour = False

    newPoints = 0

    for i in range(0, len(g[n])):
        if takeAllofOwnColour: break

        if len(g[n]) == 0: break

        if not takeAllofOwnColour:
            if g[n][0][0] == currentPlayer:
                newPoints += g[n][0][1]
                g[n].pop(0)
            else:
                takeAllofOwnColour = True


    if len(g[n]) != 0 and not takeOneofOpponentColour and g[n][0][0] == oppositePlayer(currentPlayer):
        newPoints += g[n][0][1]
        g[n].pop(0)

    global blackScore
    if currentPlayer == 'b': blackScore += newPoints
    else: blackScore -= newPoints

    return g

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
            
            G = playHeap(G, heapNumber - 1) # Convert from 1 based indexing to 0 based indexing
            currentPlayer = oppositePlayer(currentPlayer)

        case "score":
            if currentPlayer == 'b':
                print("Black's score is:", blackScore)
            else:
                print("White's score is:", -blackScore)

        case "winner":
            atLeastOneHeapNotEmpty = False
            for i in range(0, len(G)):
                if len(G[i]) != 0: 
                    atLeastOneHeapNotEmpty = True
                    break
            if atLeastOneHeapNotEmpty:
                print("Game is not done")
            else:
                if blackScore > 0: print("Black Wins! with a score of:", blackScore)
                else: print("White Wins! with a score of:", -blackScore)
        
        case "quit":
            break
        case _:
            print("Unknown command:", command[0])
