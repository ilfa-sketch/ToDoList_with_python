class toDoList:
    def __init__(self):
        try:
            with open("toDoList.txt", mode="r") as var:
                self.List = [line.strip() for line in var.readlines()]
        except FileNotFoundError:
            self.List = []
    
    def tampilkanTugas(self):
        if len(self.List) == 0:
            print("LIST EMPTY")
        else:
            for i, item in enumerate(self.List, start=1):
                print(f"{i}. {item}")
                    
    def tambahTugas(self):
        while True:
            inputUser = input("masukkan tugas:\n>> ")
            if inputUser == "":
                print("Masukkan tugas dengan benar !!")
                continue
            else:
                self.List.append(inputUser)
                with open("toDoList.txt", mode="w") as var:
                    for item in self.List:
                        var.write(item + "\n")
                print("Sudah di tambahkan")
                break
                
    def hapusTugas(self):
        while True:
            numbDelete = input("masukkan urutan ke berapa yang ingin di hapus??\n>> ")
            if not numbDelete.isdigit():
                print("Masukkan angka yang valid!")
                continue
                
            convert = int(numbDelete)
            if convert < 1 or convert > len(self.List):
                print(f"Masukkan angka antara 1 dan {len(self.List)}")
                continue
                
            self.List.pop(convert - 1)
            with open("toDoList.txt", mode="w") as var:
                for item in self.List:
                    var.write(item + "\n")
            print("Tugas berhasil dihapus")
            break

# Buat instance dari class
app = toDoList()

while True:
    print("\n\nYour list :")
    app.tampilkanTugas()
    line = "-------"
    print(f"{line * 5} \nAdd to add list \nRem to remove \nEx to exit")
    inputUser = input("What to do?? ")
    
    if inputUser == "Add":
        app.tambahTugas()
    elif inputUser == "Rem":
        app.hapusTugas()
    elif inputUser == "Ex":
        break
    else:
        print("Error Input")