from os import path
import pandas as pd
from pandas.core import series
from pandas.core.frame import DataFrame


def mainmenu():
    
    print("\033[1;34;40m")
    print("Choose one option (1, 2, 3 or 0) from the list below \n\n1 - Read a Json file  \n2 - Read a Csv file\n3 - Read an Excel file\n0 - Exit the program  ")
    print("-------------------------------------------------------\n")
    
def submenu():

    print("\033[1;34;40m")
    print("Choose one option (1, 2, 3 or 0) from the list below\n\n")
    print("1 - Add new record")
    print("2 - Edit a record")
    print("3 - Delete a record")
    print("4 - Show the Data")
    print("0 - Go back to the main menu")
    print("-------------------------------------------------------\n")


def check_input(user_input,menu):

    while True:
        try:

            if menu == "submenu":
                submenu()
            elif menu == "mainmenu":
                mainmenu()

            value = int(input(user_input))

        except ValueError:

            print("\033[1;31;40m")
            print("Not an Integer! Try again.")
            print("\033[1;34;40m")

            continue
        else:
            return value
            break

def check_index(text,df):

    while True:

        try:

            value = int(input(text))
            if value >= df.shape[0]:
                print("\033[1;31;40m")
                print("\n--- The index you provided does not have any record ----\n")
                print("\033[1;34;40m")
                continue
        except ValueError:
            print("\033[1;31;40m")
            print("Not an Integer! Try again.")
            print("\033[1;34;40m")
            continue
        else:
            return value
            break


    
def checkingFile (file,extension):

    if file.endswith("." + extension) != True:
        print("\033[1;31;40m")
        print("wrong file")
        print("\033[1;34;40m")
        return False
    elif path.exists(file) != True:
        print("\033[1;31;40m")
        print("Please check the exact file location")
        print("\033[1;34;40m")
        return False
    else:
        return True

def readingFile(file,type):
    
    if type == "json":
        df = pd.read_json(file,orient='records')
    elif type == "xlsx":
        df = pd.read_excel(file, engine='openpyxl')
    elif type == "csv":
        df = pd.read_csv(file)
    print("-------------------------------------------------------\n")
    print("\n")
    print("\033[1;32;40m")
    print(df.to_string())
    print("\033[1;34;40m")
    return df

def addingLine(file,type):
    data = {}
    print("\n")
    df  = readingFile(file,type)
    for col in df.columns:
        col = str(col)
        data[col] = input("enter the "+ col +" :")
    df = pd.DataFrame(df)
    data = pd.DataFrame([data], index=[0])
    df = df.append(data, ignore_index=True)
    if type == "json":
        df.to_json(file, orient='records') 
    elif type =="csv":
        df.to_csv(file)
    elif type == "xlsx":
        df.to_excel(file, orient='records')    

    print("\033[1;32;40m")
    print("--------------------Updated Data----------------------\n")
    print(df.to_string())
    print("-------------------------------------------------------\n")
    print("\033[1;34;40m")

def updatingLine(file,type):
    print("\n")
    df  = readingFile(file,type)

    index = check_index("Enter the index of the line you want to edit : ",df)

    if index < df.shape[0]:

        print("\033[1;31;40m")
        print("\n--- Remember to enter the columns name, seperated by comma (,) ----\n")
        print("\033[1;34;40m")
        fields = str(input("Enter the Columns names that you want to change their values: "))
        fields = fields.split(',')
        for col in fields:
            col = str(col)
            df.at[index,col]= input("enter the new value of "+ col +": ")
        if type == "json":
            df.to_json(file, orient='records') 
        elif type =="csv":
            df.to_csv(file)
        elif type == "xlsx":
            df.to_excel(file, orient='records')    
        
        print("\033[1;32;40m")
        print("--------------------Updated Data----------------------\n")
        print(df.to_string())
        print("-------------------------------------------------------\n")
        print("\033[1;34;40m")


 
def deletingLine(file,type):

    print("\n")
    df = readingFile(file,type)
    index = check_index("Enter the index of the line you want to delete : ",df)       

    index = int(index)
    if index < df.shape[0]:
        df = pd.DataFrame(df)
        df.drop(df.index[index],inplace = True)
        if type == "json":
            df.to_json(file, orient='records') 
        elif type =="csv":
            df.to_csv(file)
        elif type == "xlsx":
            df.to_excel(file, orient='records')    
        
        print("\033[1;32;40m")
        print("--------------------Updated Data----------------------\n")
        print(df.to_string())
        print("-------------------------------------------------------\n")
        print("\033[1;34;40m")
