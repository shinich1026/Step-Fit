import csv

with open("musics.csv") as file:
    reader = csv.reader(file)
    search = input("Title: ")
    for title, bpm in reader:
        if search == title:
            print(bpm)
            
            

        
