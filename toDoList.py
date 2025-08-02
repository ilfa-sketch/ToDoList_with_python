List = []
while True :
    print("\n\n Your list :")
    if len(List) == 0 :
        print("Empty")
    else:
        for i in List:
            print(i)
    line = "-------"
    print(f"{line * 5} \nAdd to add list \nRem to remove \nEx to exit")
    inputUser = input("What to do??")
    if inputUser == "Add":
        addList = input("Enter list")
        List.append(addList)
    if inputUser == "Rem":
        remList = input("Urutan berapa??")
        Remove = int(remList) - 1
        List.pop(Remove)
        # TODO: write code...
    if inputUser == "Ex":
        break
    else:
        print("Error Input")