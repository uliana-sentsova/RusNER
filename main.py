from subprocess import call

script_path = "/Users/ulyanasidorova/Development/RusNER/ru-syntax/ru-syntax.py"
in_path = "/Users/ulyanasidorova/Development/RusNER/test.txt"
out_path = "/Users/ulyanasidorova/Development/RusNER/result.txt"
syntax_call_line = "python3"
call(["python3", script_path, "-o", out_path, in_path])

arr = []
with open(out_path, 'r', encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        line = line.strip().split("\t")
        arr.append(line[-4])
        print(line)
        # print("\t".join([line[0], line[1], line[-4], line[-3]]))

