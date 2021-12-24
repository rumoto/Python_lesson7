def get_data(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            name = line.strip()
            number_recipe = int(file.readline().strip())
            list_dish = []
            for ingredients in range(number_recipe):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                ingredient_dict = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
                list_dish.append(ingredient_dict)
            cook_book[name] = list_dish
            file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    result = get_data('recipes.txt')
    for dish in dishes:
        if dish in result.keys():
            for ingredients in result[dish]:
                quantity_result = ingredients['quantity'] * person_count
                quantity_dict = {'measure': ingredients['measure'], 'quantity': quantity_result}
                name = ingredients['ingredient_name']
                if name not in shop_list.keys():
                    shop_list[name] = quantity_dict
                else:
                    shop_list_items = shop_list.get(name)
                    shop_list_items['quantity'] = shop_list_items['quantity'] + quantity_result
                    shop_list[name] = shop_list_items
    return shop_list

ingredients_list = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
print(ingredients_list)