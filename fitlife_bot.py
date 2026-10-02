print('--------------------------------------------------')
print('FitLife Console Bot')
print('V.0.0001')
print('02.10.2026')
print('Generalov A. Aleksandr')
print('(Misticle)')
print('--------------------------------------------------')
print()

#code:
print('FitLife Bot: Приветствую тебя, мой маленький толстожопый друг!') #2) вежливо здоровается
print('FitLife Bot: Как тебя зовут? Напиши свое имя:')
user_name = input('новый пользователь:') #3.1) запрашивает имя
print('СИСТЕМА: Пользователь ->>>', user_name, '<<<- зарегистрирован в системе FitLife!')
print('FitLife Bot: О! мощно! А сколько тебе лет? укажи:')
user_age = int(input(user_name + ':')) #3.2) запрашивает возраст

if user_age <= 20:
    print('FitLife Bot: Молодой еще совсем! Значит энергии еще хоть отбавляй!')
elif user_age > 20 and user_age <= 40:
    print('FitLife Bot: В самом расцвете сил, значит?')
else:
    print('FitLife Bot: Солидный возраст, как я вижу')

print('FitLife Bot: Теперь я бы хотел узнать твои вес и рост.')
print('СИСТЕМА: Укажите свой вес, кг.')
user_weight = float(input(user_name + ':'))
print('СИСТЕМА: Теперь, укажите свой рост, м.')
user_height = float(input(user_name + ':'))

bmi = user_weight / (user_height ** 2) #Рассчитать индекс массы тела по формуле
bmi = round(bmi, 1) #Округлить результат до одного знака после запятой с помощью

water_ml = user_weight * 30 #Рассчитать норму воды в миллилитрах
water_l = water_ml / 1000. #Перевести в литры

print('FitLife Bot:', user_name, 'Я провел расчеты и готов предоставить отчет.')
print('СИСТЕМА: Отчет для пользователя: ', user_name, '(' + str(user_age), 'г.)') #Отчет для пользователя: Анна (25 г.)
print('FitLife Bot: Твой Индекс Массы Тела: ', bmi) #Твой Индекс Массы Тела: 22.3
print('FitLife Bot: Рекомендуемая норма воды: ', str(water_l), 'л. в день') #Рекомендуемая норма воды: 2.1 л. в день
print('FitLife Bot: Расчет окончен.', user_name, 'Будьте здоровы!') #Расчет окончен. Будьте здоровы!

