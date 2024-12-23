#!/usr/bin/env python3

class Equation:
    def __init__(self, result, members):
        self.result = result
        self.members = members

    def combine(self, results=None):
        """
        Returns the result of all left-to-right computations.
        """
        if results is None:
            results = [self.members[0]]  # Start with the first member

        # Base case: if there's only one member left, return results
        if len(self.members) == 1:
            return results

        new_results = []
        for r in results:
            # Compute left-to-right combinations
            new_results.append(r + self.members[1])
            new_results.append(r * self.members[1])
            new_results.append(int(str(r) + str(self.members[1])))

        # Recurse with the rest of the members
        remainder = Equation(None, self.members[1:])
        return remainder.combine(new_results)
    
    def is_valid(self):
        """
        This function checks whether a left-to-right combination
        of the members can produce the result
        """
        return self.result in self.combine()


equations = []
with open("inputs") as f:
    line = f.readline().rstrip()

    while line:
        first, second = line.split(': ')
        result = int(first)
        members = second.split(' ')
        members = list(map(int, members))
        equations.append(Equation(result, members))
        line = f.readline().rstrip()

count = 0
for e in equations:
    if e.is_valid():
        count += e.result
print(count)
