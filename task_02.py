def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:

            for line in file:
                parts = line.strip().split(',')

                if len(parts) == 3:
                    cats.append({'id': parts[0], 'name': parts[1], 'age': parts[2]})
                else:
                    print(f'Skipping line due to incorrect format: "{line.strip()}"')

        return cats

    except FileNotFoundError:
        print('File not found.')
        return []
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return []