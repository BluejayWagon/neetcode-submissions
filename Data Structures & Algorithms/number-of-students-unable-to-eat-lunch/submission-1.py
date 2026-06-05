class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student1s = students.count(1)
        student0s = len(students) - student1s
        for i in range(len(sandwiches)):
            if sandwiches[i] == 0:
                student0s -= 1
            else:
                student1s -= 1
            if student0s == -1 or student1s == -1:
                break
        if student1s == -1:
            return student0s
        else:
            return student1s        