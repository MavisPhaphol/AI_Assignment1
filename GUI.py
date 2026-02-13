from tkinter import *
#use reference from youtube video: https://www.youtube.com/watch?v=lyoyTlltFVU 
window = Tk()
window.geometry("1280x720") #the window size
window.title("AI Agent GUI") #the title for the window screen
window.config(background="#343940") #background of window

#use reference from GeeksForGeeks: https://www.geeksforgeeks.org/python/python-tkinter-listbox-widget/
listbox = Listbox(window, height = 50, weight = 100, background="#495059",fg="white") #displays the assignments w/ due dates and priority in this list box
boxTitle = Label(window, text="Student Assignment Sorter") #title with listed box containing assignment information

#use reference from GeeksFor Geeks: https://www.geeksforgeeks.org/python/how-to-get-the-input-from-tkinter-text-box/
# and https://stackoverflow.com/questions/43148463/how-to-place-widgets-next-to-each-other/43149015#43149015
assignmentInput = Text(window,title="Assignment Title:",height = 10, width = 50) #text box for users to put assignment infomation
assignmentInput.pack()
dueDateInput = Text(window,title="Due Date:",height = 10, width = 20).grid(row=3,column=0,columnspan=5)
dueDateInput.pack()
priorityInput = Text(window,title="Priority:",height = 10, width = 20).grid(row=3,column=0,columnspan=5)
priorityInput.pack()
difficultyInput = Text(window,title="Difficulty:" ,height = 10, width = 20).grid(row=3,column=0,columnspan=5)
difficultyInput.pack()




window.mainloop() #this will display window size once you hit run