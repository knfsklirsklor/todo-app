# from functions import get_todos, write_todos
import functions
import time


now = time.strftime("%b %d %Y  %H:%M:%S")
print("Sejcas : ", now)
print('piskjjjja')

while True:
    action = input("Type add, show, done, edit or exit: ")
    action = action.strip()

    if action.startswith('add'):
        todo = action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos_arg=todos)

    elif action.startswith('show'):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title() # delaet vsio s bolshoj bukvi
            row = f'{index + 1}-{item}'
            print(row)
        print('Vsego: ', len(todos))
    elif action.startswith('exit'):
        break
    elif action.startswith('done'):
        try:
            number = int(action[5:])

            todos = functions.get_todos()
            index = number - 1
            toto_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos_arg=todos)

            message = f"{toto_remove} - bilo udalento iz spiska"
            print(message)
        except IndexError and ValueError:
            print("There is no item with that number.")
            continue
    elif action.startswith('edit'):
        try:
            number = int(action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos_arg=todos)
        except ValueError:
            print('Your command is not valid.')
            continue
    else:
        print("Napisal xujniu")

print("Done")

# while True:
#     ime = input("Vvedi svojo imia: ")
#     print(ime.capitalize())

# greeting = "hello"
# print(greeting.upper())

# countries = []
#
# while True:
#     country = input("Enter the country: ")
#     countries.append(country)
#     print(countries)