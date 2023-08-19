from tkinter import *
import pyshorteners
import pyperclip

root1 = Tk()
root1.title("URL Shortener")
root1.configure(bg="blue")

url = StringVar()
sortUrl= StringVar()

def urlshort():
    sort_Url= url.get()
    generateurl= pyshorteners.Shortener().tinyurl.short(sort_Url)
    sortUrl.set(generateurl)

def copy():
    generateurl= sortUrl.get()
    pyperclip.copy(generateurl)



Label(root1, text= "URL Shortener App", font= "Ariel").pack(pady= 11)
Entry(root1, textvariable= url).pack(pady= 6)
Button(root1, text= "Generate Url",command= urlshort).pack(pady= 6)
Entry (root1, textvariable= sortUrl).pack(pady= 6)
Button(root1, text= "Copy Url", command= copy).pack(pady=6)

root1.mainloop()

