def create_agenda(arrays):
    first = dict()
    level = first
    for my_list in arrays:
        for i in range(0, len(my_list)):
            try:
                if my_list[i] not in level:
                    level[my_list[i]] = {my_list[i+1]: {}}
            except IndexError:
                level[my_list[i]] = {}
            level = level[my_list[i]]
        level = first
    return first


def accepted(path, agenda):
    current_level = agenda
    for node in path:
        if node in current_level:
            current_level = current_level[node]
        else:
            return False
    return True