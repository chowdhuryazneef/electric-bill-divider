import pandas as pd
from csv import reader, writer
import os
import shutil as sh

file_dir = input("Enter filename without extension: ")
rate = float(input("Enter rate: "))

common = float(input("Enter common: "))
file_real = file_dir + ".csv"
save_loc = input('File save location: ')

assert os.path.isfile(file_real)

def copy_csv(filename, flat):
    direct= save_loc + "\\" + flat + ".csv"
    sh.copy(filename, save_loc)
    sh.move(save_loc + "\\" + filename , direct)
    return direct

        

with open(file_real, 'r') as read_obj:
    template = input("Enter template: ")
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        flat = row[0]
        presentrdg = row[1]
        prevrdg = row[2]
        consumption = float(presentrdg) - float(prevrdg)
        total = (consumption * rate) + common

        
        direct= save_loc + "\\" + flat + ".csv"
        store_excel = save_loc + "\\" + flat + ".xlsx"

        nf = open(template, "r")
        nf = "".join([i for i in nf])
        nf = nf.replace("flat_no", flat)
        nf = nf.replace("prdg", prevrdg)
        nf = nf.replace("presdg" , presentrdg)
        nf = nf.replace("cons", str(consumption))
        nf = nf.replace("total" , str(total))
        nf = nf.replace("rate", str(rate))
        nf = nf.replace("comms", str(common))
        r = open(copy_csv(template, flat), "w")
        r.writelines(nf)
        r.close()


        


            


       
     