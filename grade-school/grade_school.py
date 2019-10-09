class School(object):
    def __init__(self):
        self.roster_map = {}

    def add_student(self, name, grade):
        if grade in self.roster_map.keys():
            self.roster_map[grade].append(name)
        else:
            self.roster_map.update({grade:[name]})
    def roster(self):
        all_values = self.roster_map.values()
        #all_values = [val for val in all_values]
        return sorted(sum(all_values,[]))

    def grade(self, grade_number):
        if grade_number in self.roster_map.keys():
            return sorted(self.roster_map[grade_number])
        else:
            return []
