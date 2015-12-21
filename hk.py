# -*- coding: utf-8 -*-
# Written by Matthew Gal
# Dec 2014 

import Tkinter 
from Tkinter import *

# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html

# close command line window after run app
# emptry database entries after clicking add
# show success info after adding new data
# törlés gomb a főablakon
# javítás gomb



class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.parent = master
        self.initUI()
		
		
	
    def initUI(self):
# NOT RESIZABLE

	self.parent.resizable(width=FALSE, height=FALSE)

#PROGRAM TITLE

	self.parent.title("Házi Könyvtár")
	# self.parent.iconbitmap('kt.ico')
	
#LABELS

	L = Label(self.parent,text = "Üdvözöllek a Házi Könyvtár programban!", font = ('Comic Sans MS',25)).place(x=10,y=20)
	L2 = Label(self.parent,text = "Keresés típusa:", font = ('Comic Sans MS',12)).place(x=50,y=118)
	L9 = Label(self.parent,text = "Keresés:", font = ('Comic Sans MS',12)).place(x=50,y=85)
		
	
#SEPARATOR LINE

	separator = Frame(height=2, bd=1, relief=SUNKEN)
	separator.pack(fill=X, padx=5, pady=150)


	

		
	def callback(hello):
		
		keres = SearchVariable.get()
		keres = keres.encode('utf-8')
		
		lookup = search_variable.get()
		lookup = lookup.encode('utf-8')

		szamok = Search(keres,lookup)
		
		Switch(szamok)
		
	#ENTRY

	search_variable = StringVar()
	self.entry = Entry(self.parent, bg = "white",  textvariable = search_variable)
	self.entry.bind('<Return>', callback)
	self.entry.place(x=120,y=90, width = 300)
	self.entry.focus_set()
	
	def Switch(szamok):		
		
		def print_spinval():
			
			if len(szamok) > 0:
					current = szamok[spinval.get()-1]
					Write(current)
			
		
		
		if len(szamok) > 0:
			Write(szamok[0])
			L2 = Label(self.parent,text = "Találatok száma: %s    " % len(szamok), fg = "red", font = ('Comic Sans MS',12)).place(x=440,y=85)
			fromvalue = 1
		else:
			L3 = Label(self.parent,text = "Találatok száma: %s    " % 0, fg = "red", font = ('Comic Sans MS',12)).place(x=440,y=85)
			fromvalue = 0
			
		
			
		L3 = Label(self.parent,text = "Találat:    ", fg = "red", font = ('Comic Sans MS',12)).place(x=440,y=113)
		
		spinval = IntVar()
		if len(szamok) == 1: spinval.set("1")
		SB = Spinbox(self.parent, textvariable = spinval, from_=fromvalue, font = ('Comic Sans MS',12), width = 3, to=len(szamok), 
																									background = "grey", command = print_spinval ).place(x=510,y=115)
#		SB.bind('<Return>', callback)	

	def Write(sor):
	
		sor = sor-1
		self.text.delete(1.0, END) 
	
	
		myFile1 = open("szerzo.dat")
		lines = myFile1.readlines()
		self.text.insert(END, "Szerző: %s" % lines[sor]) 
		myFile1.close()
		
		myFile2 = open('fordito.dat')
		lines = myFile2.readlines()
		self.text.insert(END,"\nFordító: %s" % lines[sor]) 
		myFile2.close()
		
		myFile3 = open('cim.dat')
		lines = myFile3.readlines()
		self.text.insert(END, "\nCím: %s" % lines[sor]) 
		myFile3.close()
		
		myFile4 = open('mufaj.dat')
		lines = myFile4.readlines()
		self.text.insert(END, "\nMűfaj: %s" % lines[sor])
		myFile4.close()
		
		myFile5 = open('ev.dat')
		lines = myFile5.readlines()
		self.text.insert(END, "\nKiadás éve: %s" % lines[sor])
		myFile5.close()
		
		myFile6 = open('kiado.dat')
		lines = myFile6.readlines()
		self.text.insert(END, "\nKiadó: %s" % lines[sor])
		myFile6.close()
		
		myFile7 = open('tartalom.dat')
		lines = myFile7.readlines()
		self.text.insert(END, "\nTartalom: %s" % lines[sor])
		myFile7.close()
		
		myFile8 = open('megjegyzes.dat')
		lines = myFile8.readlines()
		self.text.insert(END, "\nMegjegyzés: %s" % lines[sor])
		myFile8.close()
		
	
	def Search(keres, lookup):
	
		if keres == "Szerzőkben": file = 'szerzo.dat'
		if keres == "Fordítókban": file = 'fordito.dat' 
		if keres == "Címekben": file = 'cim.dat' 
		if keres == "Műfajokban": file = 'mufaj.dat' 
		if keres == "Kiadási évek közt": file = 'ev.dat' 
		if keres == "Kiadók közt": file = 'kiado.dat'
		if keres == "Kötet tartalmában": file = 'tartalom.dat' 
		if keres == "Megjegyzésekben": file = 'megjegyzes.dat'
	
		self.text.delete(1.0, END) 
		szamok = []
		
		with open(file) as myFile:
				for num, line in enumerate(myFile, 1):
					if lookup in line:
						szamok.append(num)
						
		if not num: szamok = -1
		return szamok
		
