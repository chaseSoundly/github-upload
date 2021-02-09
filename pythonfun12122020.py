import string

class table():
    def __init__(self):
        self.cols = []
        self.rows = []
        self.content = []
        self.lengths = []
        self.answer_title = ""
        self.answer_col = ""
        self.answer_row = ""
        self.width_max = 0
        
    def crossbeam(self, m, c, s):
        print(s,end="")
        for i in range(0,(m*(int(c)+1))):
            print(s,end="")
        print(s)
        
    def crossbeam2(self, m, c, s1, s2):
        print(s1,end="")
        for i in range(0,m):
            print(s1,end="")
        print(s1,end="")
        for i in range(0,m*int(c)):
            print(s2,end="")
        print()       
    
    def create_table(self):
        self.answer_title = input("Name your table: ")
        self.lengths.append(len(self.answer_title))
        
        while True:
            self.answer_col = input("How many columns do you want? ")
            
            try:
                if (int(self.answer_col) <= 10):
                    if (int(self.answer_col) < 1):
                        print("Minimum number of columns is 1. Please try again.")
                    else:
                        for i in range(0,int(self.answer_col)):
                            if (i == 0):
                                col_temp_name = input("Name your 1st column: ")
                                self.cols.append(col_temp_name)
                                self.lengths.append(len(col_temp_name))
                            elif (i == 1):
                                col_temp_name = input("Name your 2nd column: ")
                                self.cols.append(col_temp_name)
                                self.lengths.append(len(col_temp_name))
                            elif (i == 2):
                                col_temp_name = input("Name your 3rd column: ")
                                self.cols.append(col_temp_name)
                                self.lengths.append(len(col_temp_name))
                            else:
                                col_temp_name = input("Name your %dth column: "%(i+1))
                                self.cols.append(col_temp_name)
                                self.lengths.append(len(col_temp_name))
                        
                        break
                elif (int(self.answer_col) > 10):
                    print("Max number of columns exceeded. Max is 10.")
                else:
                    print("Please try again.")
            except:
                print("Something went wrong. Please input an integer and try again.")
                
        while True:
            self.answer_row = input("How many rows do you want? ")
            
            try:
                if (int(self.answer_row) < 1):
                    print("Minimum number of rows is 1. Please try again.")
                else:
                    for i in range(0,int(self.answer_row)):
                        if (i == 0):
                            row_temp_name = input("Name your 1st row: ")
                            self.rows.append(row_temp_name)
                            self.lengths.append(len(row_temp_name))
                        elif (i == 1):
                            row_temp_name = input("Name your 2nd row: ")
                            self.rows.append(row_temp_name)
                            self.lengths.append(len(row_temp_name))
                        elif (i == 2):
                            row_temp_name = input("Name your 3rd row: ")
                            self.rows.append(row_temp_name)
                            self.lengths.append(len(row_temp_name))
                        else:
                            row_temp_name = input("Name your %dth row: "%(i+1))
                            self.rows.append(row_temp_name)
                            self.lengths.append(len(row_temp_name))
                    break
            except:
                print("Something went wrong. Please input an integer and try again.")
        
        try:
            for i in range(0,int(self.answer_col)):
                for j in range(0,int(self.answer_row)):
                    temp_content = input("Enter the content for " + self.cols[i] + "," + self.rows[j] + ": ")
                    self.content.append(temp_content)
                    self.lengths.append(len(temp_content))
        except:
            print("Something went wrong. Please try again.")
    
    def draw_table(self):
        self.width_max = max(self.lengths)*2
        
        self.crossbeam(self.width_max, self.answer_col, "=")
        
        print("|",end="")
        print(self.answer_title.center((self.width_max*(int(self.answer_col)+1))),end="|")
        print()
        #print("|")
        
        self.crossbeam(self.width_max, self.answer_col, "=")
        
        print("|",end="")
        temp_string = ""
        print(temp_string.center(self.width_max),end="|")                      
        for i in range(0,int(self.answer_col)):
            temp_string = self.cols[i]
            print(temp_string.center(self.width_max-1),end="|")
        print()
        
        self.crossbeam2(self.width_max, self.answer_col, "=", "-")
        
        
        for i in range(0,int(self.answer_row)):
            print("|",end="")
            temp_string = self.rows[i]
            print(temp_string.center(self.width_max),end="|")
            x = i
            for j in range(0,int(self.answer_col)):
                temp_string = self.content[x]
                print(temp_string.center(self.width_max-1),end="|")
                x = x + int(self.answer_row)
            print()
            self.crossbeam2(self.width_max, self.answer_col, "=", "-")
        
        #print(lengths)
        
 
        
