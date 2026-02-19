class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        responses = [set(i) for i in responses]
        myList = []
        for i in responses:
            myList.extend(list(i))
        counter_responses = Counter(myList)
        max_val = max(counter_responses.values())
        mostCommons = [k for k, v in counter_responses.items() if v == max_val]
        return min(mostCommons)