#BUTTONS

	self.ExitButton = Button(self.parent, text='Kilépés', bg='grey', fg='red', 
								activebackground='black', activeforeground='green', command = self.parent.destroy ).place(x=550, y=555)
								
#	self.SearchButton = Button(self.parent, text='Keresés', bg='grey', fg='black', 
#								activebackground='black', activeforeground='green', command = callback ).place(x=370, y=95)
								
	self.DataBaseButton = Button(self.parent, text='Adatbázis', bg='grey', fg='red', 
							activebackground='black', activeforeground='green', command = DataBase ).place(x=50, y=555)

	
#MENU 

	SearchVariable = StringVar()
	SearchVariable.set("Szerzőkben") 
	self.SearchOptions = OptionMenu(self.parent, SearchVariable, "Szerzőkben", "Fordítókban", "Címekben", "Műfajokban", "Kiadási évek közt", "Kiadók közt", "Kötet tartalmában", "Megjegyzésekben")
	self.SearchOptions.place(x=180, y=118)
	
#TEXTBOX

	self.text = Text(self.parent, font = ('Comic Sans MS',12))
	self.text.place(x=50, y=160, width = 550, height = 370)

	
def DataBase():
	
	new = Toplevel()
	new.title('Adatbázis')		
	new.geometry("440x480+250+250")
	
	def Write_in():
	
			myFile1 = open("szerzo.dat","a")
			myFile1.write("\n")
			myFile1.write((entryvar1.get()).encode('utf-8'))
			myFile1.write("\n")
			myFile1.close()
			
			myFile2 = open('fordito.dat',"a")
			myFile2.write("\n")
			myFile2.write((entryvar2.get()).encode('utf-8'))
			myFile2.write("\n")
			myFile2.close()
					
			myFile3 = open('cim.dat',"a")
			myFile3.write("\n")
			myFile3.write((entryvar3.get()).encode('utf-8'))
			myFile3.write("\n")
			myFile3.close()
				
			myFile4 = open('mufaj.dat',"a")
			myFile4.write("\n")
			myFile4.write((entryvar4.get()).encode('utf-8'))
			myFile4.write("\n")
			myFile4.close()
				
			myFile5 = open('ev.dat',"a")
			myFile5.write("\n")
			myFile5.write((entryvar5.get()).encode('utf-8'))
			myFile5.write("\n")
			myFile5.close()
			
			myFile6 = open('kiado.dat',"a")
			myFile6.write("\n")
			myFile6.write((entryvar6.get()).encode('utf-8'))
			myFile6.write("\n")
			myFile6.close()
			
			myFile7 = open('tartalom.dat',"a")
			myFile7.write("\n")
			myFile7.write((entryvar7.get()).encode('utf-8'))
			myFile7.write("\n")
			myFile7.close()
			
			myFile8 = open('megjegyzes.dat',"a")
			myFile8.write("\n")
			myFile8.write((entryvar8.get()).encode('utf-8'))
			myFile8.write("\n")
			myFile8.close()
	
	new.OkButton = Button(new, text = "Bezár", bg='white', fg='red', 
						activebackground='black', activeforeground='green', command = new.destroy ).place(x = 350, y = 430)
							
	new.NewRecordButton = Button(new, text = "Új bejegyzés", bg='white', fg='red', 
						activebackground='black', activeforeground='green', command = Write_in ).place(x = 30, y = 430)
							
	new.L0 = Label(new, text = "Rekordok szerkesztése:", font = ('Comic Sans MS',12)).place(x=30,y=20)	

	
	new.L1 = Label(new, text = "Szerző:", font = ('Comic Sans MS',10)).place(x=30,y=50)
	new.L2 = Label(new, text = "Fordító:", font = ('Comic Sans MS',10)).place(x=30,y=95)
	new.L3 = Label(new, text = "Cím:", font = ('Comic Sans MS',10)).place(x=30,y=140)
	new.L4 = Label(new, text = "Műfaj:", font = ('Comic Sans MS',10)).place(x=30,y=185)
	new.L5 = Label(new, text = "Kiadás éve:", font = ('Comic Sans MS',10)).place(x=30,y=230)
	new.L6 = Label(new, text = "Kiadó:", font = ('Comic Sans MS',10)).place(x=30,y=275)
	new.L7 = Label(new, text = "Kötet tartalma:", font = ('Comic Sans MS',10)).place(x=30,y=320)
	new.L8 = Label(new, text = "Megjegyzés:", font = ('Comic Sans MS',10)).place(x=30,y=365)

	entryvar1 = StringVar()
	entryvar2 = StringVar()
	entryvar3 = StringVar()
	entryvar4 = StringVar()
	entryvar5 = StringVar()
	entryvar6 = StringVar()
	entryvar7 = StringVar()
	entryvar8 = StringVar()
	
	new.E1 = Entry(new, textvariable=entryvar1, width = 60)
	new.E1.place(x=32,y=70)
	
	new.E2 = Entry(new, textvariable=entryvar2, width = 60)
	new.E2.place(x=32,y=115)
	
	new.E3 = Entry(new, textvariable=entryvar3, width = 60)
	new.E3.place(x=32,y=160)
	
	new.E4 = Entry(new, textvariable=entryvar4, width = 60)
	new.E4.place(x=32,y=205)
	
	new.E5 = Entry(new, textvariable=entryvar5, width = 60)
	new.E5.place(x=32,y=250)
	
	new.E6 = Entry(new, textvariable=entryvar6, width = 60)
	new.E6.place(x=32,y=295)
	
	new.E7 = Entry(new, textvariable=entryvar7, width = 60)
	new.E7.place(x=32,y=340)
	
	new.E8 = Entry(new, textvariable=entryvar8, width = 60)
	new.E8.place(x=32,y=385)
	
	"""
	
	"""
	
	
	
