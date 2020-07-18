class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Illeana", "Joseph", "Kincaid", "Larry"]):
        students.sort()
        self.ChildsPlants = {child: [] for child in students}
        for row in diagram.splitlines():
            for idx, plantCode in enumerate(row):
                self.ChildsPlants[students[idx//2]].append(plantCode)

    def code_to_plant(self, char):
        PLANT_CODES = {"V": "Violets", "R": "Radishes", "G":"Grass", "C":"Clover"}
        return PLANT_CODES[char]

    def plants(self, child):
        print(self.ChildsPlants)
        print(self.ChildsPlants[child])
        return [self.code_to_plant(code) for code in self.ChildsPlants[child]]
            