class Conversion:
    def convertntegertoromannumeral(self, integerinput):
        numerals = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X"
        }
        if integerinput not in numerals:
            result = "Integer out of range"
        else:
            result = numerals[integerinput]

        return result


convert = Conversion()
print("Please enter a number between 1 and 10: ")
integer = int(input())
romNumeral = convert.convertntegertoromannumeral(integer)
print(romNumeral)
