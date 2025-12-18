from name_function import get_formatted_name
print("Enter 'g' at any time to quit")
while True:
    First = input('\nPlease give me a first name: ')
    if First== 'q':
        break
    Last= input("\n Please give me a last name: ")
    if Last == 'q':
        break
    formatted_name = get_formatted_name(First, Last)
    print(f"\tNeatly formatted name : {formatted_name}  ")


