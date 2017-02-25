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

tree = trees[2]
print([(token.surface, token.pos, token.parent) for token in tree.array])


NPs = {}
in_NP = []
root = tree.get_root()
print(root.surface)
children = tree.get_children(root.number)
print([ch.surface for ch in children])


# for token in tree.array:
#     if token.pos == "S":
#         children = tree.get_all_children(token.number)
#         print([token.surface] + [ch.surface for ch in children])
#         if not children:
#             continue
#
#         for child in children + [token]:
#             if child not in NPs:
#                 NPs[child.number] = [token] + children
#
#             if len(children) + 1 > len(NPs[child.number]):
#                 NPs[child.number] = [token] + children
#
#         #
#         # if token.number in NPs:
#         #     if len(NPs[token.number]) > len(children) + 1:
#         #         NPs[token.number] = [token] + children
#         # else:
#         #     NPs[token.number] = [token] + children
#
# for key in NPs:
#     print(key, [token.surface for token in NPs[key]])

        # if child.number in in_NP and len
        # for child in children: in_NP[child.number] = children
        #
        # print([ch.surface for ch in children])

#
# children = t.get_all_children(2)
# print([ch.surface for ch in children])
