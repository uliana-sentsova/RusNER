class Token:

    def __init__(self):
        self.surface = ""
        self.lemma = ""
        self.pos = ""
        self.grammar = ""
        self.annotation = []
        self.parent = 0
        self.syntax = ""

    def read(self, conll_line):
        conll_line = conll_line.strip().split("\t")
        self.surface = conll_line[1]
        self.lemma = conll_line[2]
        self.pos = conll_line[3]
        self.grammar = conll_line[4]
        self.syntax = conll_line[-3]
        self.parent = int(conll_line[-4])