path = input("file path: ")
file = None
try:
    file = open(path,"r",encoding="utf-8")
    clone_file = open("F:\\uniwesitet\\6 курс\\programowanie aplikacji sieciawych\\lab1\\lab1zad1_clone.txt","w",encoding="utf-8")
    clone_file.write(file.read())
except Exception as ex:
    print(ex)


