import json

class JSONMOD:
    def __init__(self, path) -> None:
        self.pathx = path
        with open(self.pathx, 'r') as op:
            self.x = json.load(op)

    def add(self):
        a = input("Enter a name: ")
        b = input("Enter a make: ")
        c = input("Enter a year: ")
        self.x["cars"].append({"name": a, "make": b, "year": c})
        self._save()

    def rem(self):
        try:
            a = input("Enter a name: ")
            b = input("Enter a make: ")
            c = input("Enter a year: ")
            self.x["cars"].remove({"name": a, "make": b, "year": c})
            self._save()
        except ValueError:
            print("Data not found to delete")

    def mod(self):
        try:
            a = input("Enter the current name: ")
            b = input("Enter the current make: ")
            c = input("Enter the current year: ")
            p = input("Enter new name: ")
            q = input("Enter new make: ")
            r = input("Enter new year: ")
            self.x["cars"].remove({"name": a, "make": b, "year": c})
            self.x["cars"].append({"name": p, "make": q, "year": r})
            self._save()
        except ValueError:
            print("Data not found to replace")

    def _save(self):
        with open(self.pathx, 'w') as op:
            json.dump(self.x, op, indent=4)

if __name__ == '__main__':
    path = input("Enter File location: ")
    p = JSONMOD(path)
    flag = True

    while flag:
        choice = input("What do you want to do?\n1. Add data \n2. Remove data \n3. Modify data \nF. Exit\n")
        if choice == '1':
            p.add()
        elif choice == '2':
            p.rem()
        elif choice == '3':
            p.mod()
        elif choice.upper() == 'F':
            flag = False
        else:
            print("Invalid Choice, Enter F if you want to exit")
