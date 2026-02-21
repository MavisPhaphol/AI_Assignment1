from tkinter import *
from study_planner import study_planner

#use reference from youtube video: https://www.youtube.com/watch?v=lyoyTlltFVU 
window = Tk()
window.geometry("1280x720") #the window size
window.title("AI Agent GUI") #the title for the window screen
window.config(background="#343940") #background of window

#use reference from GeeksForGeeks: https://www.geeksforgeeks.org/python/python-tkinter-listbox-widget/
listbox = Listbox(window, height = 50, width = 100, background="#495059",fg="white") #displays the assignments w/ due dates and priority in this list box
boxTitle = Label(window, text="Student Assignment Sorter") #title with listed box containing assignment information
boxTitle.pack() #this will display the title for the list box
listbox.pack() #this will display the list box on the window

#use reference from GeeksFor Geeks: https://www.geeksforgeeks.org/python/how-to-get-the-input-from-tkinter-text-box/
# and https://stackoverflow.com/questions/43148463/how-to-place-widgets-next-to-each-other/43149015#43149015
assignmentLabel = Label(window, text="Assignment Title:", fg="white", background="#343940")
assignmentLabel.pack()
assignmentInput = Text(window, height = 5, width = 20) #text box for users to put assignment infomation
assignmentInput.pack() 
dueDateLabel = Label(window, text="Due Date:", fg="white", background="#343940")
dueDateLabel.pack()
dueDateInput = Text(window, height = 5, width = 20)
dueDateInput.pack()
difficultyLabel = Label(window, text="Difficulty:", fg="white", background="#343940")
difficultyLabel.pack()
difficultyInput = Text(window, height = 5, width = 20)
difficultyInput.pack()

smartStudyPlanner=study_planner()

def add_assignment_gui():
    assignmentTitle = assignmentInput.Entry()
    dueDate = dueDateInput.Entry()
    difficulty = difficultyInput.Entry()
    smartStudyPlanner.add_assignment(assignmentTitle, dueDate, difficulty) #this will add the assignment to the study planner when the button is clicked

def generate_planner():
    smartStudyPlanner.calculate_priority() #this will calculate the priority of the assignments when the button is clicked
    smartStudyPlanner.sort_assignments() #this will sort the assignments by priority and due date when the button is clicked
    listbox.delete(0, END) #this will clear the list box before displaying the sorted assignments
    for assignment in smartStudyPlanner.assignments:
        listbox.insert(END, f"{assignment["name"]} - Due: {assignment.due_date} - Difficulty: {assignment.difficulty} - Priority: {assignment.priority}") #this will display the sorted assignment information in the list box

#this will be the button to add the assignment information to the study planner
button=Button(window, text="Add Assignment", command=add_assignment_gui)
button.pack()

#this will be the button to generate the sorted assignment list in the list box
secondButton=Button(window, text="Generate Study Planner", command=generate_planner)
secondButton.pack()

window.mainloop() #this will display window size once you hit run