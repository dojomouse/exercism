class Garden:
    STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Illeana', 'Joseph', 'Kincaid', 'Larry']
    PLANT_CODES = {'V': 'Violets', 'R': 'Radishes', 'G':'Grass', 'C':'Clover'}
    def __init__(self, diagram, students=STUDENTS):
        students.sort()
        self.StudentPlants = {student: [] for student in students}
        for row in diagram.splitlines():
            for idx, plantCode in enumerate(row):
                self.StudentPlants[students[idx//2]].append(plantCode)

    def plants(self, student):
        return [self.PLANT_CODES[code] for code in self.StudentPlants[student]]
            