G = [ [('w', 5), ('b', 12), ('w', 9)],  [('b', 9), ('b', 6)] ] # Token order is opposite relative to 'Rules of HeapGo' on canvas
currentPlayer = 'b'
blackScore = 0 # Once komi is added, this should default to -komi

'''
g -> HeapGo Game
n -> Heap Number

return -> Game with move played
'''
def playHeap(g, n):
    takeAllofOwnColour = False
    takeOneExtra = False

    newPoints = 0

    for i in range(0, len(g[n])):
        if takeAllofOwnColour and takeOneExtra: break

        if len(g[n]) == 0: break

        if not takeAllofOwnColour:
            if g[n][0][0] == currentPlayer:
                newPoints += g[n][0][1]
                g[n].pop(0)
            else:
                takeAllofOwnColour = True


    if len(g[n]) != 0 and not takeOneExtra:
        newPoints += g[n][0][1]
        g[n].pop(0)

    global blackScore
    if currentPlayer == 'b': blackScore += newPoints
    else: blackScore -= newPoints

    return g

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
            
            G = playHeap(G, heapNumber - 1) # Convert from 1 based indexing to 0 based indexing
            currentPlayer = swapPlayer(currentPlayer)

        case "score":
            pass
        case "winner":
            pass
        
        case "quit":
            break
        case _:
            print("Unknown command:", command[0])
