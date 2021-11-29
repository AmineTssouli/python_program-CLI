from os import path
import pandas as pd
import matplotlib.pyplot as plt


def mainmenu():
    
    print("\033[1;34;40m")
    print("Choose one option (1, 2, 3 or 0) from the list below \n\n1 - Read a Json file  \n2 - Read a Csv file\n3 - Read an Excel file\n0 - Exit the program  ")
    print("-------------------------------------------------------\n")
    
def submenu():

    print("\033[1;34;40m")
    print("Choose one option (1, 2, 3, 4, 5 or 0) from the list below\n\n")
    print("1 - Add new record")
    print("2 - Edit a record")
    print("3 - Delete a record")
    print("4 - Show the Data")
    print("5 - Show the graph")
    print("0 - Go back to the main menu")
    print("-------------------------------------------------------\n")

def graphmenu():

    print("\033[1;34;40m")
    print("Choose one option (1, 2, 3 or 0) from the list below\n\n")
    print("1 - Show a line plot")
    print("2 - show a bar plot")
    print("3 - show a scatter plot")
    print("0 - Go back ")
    print("-------------------------------------------------------\n")


def check_input(user_input,menu):

    while True:
        try:

            if menu == "submenu":
                submenu()
            elif menu == "mainmenu":
                mainmenu()
            elif menu == "graphmenu":
                graphmenu()

            value = int(input(user_input))

        except ValueError:

            print("\033[1;31;40m")
            print("Not an Integer! Try again.")
            print("\033[1;34;40m")

            continue
        else:
            return value
            

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
            

def checkColumns(df,index):

    error = True
    cols = []
    while error:
        fields = str(input("Enter the Columns names that you want to change their values: "))
        fields = fields.split(',')

        for col in fields:
            col = str(col)
            if col in df.columns:
                cols.append(col)
                error = False
            else:
                print("\033[1;31;40m")
                print("---The column "+ col +" doesn't exist---")
                print("\033[1;34;40m")
                cols = []
                error = True
                break
    else:
        for column in cols:
            df.at[index,column]= input("Enter the new value of "+ column +": ")


def checkColumn(df,column):
    error = True
    while error:
        col = str(input("Give the column that you want in "+str(column)+"-Axis : "))
        if col in df.columns:
            error = False
        else:
            print("\033[1;31;40m ---The column "+ col +" doesn't exist--- \033[1;34;40m")
            error = True
    return col                
    
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
        df = pd.read_excel(file)
    elif type == "csv":
        df = pd.read_csv(file)
    print("-------------------------------------------------------\n")
    print("\n")
    print("\033[1;32;40m")
    print(df.to_string())
    print("\033[1;34;40m")
    return df

def saveTo(file,type,df):

    if type == "json":
       df.to_json(file, orient='records') 
    elif type =="csv":
         df.to_csv(file)
    elif type == "xlsx":
         df.to_excel(file,index = False)  
    

def addingLine(file,type):
    data = {}
    print("\n")
    df  = readingFile(file,type)
    for col in df.columns:
        col = str(col)
        data[col] = input("Enter the "+ col +" :")
    df = pd.DataFrame(df)
    data = pd.DataFrame([data], index=[0])
    df = df.append(data, ignore_index=True)
    saveTo(file,type,df)   
    print("\033[1;32;40m")
    print("--------------------Updated Data----------------------\n")
    print(df.to_string())
    print("-------------------------------------------------------\n")
    print("\033[1;34;40m")

def updatingLine(file,type):
    print("\n")
    df  = readingFile(file,type)
    index = check_index("Enter the index of the line you want to edit : ",df)
    print("\033[1;31;40m")
    print("\n--- Remember to enter the columns name, seperated by comma (,) ----\n")
    print("\033[1;34;40m")
    checkColumns(df,index)
    saveTo(file,type,df)
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
        saveTo(file,type,df)   
        print("\033[1;32;40m")
        print("--------------------Updated Data----------------------\n")
        print(df.to_string())
        print("-------------------------------------------------------\n")
        print("\033[1;34;40m")

def plot(file,type,kind):

    df = readingFile(file,type)
    column_x = checkColumn(df,"X")
    column_y = checkColumn(df,"Y")
    df.plot(kind=kind,x=column_x,y=column_y)
    plt.show()



