## install openpyxl  ##
##  ##
##  ##

import functions

def app():
    
    print ("\n\u001b[1m\u001b[40m\u001b[40m --------------- WELCOME TO OUR PROGRAM ----------------- \u001b[0m")
    main_menu = functions.check_input("Enter an option : ","mainmenu")

    while main_menu != 0:
        
        if main_menu == 1:
            print("\033[1;34;40m")
            file = str(input("\nGive the absolute path of the json file: "))
            type ="json"
            
            if functions.checkingFile(file,type):

                sub_menu = functions.check_input("Enter an option : ","submenu")
                
                while sub_menu != 0:
                    
                    if sub_menu == 1:
                            
                        functions.addingLine(file,type)
                        
                        sub_menu = functions.check_input("Enter an option : ","submenu")

                    elif sub_menu == 2:

                        functions.updatingLine(file,type)
                        
                        sub_menu = functions.check_input("Enter an option : ","submenu")
                        
                    elif sub_menu == 3:

                        functions.deletingLine(file,type)
                        
                        sub_menu = functions.check_input("Enter an option : ","submenu")

                    elif sub_menu == 4:

                        functions.readingFile(file,type)
                        
                        sub_menu = functions.check_input("Enter an option : ","submenu") 
        

                    else:

                        sub_menu = functions.check_input("\033[1;31;40m Please enter an option from the list above : \033[1;34;40m","submenu")
                
                main_menu = functions.check_input("Enter an option : ","mainmenu")
                        
            
            
        elif main_menu == 2:
            print("\033[1;34;40m")
            file = str(input("Give the absolute path of the csv file: "))
            type ="csv"
            if functions.checkingFile(file,type):
                
                
                sub_menu = functions.check_input("Enter an option : ","submenu")
                
                while sub_menu != 0:


                    if sub_menu == 1:

                        functions.addingLine(file,type)
                        
                        sub_menu = functions.check_input("Enter an option : ","submenu")
                        
                    elif sub_menu == 2:

                        functions.updatingLine(file,type)
                        
                        sub_menu = functions.check_input("Enter an option : ","submenu")
                        
                    elif sub_menu == 3:

                        functions.deletingLine(file,type)
                        
                        sub_menu = functions.check_input("Enter an option : ","submenu")

                    elif sub_menu == 4:

                        functions.readingFile(file,type)
                        
                        sub_menu = functions.check_input("Enter an option : ","submenu") 

                    else:

                        
                        sub_menu = functions.check_input("\033[1;31;40m Please enter an option from the list above : \033[1;34;40m","submenu")

                main_menu = functions.check_input("Enter an option : ","mainmenu")

        elif main_menu == 3:

            print("\033[1;34;40m")
            file = str(input("Give the absolute path of the excel file: "))
            type ="xlsx"

            if functions.checkingFile(file,type):
                
                
                sub_menu = functions.check_input("Enter an option : ","submenu")
                
                while sub_menu !=0:


                    if sub_menu == 1:

                        functions.addingLine(file,type)
                        
                        sub_menu = functions.check_input("Enter an option : ","submenu")
                        
                    elif sub_menu == 2:

                        functions.updatingLine(file,type)
                        
                        sub_menu = functions.check_input("Enter an option : ","submenu")
                        
                    elif sub_menu == 3:

                        functions.deletingLine(file,type)
                        
                        sub_menu = functions.check_input("Enter an option : ","submenu")

                    elif sub_menu == 4:

                        functions.readingFile(file,type)
                        
                        sub_menu = functions.check_input("Enter an option : ","submenu") 

                    else:

                        
                        sub_menu = functions.check_input("\033[1;31;40m Please enter an option from the list above : \033[1;34;40m","submenu")
               
                main_menu = functions.check_input("Enter an option : ","mainmenu")
       
        else:
            print("\033[1;31;40m")
            print("You should choose one of the options")
            main_menu = functions.check_input("\033[1;31;40m Please enter an option from the list above : \033[1;34;40m","mainmenu")
    
    print("\033[1;32;40m")
    print("Thanks for using our program,  goodbye, see you again soon")
    print("\033[0;37;40m")



                

if __name__ == "__main__":
    
    app()

   
