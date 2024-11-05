# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, separator=","):
    parts_first = first.split(separator)
    parts_second = second.split(separator)
    parts = []
    for i in range(len(parts_first)):
        for x in range(len(parts_second)):
            if parts_first[i] == parts_second[x]:
                parts.append(parts_second[x])
    parts.sort()
    return parts


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))