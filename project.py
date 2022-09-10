from tkinter import *
from PIL import ImageTk, Image
import pyttsx3 
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound  


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)


def listen(text_val):
    language = 'te' 
    obj = gTTS(text=text_val, lang=language, slow=False) 
    obj.save("exam.mp3")  
    playsound("exam.mp3")

root=Tk()
root.geometry('750x750')
root.title("Project")
img1=ImageTk.PhotoImage(Image.open('Images/woolen.jpeg'))
label1=Label(root,image=img1).place(x=20,y=50)
label11=Label(root,text='ఉన్ని బట్టలుs').place(x=20,y=300)
button1=Button(root,text='క్లిక్ చేయండి',command=lambda:listen('ఉన్ని బట్టలుs')).place(x=120,y=300)

img2=ImageTk.PhotoImage(Image.open('Images/cotton.jpeg'))
label2=Label(root,image=img2).place(x=350,y=50)
label22=Label(root,text='పత్తి బట్టలు').place(x=350,y=300)
button2=Button(root,text='క్లిక్ చేయండి',command=lambda:listen('పత్తి బట్టలు')).place(x=430,y=300)

img3=ImageTk.PhotoImage(Image.open('Images/saree.jpeg'))
label3=Label(root,image=img3).place(x=20,y=400)
label33=Label(root,text='చీర').place(x=20,y=600)
button3=Button(root,text='క్లిక్ చేయండి',command=lambda:listen('చీర')).place(x=120,y=600)

img4=ImageTk.PhotoImage(Image.open('Images/kids.jpeg'))
label4=Label(root,image=img4).place(x=400,y=400)
label44=Label(root,text='పిల్లల బట్టలు').place(x=400,y=630)
button3=Button(root,text='క్లిక్ చేయండి',command=lambda:listen('పిల్లల బట్టలు')).place(x=500,y=630)


# img5=ImageTk.PhotoImage(Image.open('Images/mic.png'))  
Button(root, text = 'Click Me !').place(x=300,y=650)


root.mainloop()