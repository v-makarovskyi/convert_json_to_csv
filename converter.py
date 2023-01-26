import json

if __name__ == '__main__':
    try:
        with open('input.json') as f:
            data = json.loads(f.read())

        output = ', '.join([*data[0]])
        for x in data:
            output += f'\n{x["Name"]}, {x["age"]}, {x["birthyear"]}'
        
        with open('output.csv', 'w') as f:
            f.write(output)

    
    except Exception as _ex:
        print(f'Error: {str(_ex)}')