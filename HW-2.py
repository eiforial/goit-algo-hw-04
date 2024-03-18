path = 'cats_file.txt'  

def read_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r') as file:
            for line in file:
                cat_info = line.strip().split(',')
                cat_dict = {
                    "id": cat_info[0],
                    "name": cat_info[1],
                    "age": cat_info[2]
                }
                cats_list.append(cat_dict)
    except FileNotFoundError:
        print(f"Файл '{path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return cats_list

cats = read_cats_info(path)
for cat in cats:
    print(cat) 