G = [ [('w', 9), ('b', 12), ('w', 5)],  [('b', 6), ('b', 9)] ]

print("Welcome to HeapGo")

while True:
    print("Enter your command:")
    command = input()
    command = command.split()

    match command[0]:
        case "show":
            print(G)
            
        case "play":
            pass
        case "score":
            pass
        case "winner":
            pass
        
        case "quit":
            break
        case _:
            print("Unknown command:", command[0])
