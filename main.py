import os


def cls():
    os.system("cls")


TestData = ["Apple", "Banana", "Orange"]


def ListStock():
    for i in range(0, len(TestData)):
        print(f"{i+1}.{TestData[i]}")



def AddStock():
    RunAddstock = 1
    while RunAddstock:
        cls()
        DataInput = input("Input name of product\nor enter 0 to exit\n\n-->")
        if DataInput == "0":
            RunAddstock = False
        else:
            TestData.append(DataInput)


def DeleteStock():
    RunDeleteStock = 1
    while RunDeleteStock :
        cls()
        ListStock()
        DeleteStockInput = int(input("\nSelect product \nor 0 to exit\n\n-->"))
        if DeleteStockInput == 0:
            RunDeleteStock = False
        else:
            TestData.pop(DeleteStockInput-1)


def EditStock():
    RunEditStock = 1
    while RunEditStock:
        cls()
        ListStock()
        EditStockInput = int(input("\nSelect number to edit\nor 0 to exit\n\n-->"))
        if EditStockInput == 0:
            RunEditStock = False
        else:
            cls()
            print(f"Old name is {TestData[EditStockInput-1]}")
            DataEditInput = input("\nWhat name to change\n\n-->")
            TestData[EditStockInput-1] = DataEditInput


start = 1

while start:
    cls()
    print(f"1.List Stock\n"
          f"2.Add Stock\n"
          f"3.Delete Stock\n"
          f"4.Edit Stock\n"
          f"0.Exit\n")
    StartInput = input("-->")

    if StartInput == "0":
        start = False
        cls()
    if StartInput == "1":
        cls()
        ListStock()
        nullwait = input("\n>> Enter to cotinue <<\n")
    if StartInput == "2":
        cls()
        AddStock()
    if StartInput == "3":
        cls()
        DeleteStock()
    if StartInput == "4":
        cls()
        EditStock()

print("end")
