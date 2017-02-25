from Token import Token
from Tree import Tree
from subprocess import call

script_path = "/Users/ulyanasidorova/Development/ru-syntax/ru-syntax.py"
in_path = "/Users/ulyanasidorova/Development/RusNER/test.txt"
out_path = "/Users/ulyanasidorova/Development/ru-syntax/out/result.txt"
syntax_call_line = "python3"
# call(["python3", script_path, "-o", out_path, in_path])

sentences = []
prev = 0
current_sentence = []

with open(out_path, 'r', encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        token = Token()
        token.read(line)
        # print(line)

        current = token.number
        if prev > current:
            sentences.append(current_sentence)
            current_sentence = []
        current_sentence.append(token)
        prev = current

trees = []
for sent in sentences:
    tree = Tree(len(sent))
    for token in sent:
        tree.add_elem(token.number, token)
    trees.append(tree)

# 6,5,12 – проблемные
tree = trees[6]
print([(token.surface, token.syntax, token.parent, token.pos) for token in tree.array])

# Поиск снизу:
NPs = {}
for token in tree.array:
    if token.pos == "S":
        children = tree.get_all_children(token.number)
        if not children:
            continue

        phrase = [token] + children
        phrase.sort(key=lambda x:x.number)
        phrase = [p for p in phrase if p.syntax != "PUNC"]
        print(" ".join([p.surface for p in phrase]))


# Поиск сверху:
# NPs = {}
# in_NP = []
# root = tree.get_root()
# print(root.surface)
# children = tree.get_children(root.number)
# # print([ch.surface for ch in children])
# for child in children:
#     if child.pos == "S":
#         NP = tree.get_all_children(child.number)
#         print(" ".join([child.surface] + [n.surface for n in NP]))