class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        result = set()

        def is_valid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = {s}

        while queue:
            for x in queue:
                if is_valid(x):
                    result.add(x)

            if result:
                return list(result)

            next_queue = set()

            for x in queue:
                for i in range(len(x)):
                    if x[i] in "()":
                        new_string = x[:i] + x[i + 1:]
                        next_queue.add(new_string)

            queue = next_queue

        return [""]