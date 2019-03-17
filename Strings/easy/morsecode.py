class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                      ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                      "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        v = set()

        for i in words:
            aa = list(i)
            i = 0
            s = ""
            for n in aa:
                b = morse_code[letters.index(aa[i])]
                i += 1
                s += b

            v.add(s)

        return len(v)
