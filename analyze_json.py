import json

with open(r"C:\Users\zinch\OneDrive\Рабочий стол\скилфэктори", "r", encoding="utf-8") as my_file:
    order_list = json.load(my_file)

max_order = max(order_list.items(), key=lambda x: x[1]['price'])
print(f'Номер заказа с самой большой стоимостью: {max_order[0]}, стоимость заказа: {max_order[1]["price"]}')

max_quantity_order = max(order_list.items(), key=lambda x: x[1]['quantity'])
print(f'Номер заказа с самым большим количеством товаров: {max_quantity_order[0]}')

july_orders = {}
for order_data in order_list.values():
    date_parts = order_data['date'].split('-')
    date = (int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))  # (year, day, month)
    if date[2] == 7 and date[0] == 2023:
        july_orders[date[1]] = july_orders.get(date[1], 0) + 1

if july_orders:
    max_orders_day = max(july_orders, key=july_orders.get)
    print(f'День в июле с наибольшим количеством заказов: {max_orders_day}')
else:
    print('В июле не было заказов')

user_orders_count = {}
for order_data in order_list.values():
    date_parts = order_data['date'].split('-')
    date = (int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))  # (year, day, month)
    if date[2] == 7 and date[0] == 2023:
        user_id = order_data['user_id']
        user_orders_count[user_id] = user_orders_count.get(user_id, 0) + 1

if user_orders_count:
    max_user_orders = max(user_orders_count, key=user_orders_count.get)
    print(f'Пользователь с самым большим количеством заказов за июль: {max_user_orders}')
else:
    print('В июле не было заказов')

user_total_price = {}
for order_data in order_list.values():
    date_parts = order_data['date'].split('-')
    date = (int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))  # (year, day, month)
    if date[2] == 7 and date[0] == 2023:
        user_id = order_data['user_id']
        user_total_price[user_id] = user_total_price.get(user_id, 0) + order_data['price']

if user_total_price:
    max_user_total_price = max(user_total_price, key=user_total_price.get)
    print(f'Пользователь с самой большой суммарной стоимостью заказов за июль: {max_user_total_price}')
else:
    print('В июле не было заказов')

total_price = 0
total_orders = 0
for order_data in order_list.values():
    date_parts = order_data['date'].split('-')
    date = (int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))  # (year, day, month)
    if date[2] == 7 and date[0] == 2023:
        total_price += order_data['price']
        total_orders += 1

average_order_price = total_price / total_orders if total_orders else 0
print(f'Средняя стоимость заказа в июле: {average_order_price}')

total_quantity = 0
total_price = 0
for order_data in order_list.values():
    date_parts = order_data['date'].split('-')
    date = (int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))  # (year, day, month)
    if date[2] == 7 and date[0] == 2023:
        total_quantity += order_data['quantity']
        total_price += order_data['price']

average_item_price = total_price / total_quantity if total_quantity else 0
print(f'Средняя стоимость товаров в июле: {average_item_price}')
