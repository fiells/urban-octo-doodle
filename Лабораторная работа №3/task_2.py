# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, split_=','):
    first = set(participants_first_group.split(split_))
    second = set(participants_second_group.split(split_))
    general_participants = list(first.intersection(second))
    general_participants.sort()
    return general_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, split_='|')