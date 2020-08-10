from tkinter import *
from tkinter.ttk import Combobox
window = Tk()
window.title('SCOUTING')
window.geometry("500x600+0+0")
window.resizable(False, False)

coutingTitle=Label(window, text="TEAM NAME - ", fg='black', font=("Helvetica", 25))
coutingTitle.place(x=5, y=5)

AutonPointsText=Label(window, text="How many auton points?", fg='black', font=("Helvetica", 10))
AutonPointsText.place(x=10, y=50)
AutonPointsInput=Entry()
AutonPointsInput.place(x=220, y=50)

OwnedMiddleText=Label(window, text="Do They Own Middle Tower?", fg='black', font=("Helvetica", 10))
v0=IntVar()
v0.set(1)
OwnedMiddleYES=Radiobutton(window, text="Yes", variable=v0,value=1)
OwnedMiddleNO=Radiobutton(window, text="No", variable=v0,value=2)
OwnedMiddleText.place(x=10, y=95)
OwnedMiddleYES.place(x=225,y=95)
OwnedMiddleNO.place(x=300, y=95)

ContributionText=Label(window, text="How much did they contribute?", fg='black', font=("Helvetica", 10))
ContributionSet =("1", "2", "3", "4","5","6","7","8","9","10")
ContributionInput=Combobox(window, values=ContributionSet)
ContributionText.place(x=10,y=140)
ContributionInput.place(x=210, y=140)

FinesseText=Label(window, text="How good is the driver?", fg='black', font=("Helvetica", 10))
FinesseSet =("1", "2", "3", "4","5","6","7","8","9","10")
FinesseInput=Combobox(window, values=FinesseSet)
FinesseText.place(x=10,y=185)
FinesseInput.place(x=210, y=185)

DriveTypeText=Label(window, text="What's the drive type?", fg='black', font=("Helvetica", 10))
DriveTypeText.place(x=10, y=230)
DriveTypeInput=Entry()
DriveTypeInput.place(x=220, y=230)

DriveSpeedText=Label(window, text="How fast is the drivebase?", fg='black', font=("Helvetica", 10))
DriveSpeedSet =("1", "2", "3", "4","5","6","7","8","9","10")
DriveSpeedInput=Combobox(window, values=DriveSpeedSet)
DriveSpeedText.place(x=10,y=275)
DriveSpeedInput.place(x=210, y=275)

IntakeSpeedText=Label(window, text="How fast are the intakes?", fg='black', font=("Helvetica", 10))
IntakeSpeedSet =("1", "2", "3", "4","5","6","7","8","9","10")
IntakeSpeedInput=Combobox(window, values=IntakeSpeedSet)
IntakeSpeedText.place(x=10,y=320)
IntakeSpeedInput.place(x=210, y=320)

BallCtrlText=Label(window, text="How well do they control balls?", fg='black', font=("Helvetica", 10))
BallCtrlSet =("1", "2", "3", "4","5","6","7","8","9","10")
BallCtrlInput=Combobox(window, values=BallCtrlSet)
BallCtrlText.place(x=10,y=365)
BallCtrlInput.place(x=210, y=365)

ScoringSpeedText=Label(window, text="How fast do they score?", fg='black', font=("Helvetica", 10))
ScoringSpeedSet =("1", "2", "3", "4","5","6","7","8","9","10")
ScoringSpeedInput=Combobox(window, values=ScoringSpeedSet)
ScoringSpeedText.place(x=10,y=410)
ScoringSpeedInput.place(x=210, y=410)

DefenceText=Label(window, text="How well do they defend?", fg='black', font=("Helvetica", 10))
DefenceSet =("1", "2", "3", "4","5","6","7","8","9","10")
DefenceInput=Combobox(window, values=DefenceSet)
DefenceText.place(x=10,y=455)
DefenceInput.place(x=210, y=455)

OwnedMiddleText=Label(window, text="Did They Win or Lose?", fg='black', font=("Helvetica", 10))
v1=IntVar()
v1.set(1)
OwnedMiddleYES=Radiobutton(window, text="Win", variable=v1,value=1)
OwnedMiddleNO=Radiobutton(window, text="Lose", variable=v1,value=2)
OwnedMiddleText.place(x=10, y=500)
OwnedMiddleYES.place(x=215,y=500)
OwnedMiddleNO.place(x=290, y=500)

SubmitButton = Button(text='SUBMIT!')
SubmitButton.place(x=250, y=550)


window.mainloop()

