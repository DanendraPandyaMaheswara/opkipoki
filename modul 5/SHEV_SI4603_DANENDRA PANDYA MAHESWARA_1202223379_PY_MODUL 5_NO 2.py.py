username = "1202223379"
password = "PPLIsFun2022"
loginChance = 3

print("===DASPRO LOGIN===\n")

while loginChance >= 1:
    loginChance -= 1
    
    try:
        masukkanUsername = input("Username : ")
        masukkanPassword = input("Password : ")
        
        if len(masukkanPassword) <= 8:
            raise NameError
        
        elif masukkanUsername == username and masukkanPassword == password:
            print("\nSuccesfully logged in!\n")
        elif masukkanUsername != username and masukkanPassword == password:
            print("\nWrong username!\n")
        elif masukkanUsername != username and masukkanPassword != password:
            print("\nWrong username and password!\n")
        elif masukkanUsername == username and masukkanPassword != password:
            print("\nWrong password!\n")
            
    except NameError:
        print("password length should be more then 8 letter!")
        break
        