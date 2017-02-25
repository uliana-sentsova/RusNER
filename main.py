from Token import Token
from Tree import Tree
from subprocess import call

script_path = "/Users/ulyanasidorova/Development/ru-syntax/ru-syntax.py"
in_path = "/Users/ulyanasidorova/Development/RusNER/test.txt"
out_path = "/Users/ulyanasidorova/Development/RusNER/result.txt"
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

t = trees[2]
print([(token.surface, token.number, token.parent) for token in t.array])

children = t.get_all_children(2)
print([ch.surface for ch in children])
