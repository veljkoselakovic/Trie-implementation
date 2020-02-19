
class TrieCvor:

    def __init__(self, vrednost: str, krajReci=False):

        self.vrednost = vrednost
        self.krajReci = krajReci
        self.deca = {}

    def add(self, rec: str) -> None:
        if len(rec) == 0:
            self.krajReci = True
            return

        prvo_slovo = rec[0]
        cvor = self.deca.setdefault(prvo_slovo, TrieCvor(prvo_slovo))
        cvor.add(rec[1:])

    def nadji(self, rec, path=""):
        if self.krajReci:
            yield path + self.vrednost, 0

        if len(rec) > 0:

            slovo = rec[0]
            cvor = self.deca.get(slovo)

            if cvor is None:
                pass
            else:
                yield from cvor.nadji(rec[1:], path + self.vrednost)
        else:
            for cvor in self.deca.values():
                yield from cvor.nadji("", path + self.vrednost)


print('Ucitavam reci')

import codecs
fileObj = codecs.open("recnik.txt", "r", "utf-8" )
words = fileObj.readlines()
#print(words)
root = TrieCvor("")



for word in words:
    root.add(word.rstrip('\r\n'))
    #print(word)
while True:
    rec = input()
    for word, _ in root.nadji(rec):
        print(word)
#print('2')
