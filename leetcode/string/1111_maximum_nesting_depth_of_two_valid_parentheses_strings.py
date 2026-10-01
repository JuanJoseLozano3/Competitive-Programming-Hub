class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        levels = [0] * len(seq)
        depth = 0
        max_depth = 0

        for i, char in enumerate(seq):
            if char == "(":
                depth += 1
                levels[i] = depth
                max_depth = max(max_depth, depth)
            else:
                levels[i] = depth
                depth -= 1

        best_cutoff = 0
        best_score = len(seq) + 1
        for cutoff in range(max_depth + 1):
            score = max(cutoff, max_depth - cutoff)
            if score < best_score:
                best_score = score
                best_cutoff = cutoff

        return [0 if level <= best_cutoff else 1 for level in levels]