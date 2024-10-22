def total_salary(path):
    salaries = []
    try:
        with open(path, 'r', encoding='utf-8') as file:

            for line in file:
                parts = line.strip().split(',')

                if len(parts) == 2:
                    salary = int(parts[1])
                    salaries.append(salary)
                else:
                    print(f'Skipping line due to incorrect format: "{line.strip()}"')
        
        sum_salaries = sum(salaries)
        avg_salary = int(sum_salaries / len(salaries) if salaries else 0)

        return sum_salaries, avg_salary

    except FileNotFoundError:
        print('File not found.')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None