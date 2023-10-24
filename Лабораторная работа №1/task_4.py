users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
general_amount = {
    'Общее количество':0,
    'Уникальные посещения':0
}
general_amount['Общее количество'] = len(users)
general_amount['Уникальные посещения'] = len(set(users))

print(general_amount)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
