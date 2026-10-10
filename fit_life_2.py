WATER_PER_KG = 30  # const: [мл/кг]
ML_IN_LITRE = 1000  # const: [л/мл]
BOT_NAME = 'FitLife Bot'
SYSTEM_NAME = 'СИСТЕМА'


def input_function(prompt, convert):
    while True:
        try:
            value = convert(input(prompt))
            return (value)
        except ValueError:
            print(f"{SYSTEM_NAME}: Ошибка!")

print(f'{BOT_NAME}: Приветствую тебя, дружище! Добро пожаловать в FitLife!')
user_name = input(f'{BOT_NAME}: Как тебя зовут? Напиши свое имя.\n'
                  'новый пользователь: ')
print(f'{SYSTEM_NAME}: Пользователь ->>> {user_name} <<<- зарегистрирован в '
      'системе FitLife!\n'
      f'{BOT_NAME}: О! мощно! А сколько тебе лет?')

user_age = input_function(f'{SYSTEM_NAME}: Укажите свой возраст числом '
                          f'(например, 25).\n{user_name}: ', int)

if user_age <= 20:
    print(f'{BOT_NAME}: Молодой еще совсем! Значит энергии еще хоть отбавляй!')
elif user_age <= 40:
    print(f'{BOT_NAME}: В самом расцвете сил, значит?')
else:
    print(f'{BOT_NAME}: Солидный возраст, как я погляжу')

print(f'{BOT_NAME}: Теперь я бы хотел узнать твои вес и рост.\n')

user_weight = input_function(f'{SYSTEM_NAME}: Укажите свой вес, кг '
                             f'(например, 75).\n{user_name}: ', float)

user_height = input_function(f'{SYSTEM_NAME}: Укажите свой рост, '
                             'м. в виде числа c дробной частью в '
                             f'метрах (например, 1.75)\n{user_name}: ', float)

bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_IN_LITRE

if user_age < 5:
    age_marker = 'г'  # от 1 до 4 лет возраст - это год/года (г.)
else:
    age_marker = 'л'  # от 5 лет возраст - это лет (л.)

print(f'{BOT_NAME}: {user_name} Я провел расчеты и готов предоставить '
      'отчет!\n\n'
      f'Отчет для пользователя: {user_name} {user_age}, {age_marker}.\n'
      f'Твой Индекс Массы Тела: {bmi}\n'
      f'Рекомендуемая норма воды: {water_l:.2f} л. в день\n'
      f'Расчет окончен. {user_name} Будьте здоровы!')
