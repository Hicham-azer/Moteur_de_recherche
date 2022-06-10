import os

def searchfile(words) : 
    list_of_words = words.split()
    print(list_of_words)
    dir_path = r"C:\Users\hicha\Desktop\moteur_de_recherche\files"
    res = []

    for file in os.listdir(dir_path):
        cur_path = os.path.join(dir_path,file)
        if os.path.isfile(cur_path):
            with open (cur_path, 'r') as file :
                for i in range ( 0 , len (list_of_words) +1 )  :
                    if list_of_words[i] in file.read():
                        res.append(file.name)
                        
    return res

words = input("donner les mots à chercher : ")
print (searchfile(words) )
