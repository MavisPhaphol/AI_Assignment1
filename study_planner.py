from datetime import datetime

class study_planner:
    def __init__(self):
        self.assignments = [] #this will be a list of assignments that the user inputs


    def add_assignment(self,assignment):
        self.assignments.append(assignment) #this will add the assignment to the list of assignments

    def until_due_date(self, current_date):
        for assignment in self.assignments:
            time_remaining = assignment.due_date - current_date

    def calculate_priority(self):
        current_date = datetime.today() #this will get the current date
        for assignment in self.assignments:
            remaining_days = (assignment.due_date - current_date).days
            if assignment.difficulty == "hard" or remaining_days <= 3: #if the assignment is hard or due in 3 days or less, it will be a priority
                assignment.priority = 3
            elif assignment.difficulty == "medium" or remaining_days <= 5: #if the assignment is medium or due in 5 days or less, it will be a priority
                assignment.priority = 2
            else:
                assignment.priority = 1

    def sort_assignments(self):
        self.assignments.sort(key=lambda x: (x.priority, x.due_date.timestamp()),reverse=True) #this will sort the assignments by priority and then by due date