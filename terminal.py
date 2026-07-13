import os

while True:
    command = input("-->")

    if command == "ls":
        print(os.listdir())

    elif command == "lstfolder":
        data = os.listdir()
        for x in data:
            if os.path.isdir(x):
                print(x)

    elif command == "lstfile":
        data = os.listdir()
        for x in data:
            if x.endswith(".py"):
                print(x)

    elif command == "exit":
        break

    else:
        print("Invalid Command")