def app():
    
    print ("\n\u001b[1m\u001b[40m\u001b[40m --------------- WELCOME TO OUR PROGRAM ----------------- \u001b[0m")
    main_menu = check_input("Enter an option : ","mainmenu")

    while main_menu != 0:
        
        if main_menu == 1:
            print("\033[1;34;40m")
            file = str(input("\nGive the absolute path of the json file: "))
            type ="json"
            
            if checkingFile(file,type):

                sub_menu = check_input("Enter an option : ","submenu")
                
                while sub_menu != 0:
                    
                    if sub_menu == 1:
                            
                        addingLine(file,type)
                        
                        sub_menu = check_input("Enter an option : ","submenu")

                    elif sub_menu == 2:

                        updatingLine(file,type)
                        
                        sub_menu = check_input("Enter an option : ","submenu")
                        
                    elif sub_menu == 3:

                        deletingLine(file,type)
                        
                        sub_menu = check_input("Enter an option : ","submenu")

                    elif sub_menu == 4:

                        readingFile(file,type)
                        
                        sub_menu = check_input("Enter an option : ","submenu")

                    elif sub_menu == 5:

                        graph_menu = check_input("Enter an option : ","graphmenu")
                        
                        while graph_menu != 0:
        
                            
                            if graph_menu == 1:

                                plot(file,type,"line")
                                graph_menu = check_input("Enter an option : ","graphmenu")

                            elif graph_menu == 2:

                                plot(file,type,"bar")
                                graph_menu = check_input("Enter an option : ","graphmenu")

                            elif graph_menu == 3:

                                plot(file,type,"scatter")
                                graph_menu = check_input("Enter an option : ","graphmenu")

                            else:
                                graph_menu = check_input("\033[1;31;40m Please enter an option from the list above : \033[1;34;40m","graphmenu")    

                              
                        
                        sub_menu = check_input("Enter an option : ","submenu")  
        

                    else:

                        sub_menu = check_input("\033[1;31;40m Please enter an option from the list above : \033[1;34;40m","submenu")
                
                main_menu = check_input("Enter an option : ","mainmenu")
                        
            
            
        elif main_menu == 2:
            print("\033[1;34;40m")
            file = str(input("Give the absolute path of the csv file: "))
            type ="csv"
            if checkingFile(file,type):
                
                
                sub_menu = check_input("Enter an option : ","submenu")
                
                while sub_menu != 0:


                    if sub_menu == 1:

                        addingLine(file,type)
                        
                        sub_menu = check_input("Enter an option : ","submenu")
                        
                    elif sub_menu == 2:

                        updatingLine(file,type)
                        
                        sub_menu = check_input("Enter an option : ","submenu")
                        
                    elif sub_menu == 3:

                        deletingLine(file,type)
                        
                        sub_menu = check_input("Enter an option : ","submenu")

                    elif sub_menu == 4:

                        readingFile(file,type)
                        
                        sub_menu = check_input("Enter an option : ","submenu") 

                    elif sub_menu == 5:

                        graph_menu = check_input("Enter an option : ","graphmenu")
                        
                        while graph_menu != 0:
        
                            
                            if graph_menu == 1:

                                plot(file,type,"line")
                                graph_menu = check_input("Enter an option : ","graphmenu")

                            elif graph_menu == 2:

                                plot(file,type,"bar")
                                graph_menu = check_input("Enter an option : ","graphmenu")

                            elif graph_menu == 3:

                                plot(file,type,"scatter")
                                graph_menu = check_input("Enter an option : ","graphmenu")

                            else:
                                graph_menu = check_input("\033[1;31;40m Please enter an option from the list above : \033[1;34;40m","graphmenu")
                       
                        sub_menu = check_input("Enter an option : ","submenu") 
                    
                    else:

                        
                        sub_menu = check_input("\033[1;31;40m Please enter an option from the list above : \033[1;34;40m","submenu")

                main_menu = check_input("Enter an option : ","mainmenu")

        elif main_menu == 3:

            print("\033[1;34;40m")
            file = str(input("Give the absolute path of the excel file: "))
            type ="xlsx"

            if checkingFile(file,type):
                
                
                sub_menu = check_input("Enter an option : ","submenu")
                
                while sub_menu !=0:


                    if sub_menu == 1:

                        addingLine(file,type)
                        
                        sub_menu = check_input("Enter an option : ","submenu")
                        
                    elif sub_menu == 2:

                        updatingLine(file,type)
                        
                        sub_menu = check_input("Enter an option : ","submenu")
                        
                    elif sub_menu == 3:

                        deletingLine(file,type)
                        
                        sub_menu = check_input("Enter an option : ","submenu")

                    elif sub_menu == 4:

                        readingFile(file,type)
                        
                        sub_menu = check_input("Enter an option : ","submenu")

                    elif sub_menu == 5:

                        graph_menu = check_input("Enter an option : ","graphmenu")
                        
                        while graph_menu != 0:
        
                            
                            if graph_menu == 1:

                                plot(file,type,"line")
                                graph_menu = check_input("Enter an option : ","graphmenu")

                            elif graph_menu == 2:

                                plot(file,type,"bar")
                                graph_menu = check_input("Enter an option : ","graphmenu")

                            elif graph_menu == 3:

                                plot(file,type,"scatter")
                                graph_menu = check_input("Enter an option : ","graphmenu")

                            else:
                                graph_menu = check_input("\033[1;31;40m Please enter an option from the list above : \033[1;34;40m","graphmenu")                      
                        
                        sub_menu = check_input("Enter an option : ","submenu")
                    else:

                        
                        sub_menu = check_input("\033[1;31;40m Please enter an option from the list above : \033[1;34;40m","submenu")
               
                main_menu = check_input("Enter an option : ","mainmenu")
       
        else:
            print("\033[1;31;40m")
            print("You should choose one of the options")
            main_menu = check_input("\033[1;31;40m Please enter an option from the list above : \033[1;34;40m","mainmenu")
    
    print("\033[1;32;40m")
    print("Thanks for using our program,  goodbye, see you again soon")
    print("\033[0;37;40m")
