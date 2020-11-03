from tkinter import *
from tkinter import messagebox
import sys

#Set Up Screen
root = Tk()
root.title("Super Calculator V3.0 (Admin Beta Version)")
#root.attributes("-fullscree", True)
root.geometry("1350x680")
root.configure(bg = "Cadet Blue")

#Set Up The Var
WidthRecPerimeterVar = StringVar()
HeightRecPerimeterVar = StringVar()
WidthRecAreaimeterVar = StringVar()
HeightRecAreaimeterVar = StringVar()
SideSquarePerVar = StringVar()
SideSquareAreaVar = StringVar()
VarAns = StringVar()

#Define main Function
def clear_before_exit():
	WidthRecPerimeterVar.set("")
	HeightRecPerimeterVar.set("")
	WidthRecAreaimeterVar.set("")
	HeightRecAreaimeterVar.set("")
	VarAns.set("")

def Exit():
	root.destroy()
	sys.exit()

def clear_Per_Rec():
	VarAns.set("")
	WidthRecPerimeterVar.set("")
	HeightRecPerimeterVar.set("")

def clear_Area_Rec():
	VarAns.set("")
	WidthRecAreaimeterVar.set("")
	HeightRecAreaimeterVar.set("")

def clear_Per_Square():
	VarAns.set("")
	WidthRecPerimeterVar.set("")
	HeightRecPerimeterVar.set("")

def clear_Area_Square():
	VarAns.set("")
	WidthRecAreaimeterVar.set("")
	HeightRecAreaimeterVar.set("")

def calculate_Per_Rec():
	WidthRecPerimeterVar2 = int(WidthRecPerimeterVar.get())
	HeightRecPerimeterVar2 = int(HeightRecPerimeterVar.get())
	PerimeterRectAns = (WidthRecPerimeterVar2 + HeightRecPerimeterVar2) * 2
	VarAns.set(PerimeterRectAns)

def calculate_Area_Rec():
	WidthRecAreaimeterVar2 = int(WidthRecAreaimeterVar.get())
	HeightRecAreaimeterVar2 = int(HeightRecAreaimeterVar.get())
	AreaRectAns = WidthRecAreaimeterVar2 * HeightRecAreaimeterVar2
	VarAns.set(AreaRectAns)

def calculate_Per_Square():
	PerSquareAns = SideSquarePerVar * 4
	VarAns.set(PerSquareAns)

def calculate_Area_Square():
	pass

#License messageBox
def license():
	messagebox.showinfo(message = "This is A Free Program License")

def About_Program():
	messagebox.showinfo(message = "This Program is For Parent To Find The Answer Of The Area Or The Perimeter Of The Shapes")

def language():
	messagebox.showinfo(message = "This is English Version")

def About_Updates():
	messagebox.showinfo(message = "This is Version 3.0, Fix Bug")

def Check_Updates():
	messagebox.showinfo(message = "Go to https://github.com/loc-code To Get The Latest Version")

#Create The Menu
menuBar = Menu(root)
About = Menu(menuBar, tearoff=0)
About.add_command(label = "About License", command = license)
About.add_command(label = "About This Program", command = About_Program)
About.add_command(label = "Language",command = language)
About.add_separator()
About.add_command(label = "Exit", command = Exit)
menuBar.add_cascade(label = "About This Program", menu = About)
helper = Menu(menuBar, tearoff = 0)
helper.add_command(label = "About This Updates", command = About_Updates)
helper.add_command(label = "Check For Updates", command = Check_Updates)
menuBar.add_cascade(label = "Help", menu = helper)

#Define the TopLevel
def ChonDienTichChuViHinhVuong():
	ChonDienTichChuViHinhVuong = Toplevel(root)
	ChonDienTichChuViHinhVuong.geometry("500x500")
	ChonDienTichChuViHinhVuong.title("Choose The Function To Calculate")
	ChonDienTichChuViHinhVuong.configure(bg = "Cadet Blue")

	SelectRecLbl = Label(ChonDienTichChuViHinhVuong, text = "Please Select The Function To Calculate:", font = ("Arial 16 bold"), bg = "Cadet Blue")
	SelectRecLbl.pack(side = TOP, anchor = W)

	PerimeterSquare = Button(ChonDienTichChuViHinhVuong, text = "Perimeter Of Square", font = ("Arial 16 bold"), width = 23, height = 2, activebackground = "Lime", command = ChuViHinhVuong)
	PerimeterSquare.pack(side = TOP, anchor = W)
	areaSquare = Button(ChonDienTichChuViHinhVuong, text = "Area Of Square", font = ("Arial 16 bold"), width = 23, height = 2, activebackground = "Lime")
	areaSquare.pack(side = TOP, anchor = W)

