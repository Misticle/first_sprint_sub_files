print('--------------------------------------------------\n'
    'FitLife Console Bot\n'
    'V.1.00\n'
    '02.10.2026\n'
    'Generalov A. Aleksandr\n'
    '(Misticle)\n'
    '--------------------------------------------------\n')

#code:
print('FitLife Bot: Приветствую тебя, мой маленький толстожопый друг!\n' #2) вежливо здоровается
    'FitLife Bot: Как тебя зовут? Напиши свое имя:')
user_name = input('новый пользователь:') #3.1) запрашивает имя
print('СИСТЕМА: Пользователь ->>>', user_name, '<<<- зарегистрирован в системе FitLife!\n'
    'FitLife Bot: О! мощно! А сколько тебе лет? укажи:')
user_age = int(input(user_name + ':')) #3.2) запрашивает возраст

if user_age <= 20:
    print('FitLife Bot: Молодой еще совсем! Значит энергии еще хоть отбавляй!')
elif user_age > 20 and user_age <= 40:
    print('FitLife Bot: В самом расцвете сил, значит?')
else:
    print('FitLife Bot: Солидный возраст, как я вижу')

print('FitLife Bot: Теперь я бы хотел узнать твои вес и рост.\n'
    'СИСТЕМА: Укажите свой вес, кг.')
user_weight = float(input(user_name + ':'))
print('СИСТЕМА: Теперь, укажите свой рост, м.')
user_height = float(input(user_name + ':'))

bmi = user_weight / (user_height ** 2) #Рассчитать индекс массы тела по формуле
bmi = round(bmi, 1) #Округлить результат до одного знака после запятой с помощью

water_ml = user_weight * 30 #Рассчитать норму воды в миллилитрах
water_l = water_ml / 1000. #Перевести в литры

if user_age < 5:
    age_marker = str('г')
else:
    age_marker = str('л')

print('FitLife Bot:', user_name, 'Я провел расчеты и готов предоставить отчет.\n'
    'СИСТЕМА: Отчет для пользователя: ', user_name, '(' + str(user_age), age_marker + '.)\n'
    'FitLife Bot: Твой Индекс Массы Тела: ', bmi, '\n'
    'FitLife Bot: Рекомендуемая норма воды: ', str(water_l), 'л. в день\n'
    'FitLife Bot: Расчет окончен.', user_name, 'Будьте здоровы!')

