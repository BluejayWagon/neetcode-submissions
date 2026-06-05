class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentQueue = deque(students)
        count = 0
        while studentQueue and count < len(studentQueue):
            student = studentQueue.popleft()
            count += 1
            if student == sandwiches[0]:
                #student takes their sammy
                sandwiches.pop(0)
                count = 0
            else:
                #wrong sammy, student goes back in line
                studentQueue.append(student)
        return len(studentQueue)

                