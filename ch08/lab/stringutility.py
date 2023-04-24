class StringUtility:
    def __init__(self, string):
        self.string = string

    def __str__(self): ## passed
        return self.string

    def vowels(self): ## passed
        count = 0
        for ch in self.string:
            if ch == "a":
                count += 1
            if ch == "e":
                count += 1
            if ch == "i":
                count += 1
            if ch == "o":
                count += 1
            if ch == "u":
                count += 1
        if count < 5:
           return str(count)
        if count >= 5:
            return str("many")
        

        
    def bothEnds(self):
        if (len(self.string)) <= 2:
            return ""
        else:
            newstr = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
            return newstr


    def fixStart(self):
        if self.string == '':
            return ''
        firstnum = self.string[0]
        fixed = self.string[0] + self.string[1:].replace(firstnum, "*")
        return fixed

    def asciiSum(self):
        sum = 0
        for ch in self.string:
            sum += ord(ch)
        return sum
        

    def cipher(self):
        result = ""
        for ch in self.string:
            if ch.isalpha():
                start = ord('A') if ch.isupper() else ord('a')
                new_pos = (ord(ch) - start + len(self.string)) % 26
                ch = chr(start + new_pos)
            result += ch
            result = result.replace(self.string, ch)
        return result