def ChuViHinhVuong():
	ChuViHinhVuong = Toplevel(root)
	ChuViHinhVuong.geometry("600x600")
	ChuViHinhVuong.title("Perimeter Of Square")

	#Clear Before Function
	clear_before_exit()

	#Labels And Side Buttons
	typeSidelblPerRec = Label(ChuViHinhVuong, font = ("Arial 12 bold"), text = "Please Insert The Side Of The Square:")
	typeSidelblPerRec.pack(side = TOP, anchor = W)
	insertPerRecHeight = Entry(ChuViHinhVuong, font = ("Arial 12 bold"))
	insertPerRecHeight.pack(side = TOP, anchor = W)

	#Clear Buttons
	ClearButtons = Button(ChuViHinhVuong, text = "Clear", font = ("Arial 12 bold"), command = clear_Per_Square)
	ClearButtons.pack(side = TOP)

	#Calculate Buttons
	CalButtons = Button(ChuViHinhVuong, text = "Calculate", font = ("Arial 12 bold"))
	CalButtons.pack(side = TOP)

	#Answer Label
	Answerlbl = Label(ChuViHinhVuong, text = "Answer:", font = ("Arial 12 bold"))
	Answerlbl.pack(side = TOP)

	#Answer Entry Box
	answerEntryBox = Entry(ChuViHinhVuong, font = ("Arial 15 bold"), width = 20)
	answerEntryBox.pack(side = TOP)

def ChonDienTichChuViHinhChuNhat():
	ChonDienTichChuViHinhChuNhat = Toplevel(root)
	ChonDienTichChuViHinhChuNhat.geometry("500x500")
	ChonDienTichChuViHinhChuNhat.title("Choose The Function To Calculate")
	ChonDienTichChuViHinhChuNhat.configure(bg = "Cadet Blue")

	SelectRecLbl = Label(ChonDienTichChuViHinhChuNhat, text = "Please Select The Function To Calculate:", font = ("Arial 16 bold"), bg = "Cadet Blue")
	SelectRecLbl.pack(side = TOP, anchor = W)

	PerimeterRec = Button(ChonDienTichChuViHinhChuNhat, text = "Perimeter Of Square", font = ("Arial 16 bold"), width = 23, height = 2, activebackground = "Lime", command = ChuViHinhChuNhat)
	PerimeterRec.pack(side = TOP, anchor = W)
	areaRec = Button(ChonDienTichChuViHinhChuNhat, text = "Area Of Rectangle", font = ("Arial 16 bold"), width = 23, height = 2, activebackground = "Lime", command = DienTichHinhChuNhat)
	areaRec.pack(side = TOP, anchor = W)

