def solve(n):
    anagram = set([])
    for i in range(n):
        word1 = input()
        word2 = "".join(sorted(word1))
        if word2 not in anagram:
            print(word1)
            anagram.add(word2)
solve(4)