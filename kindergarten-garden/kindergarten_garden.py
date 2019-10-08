given_students = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry"]

class Garden(object):
    def __init__(self, diagram, students=given_students):
        diagram = diagram.splitlines()
        self.row1 = diagram[0]
        self.row2 = diagram[1]
        self.students = sorted(students)

    @staticmethod
    def _mapping_(plant_char):
        if plant_char == 'G':
            return "Grass"
        elif plant_char == 'C':
            return "Clover"
        elif plant_char == 'R':
            return "Radishes"
        elif plant_char == 'V':
            return "Violets"
        else:
            return ""

    def plants(self, student):
        try:
            index = self.students.index(student)
        except ValueError:
            print("student not enrolled")
        #as each child gets 2 cups
        index *= 2
        new = self.row1[index] + self.row1[index+1] + self.row2[index] + self.row2[index+1]
        return list(map(self._mapping_,new))