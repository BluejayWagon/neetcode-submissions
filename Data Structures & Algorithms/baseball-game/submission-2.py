class Solution:
    def calPoints(self, operations: List[str]) -> int:
        finalScores = []
        for i in range(len(operations)):
            op = operations[i]
            if op == '+':
                prevScore = finalScores.pop()
                prevPrevScore = finalScores[-1]
                newScore = int(prevScore) + int(prevPrevScore)
                finalScores.append(prevScore)
                finalScores.append(newScore)
            elif op == 'D':
                prevScore = finalScores[-1]
                finalScores.append(int(prevScore) * 2)
            elif op == 'C':
                finalScores.pop()
            else:
                finalScores.append(int(op))
        return sum(finalScores)
