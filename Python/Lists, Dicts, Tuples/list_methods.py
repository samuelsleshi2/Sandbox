def main():
    history = []
    
    while True:
        action = input("Action: ")
        
        if action == "Undo":
            history.pop()
            print("Undone")
        elif action == "Restart":
            history.clear()
            print("Restarted")
        else:
            history.append(action)
        print(history)

main()