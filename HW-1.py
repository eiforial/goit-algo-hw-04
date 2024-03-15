file_path = "text.txt" 

def total_salary(path):

    try:
        total = 0
        count = 0

        with open(path, encoding = "utf-8") as file:
            for line in file:
                _, salary = line.strip().split(',')
                total += int(salary)
                count += 1

        average = total / count 
        return total, average
    
    except FileNotFoundError:
        print("Файл не найден.")
   
total, average = total_salary(file_path)

print(f"Общая сумма зарплаты: {total} Средняя зарплата: {average}")
