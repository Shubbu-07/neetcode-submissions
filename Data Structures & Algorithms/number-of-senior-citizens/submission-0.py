class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passenger in details:
            age = passenger[11] + passenger[12]
            age = int(age)

            if age > 60:
                count += 1

        return count