def main():
    root = Tk()
    app = Application(root)
    root.geometry('640x600+200+200')
	
    app.mainloop()

main()

"""
import sys
import fileinput

def Delete(sor):

	fin = open( 'szerzo.dat', "r" )
	data_list = fin.readlines()
	fin.close()
	del data_list[sor-1] 
	fout = open("szerzo.dat", "w")
	fout.writelines(data_list)
	fout.close()
	
	fin = open( 'fordito.dat', "r" )
	data_list = fin.readlines()
	fin.close()
	del data_list[sor-1] 
	fout = open("fordito.dat", "w")
	fout.writelines(data_list)
	fout.close()
	
	fin = open( 'cim.dat', "r" )
	data_list = fin.readlines()
	fin.close()
	del data_list[sor-1] 
	fout = open("cim.dat", "w")
	fout.writelines(data_list)
	fout.close()
	
	fin = open( 'mufaj.dat', "r" )
	data_list = fin.readlines()
	fin.close()
	del data_list[sor-1] 
	fout = open("mufaj.dat", "w")
	fout.writelines(data_list)
	fout.close()
	
	fin = open( 'ev.dat', "r" )
	data_list = fin.readlines()
	fin.close()
	del data_list[sor-1] 
	fout = open("ev.dat", "w")
	fout.writelines(data_list)
	fout.close()
	
	fin = open( 'kiado.dat', "r" )
	data_list = fin.readlines()
	fin.close()
	del data_list[sor-1] 
	fout = open("kiado.dat", "w")
	fout.writelines(data_list)
	fout.close()
	
	fin = open( 'tartalom.dat', "r" )
	data_list = fin.readlines()
	fin.close()
	del data_list[sor-1] 
	fout = open("tartalom.dat", "w")
	fout.writelines(data_list)
	fout.close()
	
	fin = open( 'megjegyzes.dat', "r" )
	data_list = fin.readlines()
	fin.close()
	del data_list[sor-1] 
	fout = open("megjegyzes.dat", "w")
	fout.writelines(data_list)
	fout.close()
	
"""