def ChuViHinhChuNhat():
	ChuViHinhChuNhat = Toplevel(root)
	ChuViHinhChuNhat.geometry("600x600")
	ChuViHinhChuNhat.title("Perimeter Of Rectangle")

	#Clear Function
	clear_before_exit()

	#Labels And Width Buttons
	typeWidthlblPerRec = Label(ChuViHinhChuNhat, font = ("Arial 12 bold"), text = "Please Insert The Width Of The Rectangle:")
	typeWidthlblPerRec.pack(side = TOP, anchor = W)
	insertPerRecWidth = Entry(ChuViHinhChuNhat, font = ("Arial 12 bold"), textvariable = WidthRecPerimeterVar)
	insertPerRecWidth.pack(side = TOP, anchor = W)

	#Labels And Height Buttons
	typeHeightlblPerRec = Label(ChuViHinhChuNhat, font = ("Arial 12 bold"), text = "Please Insert The Height Of The Rectangle:")
	typeHeightlblPerRec.pack(side = TOP, anchor = W)
	insertPerRecHeight = Entry(ChuViHinhChuNhat, font = ("Arial 12 bold"), textvariable = HeightRecPerimeterVar)
	insertPerRecHeight.pack(side = TOP, anchor = W)

	#Clear Buttons
	ClearButtons = Button(ChuViHinhChuNhat, text = "Clear", font = ("Arial 12 bold"), command = clear_Per_Rec)
	ClearButtons.pack(side = TOP)

	#Calculate Buttons
	CalButtons = Button(ChuViHinhChuNhat, text = "Calculate", font = ("Arial 12 bold"), command = calculate_Per_Rec)
	CalButtons.pack(side = TOP)

	#Answer Label
	Answerlbl = Label(ChuViHinhChuNhat, text = "Answer:", font = ("Arial 12 bold"))
	Answerlbl.pack(side = TOP)

	#Answer Entry Box
	answerEntryBox = Entry(ChuViHinhChuNhat, font = ("Arial 15 bold"), width = 20, textvariable = VarAns)
	answerEntryBox.pack(side = TOP)

def DienTichHinhChuNhat():
	DienTichHinhChuNhat = Toplevel(root)
	DienTichHinhChuNhat.geometry("600x600")
	DienTichHinhChuNhat.title("Area Of Rectangle")

	#Clear Function
	clear_before_exit()

	#Labels And Width Buttons
	typeWidthlblAreaRec = Label(DienTichHinhChuNhat, font = ("Arial 12 bold"), text = "Please Insert The Width Of The Rectangle:")
	typeWidthlblAreaRec.pack(side = TOP, anchor = W)
	insertAreaRecWidth = Entry(DienTichHinhChuNhat, font = ("Arial 12 bold"), textvariable = WidthRecAreaimeterVar)
	insertAreaRecWidth.pack(side = TOP, anchor = W)

	#Labels And Height Buttons
	typeHeightlblAreaRec = Label(DienTichHinhChuNhat, font = ("Arial 12 bold"), text = "Please Insert The Height Of The Rectangle:")
	typeHeightlblAreaRec.pack(side = TOP, anchor = W)
	insertAreaRecHeight = Entry(DienTichHinhChuNhat, font = ("Arial 12 bold"), textvariable = HeightRecAreaimeterVar)
	insertAreaRecHeight.pack(side = TOP, anchor = W)

	#Clear Buttons
	ClearButtons = Button(DienTichHinhChuNhat, text = "Clear", font = ("Arial 12 bold"), command = clear_Area_Rec)
	ClearButtons.pack(side = TOP)

	#Calculate Buttons
	CalButtons = Button(DienTichHinhChuNhat, text = "Calculate", font = ("Arial 12 bold"), command = calculate_Area_Rec)
	CalButtons.pack(side = TOP)

	#Answer Label
	Answerlbl = Label(DienTichHinhChuNhat, text = "Answer:", font = ("Arial 12 bold"))
	Answerlbl.pack(side = TOP)

	#Answer Entry Box
	answerEntryBox = Entry(DienTichHinhChuNhat, font = ("Arial 15 bold"), width = 20, textvariable = VarAns)
	answerEntryBox.pack(side = TOP)

#Main Label
mainlbl = Label(root, text = "Super Calculator Program", bg = "Cadet Blue", font = "Arial 30 bold")
mainlbl.pack()

#Main Function
tinhHinhVuongBtn = Button(root, text = "Square", font = ("Arial 16 bold"), width = 18, height = 3, activebackground = "Lime", command = ChonDienTichChuViHinhVuong).pack(side = TOP, anchor = W)
tinhHinhChuNhatBtn = Button(root, text = "Rectangle", font = ("Arial 16 bold"), width = 18, height = 3, activebackground = "Lime", command = ChonDienTichChuViHinhChuNhat).pack(side = TOP, anchor = W)

#Exit Button

#LiencenceLbl
liceseLbl = Label(root, text = "Made By Tien Loc In 2020", font = "Arial 18 bold", bg = "Lime")
liceseLbl.pack(fill = BOTH, side = BOTTOM)

#Program mainloop
root.config(menu = menuBar)
root.mainloop()
