print ("===DIVIDING CALCULATOR===")

try:
    angkaPertama=int(input("Insert the number : "))
    angkaKedua=int(input("Insert the dividers : "))

    hasil = angkaPertama/angkaKedua

    print("The result is", hasil)
except ZeroDivisionError:
    print("Can't divide a number by 0!")
except:
    print("Inputted data should be in integer!")
