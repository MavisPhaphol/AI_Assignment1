import datetime


class study_planner:
    def __init__():
        self.assignments = [] #this will be a list of assignments that the user inputs
    
    def add_assignment(self, assignment):
        self.assignments.append(assignment) #this will add the assignment to the list of assignments
    
    def until_due_date(self, current_date):
        for assignment in self.assignments:
            time_remaining = assignment.due_date - current_date
            print(f"{assignment.name} is due in {time_remaining} days.") #test if this function works
    
    def calculate_priority(self):
        current_date=datetime.today() #this will get the current date
        for assignment in self.assignments:
            if assignment.difficulty == "hard" or assignment.due_date - current_date <= 3: #if the assignment is hard or due in 3 days or less, it will be a priority
                assignment.priority = 3
                print(f"{assignment.name} is a high priority assignment.") #test
            elif assignment.difficulty == "medium" or assignment.due_date - current_date <= 5: #if the assignment is medium or due in 5 days or less, it will be a priority
                assignment.priority = 2
                print(f"{assignment.name} is a medium priority assignment.") #test 
            else:
                assignment.priority = 1
                print(f"{assignment.name} is a low priority assignment.") #test

    def sort_assignments(self):
        self.assignments.sort(key=lambda x: (x.priority, x.due_date.timestamp()), reverse=True) #this will sort the assignments by priority and then by due date
        print("Assignments sorted by priority and due date:") #test
        for assignment in self.assignments:
            print(f"{assignment.name} - Priority: {assignment.priority}, Due Date: {assignment.due_date}") #test


