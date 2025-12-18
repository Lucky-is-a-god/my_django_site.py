name = str(input('введите имя'))
family = str(input('введите фамилию'))

print( f'"Привет! {name} {family}')
print( f' "Привет!" \n {name} {family}')
full = f"{name} {family}"
print(f"привет! {full.title()}")
# так же бывают и другие виды title, upper (пишет весь текст капсом), lower(пишет все буквы маленькими)