t = table()



t.create_table()
t.draw_table()

#def crossbeam(m, c, s):
    #print(s,end="")
    #for i in range(0,(m*(int(c)+1))):
        #print(s,end="")
    #print(s)

#def crossbeam2(m, c, s1, s2):
    #print(s1,end="")
    #for i in range(0,m):
        #print(s1,end="")
    #print(s1,end="")
    #for i in range(0,m*int(c)):
        #print(s2,end="")
    #print()
    ##print(s2)

#def create_table():
    #lengths = []
    #cols = []
    #rows = []
    #content = []
    
    #answer_title = input("Name your table: ")
    #lengths.append(len(answer_title))
    
    #while True:
        #answer_col = input("How many columns do you want? ")
        
        #try:
            #if (int(answer_col) <= 10):
                #if (int(answer_col) < 1):
                    #print("Minimum number of columns is 1. Please try again.")
                #else:
                    #for i in range(0,int(answer_col)):
                        #if (i == 0):
                            #col_temp_name = input("Name your 1st column: ")
                            #cols.append(col_temp_name)
                            #lengths.append(len(col_temp_name))
                        #elif (i == 1):
                            #col_temp_name = input("Name your 2nd column: ")
                            #cols.append(col_temp_name)
                            #lengths.append(len(col_temp_name))
                        #elif (i == 2):
                            #col_temp_name = input("Name your 3rd column: ")
                            #cols.append(col_temp_name)
                            #lengths.append(len(col_temp_name))
                        #else:
                            #col_temp_name = input("Name your %dth column: "%(i+1))
                            #cols.append(col_temp_name)
                            #lengths.append(len(col_temp_name))
                    
                    #break
            #elif (int(answer_col) > 10):
                #print("Max number of columns exceeded. Max is 10.")
            #else:
                #print("Please try again.")
        #except:
            #print("Something went wrong. Please input an integer and try again.")
            
    #while True:
        #answer_row = input("How many rows do you want? ")
        
        #try:
            #if (int(answer_row) < 1):
                #print("Minimum number of rows is 1. Please try again.")
            #else:
                #for i in range(0,int(answer_row)):
                    #if (i == 0):
                        #row_temp_name = input("Name your 1st row: ")
                        #rows.append(row_temp_name)
                        #lengths.append(len(row_temp_name))
                    #elif (i == 1):
                        #row_temp_name = input("Name your 2nd row: ")
                        #rows.append(row_temp_name)
                        #lengths.append(len(row_temp_name))
                    #elif (i == 2):
                        #row_temp_name = input("Name your 3rd row: ")
                        #rows.append(row_temp_name)
                        #lengths.append(len(row_temp_name))
                    #else:
                        #row_temp_name = input("Name your %dth row: "%(i+1))
                        #rows.append(row_temp_name)
                        #lengths.append(len(row_temp_name))
                #break
        #except:
            #print("Something went wrong. Please input an integer and try again.")
    
    #try:
        #for i in range(0,int(answer_col)):
            #for j in range(0,int(answer_row)):
                #temp_content = input("Enter the content for " + cols[i] + "," + rows[j] + ": ")
                #content.append(temp_content)
                #lengths.append(len(temp_content))
    #except:
        #print("Something went wrong. Please try again.")
    
    #maximum = max(lengths)*2
    
    #crossbeam(maximum, answer_col, "=")
    
    #print("|",end="")
    #print(answer_title.center((maximum*(int(answer_col)+1))),end="|")
    #print()
    ##print("|")
    
    #crossbeam(maximum, answer_col, "=")
    
    #print("|",end="")
    #temp_string = ""
    #print(temp_string.center(maximum),end="|")                      
    #for i in range(0,int(answer_col)):
        #temp_string = cols[i]
        #print(temp_string.center(maximum-1),end="|")
    #print()
    
    #crossbeam2(maximum, answer_col, "=", "-")
    
    
    #for i in range(0,int(answer_row)):
        #print("|",end="")
        #temp_string = rows[i]
        #print(temp_string.center(maximum),end="|")
        #x = i
        #for j in range(0,int(answer_col)):
            #temp_string = content[x]
            #print(temp_string.center(maximum-1),end="|")
            #x = x + int(answer_row)
        #print()
        #crossbeam2(maximum, answer_col, "=", "-")
    
    ##print(lengths)    
    
#create_table()