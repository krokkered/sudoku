import tkinter as tk
from tkinter import *


# sudoku part
class Sudoku:  

    def __init__(self, inputSudoku):
        self.inputSudoku= self.convertMatrixToInt(inputSudoku)
        self.inputSudoku=self.convertMatrixTo0(self.inputSudoku)
        self.maxsolvingtry=0
        self.solvedSudoku=[]
        self.basta=0
        self.solvedflag=False


    def convertMatrixToInt(self, mat):
        for i in range(9):
            for j in range(9):
                if mat[i][j]!="":
                    mat[i][j]= int(mat[i][j])
        return mat
    
    def convertMatrixTo0(self, mat):
        for i in range(9):
            for j in range(9):
                if mat[i][j]=='':
                    mat[i][j]= 0
        return mat   

    def hasDoubleInRow(self, c):
        a=[ele[:] for ele in c] 
        doublefound=False
        for i in range(9):
            b=a[i][:]
            if "" in a[i]:
                while "" in a[i]:
                    a[i].remove("")
            if len(set(a[i])) != len(a[i]):
                doublelist=list(set([x for x in a[i] if a[i].count(x) > 1]))
                #for k,el in enumerate(b):
                    #if el in doublelist:
                        #print("the row ",i," has a double",el,"in the column", k)
                doublefound = True
        return doublefound


    def hasDoubleInCol(self, c):
        a=[ele[:] for ele in c] 
        acol=[[row[i] for row in a]for i in range(9)]
        doublefound=False
        for i in range(9):
            b=acol[i][:]
            if "" in acol[i]:
                while "" in acol[i]:
                    acol[i].remove("")
            if len(set(acol[i])) != len(acol[i]):
                doublelist=list(set([x for x in acol[i] if acol[i].count(x) > 1]))
                #for k,el in enumerate(b):
                    #if el in doublelist:
                        #print("the column ",i," has a double",el," in the row", k)
                doublefound = True
        return doublefound
            

    def hasDoubleInSquare(self, c):
        a=[ele[:] for ele in c] 
        doublefound=False
        tq=[]
        for r in range(0,7,3):
            for d in range(0,7,3):
                quadsingolo = [element for row in a[r:r+3] for element in row[d:d+3]]
                tq.append(quadsingolo)
        for i in range(9):
            b=tq[i][:]
            if "" in tq[i]:
                while "" in tq[i]:
                    tq[i].remove("")
            if len(set(tq[i])) != len(tq[i]):
                doublelist=list(set([x for x in tq[i] if tq[i].count(x) > 1]))
                #for k,el in enumerate(b):
                    #if el in doublelist:
                       # print("the little square",i," has a douoble",el," in the place ", k)
                doublefound = True
        return doublefound


    def hasDoubles(self, mat):
        if self.hasDoubleInRow(mat) or self.hasDoubleInCol(mat) or self.hasDoubleInSquare(mat):
            return True
        else: return False
        



        
    def riempivuoti(self, sudo):
        matdef=[ele[:] for ele in sudo ]
        # rimpie i vuoti 
        while True:
            matdef2=[ele[:] for ele in matdef ]
            sudotemp=[ele[:] for ele in matdef ]
                #convert sudotemp empty elements to empty list
            for i in range(9):
                for j in range(9):
                        if sudotemp[i][j]=="":
                            sudotemp[i][j]=[]
            mattemp=[ele[:] for ele in sudo ]
            
            for i in range(9):
                for j in range(9):
                    for k in range(1,10):
                        mattemp=[ele[:] for ele in matdef ] 
                        if mattemp[i][j] =="":
                            mattemp[i][j]=k
                            if not self.hasDoubles(mattemp):
                                sudotemp[i][j].append(k)
            
            for i in range(9):
                for j in range(9):
                    if type(sudotemp[i][j])==list:
                        if len(sudotemp[i][j])==1:
                            matdef[i][j]=sudotemp[i][j][0]
            if matdef==matdef2:
                #print(sudotemp)
                break
        return sudotemp
        






    # fase due, elementi singoli in lista

    # righe

    def singleelements(self,mat):
        for lst in mat:
            numcom={}
            for i in lst:
                if type(i)==list:
                    for k in i:
                        if k in numcom.keys():
                            numcom[k]+=1
                        else:
                            numcom[k]=1
                    
                    
            for key in numcom.keys():
                if numcom[key]==1:
                    for el in lst:
                        if type(el)==list:
                            if key in el:
                                lst[lst.index(el)]=key
        return mat
            



    def singleelementscol(self,mat):
        acol=[[row[i] for row in mat]for i in range(9)]
        acol=self.singleelements(acol)
        mat2=[[row[i] for row in acol]for i in range(9)]
        return mat2  

    #per i quadrati 

    def singleelementsquad(self,mat):  
        tq=[]
        for r in range(0,7,3):
            for d in range(0,7,3):
                quadsingolo = [element for row in mat[r:r+3] for element in row[d:d+3]]
                tq.append(quadsingolo)
        tq=self.singleelements(tq)
        mat2=[]
        for r in range(0,7,3):
            for d in range(0,7,3):
                quadsingolo = [element for row in tq[r:r+3] for element in row[d:d+3]]
                mat2.append(quadsingolo)
        return mat2

    def resetvuoti(sef,sudo):
        for i in range(9):
            for j in range(9):
                    if type(sudo[i][j])==list:
                        sudo[i][j]=""
        #for i in sudo:
            #print(i)
            
               
                    
    def hasEmpty(self,mat):              
        for r in mat:
            for el in r:
                if el=="":
                    return True
        return False
                    


    def solve2(self): #the solver works only if the sudoku has a univocal solution

        mat=self.inputSudoku
        sudotemp=self.riempivuoti(mat)
        sudotemp=self.singleelements(sudotemp)
        self.resetvuoti(sudotemp)
        sudotemp=self.riempivuoti(sudotemp)
        sudotemp=self.singleelementscol(sudotemp)
        self.resetvuoti(sudotemp)
        sudotemp=self.riempivuoti(sudotemp)
        sudotemp=self.singleelementsquad(sudotemp)
        self.resetvuoti(sudotemp)
        if self.hasEmpty(sudotemp):
            self.maxsolvingtry+=1
            if self.maxsolvingtry<120:
                self.inputSudoku=sudotemp
                print("bisogna ricorrere")
                print("mat",sudotemp)
                self.solve()
            else:
                print("no univocal solution")
                self.solvedSudoku= sudotemp

        else:
            print("niente vuoti")
            self.solvedSudoku= sudotemp


    # this is based on https://www.youtube.com/watch?v=G_UYXzGuqvM
    def possible(self,x, y, n):
        grid = self.inputSudoku
        for i in range (0, 9):
            if grid[i][y] == n:
                return False
        for j in range (9):
            if grid[x][j] == n:
                return False

        x0 = (x // 3) * 3
        y0 = (y // 3) * 3

        for i in range(3):
            for j in range(3):
                if grid[x0 + i][y0 + i] == n:
                    return False
        return True

    def isSolved(self):
        s=True
        for i in range (0, 9):
            for j in range (0, 9):
                if self.inputSudoku[i][j] == 0:
                    s=False
        return s

    def solve(self):
        self.basta+=1
        if self.basta<1000000 and self.solvedflag== False:
            for i in range (0, 9):
                for j in range (0, 9):
                    if self.inputSudoku[i][j] == 0:
                        for _ in range(1,10):
                            if self.possible(i, j, _):
                                self.inputSudoku[i][j] = _
                                self.solve()
                                self.inputSudoku[i][j] = 0                        
                        return
        if self.isSolved():
            print("di risolvere è risolto")
            self.solvedflag=True
            print(self.inputSudoku)
            self.solvedSudoku= [x[:] for x in self.inputSudoku]








# graphic interface 

class GUI:


    def __init__(self):
        

        self.window = tk.Tk()
        self.window.title(" Sudoku ")
        # window.geometry('350x200')
        self.frameG = tk.Frame(master=self.window)
        self.frameG.grid(row=0, column=0, pady=(20, 0), padx=(15, 15))
        
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=2)
        self.listacelle = []
        self.validate = self.window.register(self.validate_input)
        n=1
        for i in range(9):
            sepy = 0
            if i == 3 or i == 6:
                sepy = 6
            for j in range(9):
                self.frame = tk.Frame(
                    master=self.frameG,
                    relief=tk.FLAT,
                    borderwidth=1
                )
                if j == 3 or j == 6:
                     self.frame.grid(row=i, column=j, padx=(6, 0), pady=(sepy, 0))
                else:
                     self.frame.grid(row=i, column=j, pady=(sepy, 0))

                inputtxt = Entry( self.frame, bg="light yellow", width=2,validate='all', validatecommand=(self.validate, "%P"),disabledbackground="light blue",disabledforeground="white",textvariable="cella"+str(n))
                inputtxt.focus_set()
                #inputtxt.insert(INSERT, str(i)+","+str(j))
                inputtxt.insert(INSERT, "")
                inputtxt.bind('<FocusIn>', self.select_on_focus)
                inputtxt.bind('<KeyRelease>', self.nextCell)
                inputtxt.pack()
                self.listacelle.append(inputtxt)
                n+=1



        self.var1 = tk.IntVar() # edit mode toggler
        self.var1.set(True)
        c1 = tk.Checkbutton( self.window, text='Edit mode', variable=self.var1,
                            onvalue=1, offvalue=0, command=self.editModeOn)
        c1.grid(row=10, column=0, sticky="w", pady=(7, 10), padx=(15, 0))
        okButton = Button( self.window, text="Solve", command= self.risolvi)
        okButton.grid(row=10, column=0, sticky="e", pady=(7, 10), padx=(0, 15))






    def gatherNumbers(self):
        listacel=self.listacelle
        templist=[]      
        for e in listacel:
                    templist.append(e.get())
        matrix = [[0 for i in range(9)] for i in range(9)]
        for indx,elm in enumerate(templist):
            matrix[indx//9][indx%9]=elm
        print ("here are the insert numbers")
        for k in matrix:
            print(k)
        return matrix


    def editModeOn(self):
        if (self.var1.get() == 1):
            print("edit mode on ")
            for e in self.listacelle:
                e['state'] = 'normal'
        else:
            print("edit mode off")
            edit_Mode = False
            for e in self.listacelle:
                if e.get()!= "":
                    e['state'] = 'disabled'





    def validate_input(self,val):
        valid = (val=="") or (val.isdigit() and len(val) <= 1)
        return valid

    def select_on_focus(self,event):
        event.widget.select_range(0, tk.END)  # Select all the text in the widget.
        

    def nextCell(self,event):
        entry_index = self.listacelle.index(self.window.focus_get())
        if entry_index < len(self.listacelle) - 1:
            self.listacelle[entry_index + 1].focus_set()
        else:
            self.listacelle[0].focus_set()

    def insertNumbersOnScreen(self,mat):
        for i,el in enumerate(self.listacelle):
            el.delete(0, tk.END)
            el.insert(0, mat[int(i/9)][i%9])


    def risolvi(self):
        print("parte per risolvere")
        mat=self.gatherNumbers()

        sud= Sudoku(mat)
        sud.solve()
        solved =sud.solvedSudoku
        print("solved",solved)
        self.insertNumbersOnScreen(solved)

    #gui cellette
    



Newgui=GUI()
Newgui.window.mainloop()