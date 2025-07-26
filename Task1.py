try:
    with open("sample.txt","r") as file:
        print(file.read())
except:
    print("The file \'sample.txt' was not found")
              