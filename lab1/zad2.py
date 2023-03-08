import shutil


path = input("file path: ")
file = None
try:
    file = path
    file_clone = r"F:\\uniwesitet\\6 курс\\programowanie aplikacji sieciawych\\lab1\\lab1zad2_clone.png"
    shutil.copyfile(file,file_clone)
except Exception as ex:
    print(ex)


