# Generated by Django 4.2.1 on 2023-05-23 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0013_alter_student_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(choices=[('', 'Выберите Страну'), ('Австралия', 'Австралия'), ('Австрия', 'Австрия'), ('Азербайджан', 'Азербайджан'), ('Албания', 'Албания'), ('Алжир', 'Алжир'), ('Американское Самоа', 'Американское Самоа'), ('Ангилья', 'Ангилья'), ('Ангола', 'Ангола'), ('Андорра', 'Андорра'), ('Антарктика', 'Антарктика'), ('Антигуа и Барбуда', 'Антигуа и Барбуда'), ('Аргентина', 'Аргентина'), ('Армения', 'Армения'), ('Аруба', 'Аруба'), ('Афганистан', 'Афганистан'), ('Багамы', 'Багамы'), ('Бангладеш', 'Бангладеш'), ('Барбадос', 'Барбадос'), ('Бахрейн', 'Бахрейн'), ('Беларусь', 'Беларусь'), ('Белиз', 'Белиз'), ('Бельгия', 'Бельгия'), ('Бенин', 'Бенин'), ('Бермудские Острова', 'Бермудские Острова'), ('Болгария', 'Болгария'), ('Боливия', 'Боливия'), ('Босния и Герцеговина', 'Босния и Герцеговина'), ('Ботсвана', 'Ботсвана'), ('Бразилия', 'Бразилия'), ('Британская территория в Индийском Океане', 'Британская территория в Индийском Океане'), ('Британские Виргинские острова', 'Британские Виргинские острова'), ('Бруней-Даруссалам', 'Бруней-Даруссалам'), ('Буркина-Фасо', 'Буркина-Фасо'), ('Бурунди', 'Бурунди'), ('Бутан', 'Бутан'), ('Вануату', 'Вануату'), ('Великобритания', 'Великобритания'), ('Венгрия', 'Венгрия'), ('Виргинские острова (США)', 'Виргинские острова (США)'), ('Внешние малые острова США', 'Внешние малые острова США'), ('Восточный Тимор (Тимор-Лесте)', 'Восточный Тимор (Тимор-Лесте)'), ('Вьетнам', 'Вьетнам'), ('Габон', 'Габон'), ('Гаити', 'Гаити'), ('Гайана', 'Гайана'), ('Гамбия', 'Гамбия'), ('Гана', 'Гана'), ('Гваделупа', 'Гваделупа'), ('Гватемала', 'Гватемала'), ('Гвинея', 'Гвинея'), ('Германия', 'Германия'), ('Гибралтар', 'Гибралтар'), ('Гондурас', 'Гондурас'), ('Гонконг', 'Гонконг'), ('Гренада', 'Гренада'), ('Гренландия', 'Гренландия'), ('Греция', 'Греция'), ('Грузия', 'Грузия'), ('Гуам', 'Гуам'), ('Дания', 'Дания'), ('Демократическая Республика Конго', 'Демократическая Республика Конго'), ('Джибути', 'Джибути'), ('Доминика', 'Доминика'), ('Доминиканская Республика', 'Доминиканская Республика'), ('Египет', 'Египет'), ('Западная Сахара', 'Западная Сахара'), ('Зимбабве', 'Зимбабве'), ('Израиль', 'Израиль'), ('Индия', 'Индия'), ('Индонезия', 'Индонезия'), ('Иордания', 'Иордания'), ('Ирак', 'Ирак'), ('Иран, Исламская Республика', 'Иран, Исламская Республика'), ('Ирландия', 'Ирландия'), ('Исландия', 'Исландия'), ('Испания', 'Испания'), ('Италия', 'Италия'), ('Йемен', 'Йемен'), ('Кабо-Верде', 'Кабо-Верде'), ('Казахстан', 'Казахстан'), ('Каймановы Острова', 'Каймановы Острова'), ('Камбоджа', 'Камбоджа'), ('Камерун', 'Камерун'), ('Канада', 'Канада'), ('Катар', 'Катар'), ('Кения', 'Кения'), ('Кипр', 'Кипр'), ('Киргизия', 'Киргизия'), ('Кирибати', 'Кирибати'), ('Китай', 'Китай'), ('Кокосовые (Килинг) Острова', 'Кокосовые (Килинг) Острова'), ('Колумбия', 'Колумбия'), ('Коморы', 'Коморы'), ('Конго', 'Конго'), ('Корейская Народно-Демократическая Республика', 'Корейская Народно-Демократическая Республика'), ('Корея, Республика', 'Корея, Республика'), ('Коста-Рика', 'Коста-Рика'), ("Кот-д'Ивуар", "Кот-д'Ивуар"), ('Куба', 'Куба'), ('Кувейт', 'Кувейт'), ('Лаосская Народно-Демократическая Республика', 'Лаосская Народно-Демократическая Республика'), ('Латвия', 'Латвия'), ('Лесото', 'Лесото'), ('Либерия', 'Либерия'), ('Ливан', 'Ливан'), ('Ливийская Арабская Джамахирия', 'Ливийская Арабская Джамахирия'), ('Литва', 'Литва'), ('Лихтенштейн', 'Лихтенштейн'), ('Люксембург', 'Люксембург'), ('Маврикий', 'Маврикий'), ('Мавритания', 'Мавритания'), ('Мадагаскар', 'Мадагаскар'), ('Майотта', 'Майотта'), ('Македония, Бывшая Югославская Республика', 'Македония, Бывшая Югославская Республика'), ('Малави', 'Малави'), ('Малайзия', 'Малайзия'), ('Мали', 'Мали'), ('Мальдивы', 'Мальдивы'), ('Мальта', 'Мальта'), ('Марокко', 'Марокко'), ('Мартиника', 'Мартиника'), ('Маршалловы Острова', 'Маршалловы Острова'), ('Мексика', 'Мексика'), ('Микронезия, Федеративные Штаты', 'Микронезия, Федеративные Штаты'), ('Мозамбик', 'Мозамбик'), ('Молдова, Республика', 'Молдова, Республика'), ('Монако', 'Монако'), ('Монголия', 'Монголия'), ('Монтсеррат', 'Монтсеррат'), ('Мьянма (Бирма)', 'Мьянма (Бирма)'), ('Намибия', 'Намибия'), ('Науру', 'Науру'), ('Непал', 'Непал'), ('Нигер', 'Нигер'), ('Нигерия', 'Нигерия'), ('Нидерландские Антильские острова', 'Нидерландские Антильские острова'), ('Нидерланды', 'Нидерланды'), ('Никарагуа', 'Никарагуа'), ('Ниуэ', 'Ниуэ'), ('Новая Зеландия', 'Новая Зеландия'), ('Новая Каледония', 'Новая Каледония'), ('Норвегия', 'Норвегия'), ('Объединенная Республика Танзания', 'Объединенная Республика Танзания'), ('Объединенные Арабские Эмираты', 'Объединенные Арабские Эмираты'), ('Оккупированная территория Палестинская', 'Оккупированная территория Палестинская'), ('Оман', 'Оман'), ('Остров Буве', 'Остров Буве'), ('Остров Норфолк', 'Остров Норфолк'), ('Остров Рождества', 'Остров Рождества'), ('Остров Святой Елены', 'Остров Святой Елены'), ('Остров Херд и острова Макдональд', 'Остров Херд и острова Макдональд'), ('Острова Кука', 'Острова Кука'), ('Пакистан', 'Пакистан'), ('Палау', 'Палау'), ('Панама', 'Панама'), ('Папуа-Новая Гвинея', 'Папуа-Новая Гвинея'), ('Парагвай', 'Парагвай'), ('Перу', 'Перу'), ('Питкэрн', 'Питкэрн'), ('Польша', 'Польша'), ('Португалия', 'Португалия'), ('Пуэрто-Рико', 'Пуэрто-Рико'), ('Реюньон', 'Реюньон'), ('Российская Федерация', 'Российская Федерация'), ('Руанда', 'Руанда'), ('Румыния', 'Румыния'), ('Сальвадор', 'Сальвадор'), ('Самоа', 'Самоа'), ('Сан-Марино', 'Сан-Марино'), ('Сан-Томе и Принсипи', 'Сан-Томе и Принсипи'), ('Саудовская Аравия', 'Саудовская Аравия'), ('Свазиленд', 'Свазиленд'), ('Северные Марианские острова', 'Северные Марианские острова'), ('Сейшельские Острова', 'Сейшельские Острова'), ('Сен-Пьер и Микелон', 'Сен-Пьер и Микелон'), ('Сенегал', 'Сенегал'), ('Сент-Винсент и Гренадины', 'Сент-Винсент и Гренадины'), ('Сент-Китс и Невис', 'Сент-Китс и Невис'), ('Сент-Люсия', 'Сент-Люсия'), ('Сербия и Черногория', 'Сербия и Черногория'), ('Сингапур', 'Сингапур'), ('Сирийская арабская республика', 'Сирийская арабская республика'), ('Словакия', 'Словакия'), ('Словения', 'Словения'), ('Соединенные Штаты', 'Соединенные Штаты'), ('Соломоновы Острова', 'Соломоновы Острова'), ('Сомали', 'Сомали'), ('Судан', 'Судан'), ('Суринам', 'Суринам'), ('Сьерра-Леоне', 'Сьерра-Леоне'), ('Таджикистан', 'Таджикистан'), ('Таиланд', 'Таиланд'), ('Тайвань, провинция Китая', 'Тайвань, провинция Китая'), ('Теркс и Кайкос', 'Теркс и Кайкос'), ('Того', 'Того'), ('Токелау', 'Токелау'), ('Тонга', 'Тонга'), ('Тринидад и Тобаго', 'Тринидад и Тобаго'), ('Тувалу', 'Тувалу'), ('Тунис', 'Тунис'), ('Туркменистан', 'Туркменистан'), ('Турция', 'Турция'), ('Уганда', 'Уганда'), ('Узбекистан', 'Узбекистан'), ('Украина', 'Украина'), ('Уоллис и Футуна', 'Уоллис и Футуна'), ('Уругвай', 'Уругвай'), ('Фарерские острова', 'Фарерские острова'), ('Фиджи', 'Фиджи'), ('Филиппины', 'Филиппины'), ('Финляндия', 'Финляндия'), ('Фолклендские острова (Мальвинские)', 'Фолклендские острова (Мальвинские)'), ('Франция', 'Франция'), ('Французская Гвиана', 'Французская Гвиана'), ('Французская Полинезия', 'Французская Полинезия'), ('Французские Южные и Антарктические территории', 'Французские Южные и Антарктические территории'), ('Хорватия', 'Хорватия'), ('Центральноафриканская Республика', 'Центральноафриканская Республика'), ('Чад', 'Чад'), ('Чехия', 'Чехия'), ('Чили', 'Чили'), ('Швейцария', 'Швейцария'), ('Швеция', 'Швеция'), ('Шпицберген и Ян-Майен', 'Шпицберген и Ян-Майен'), ('Шри-Ланка', 'Шри-Ланка'), ('Эдакао (Аомынь)', 'Эдакао (Аомынь)'), ('Эквадор', 'Эквадор'), ('Экваториальная Гвинея', 'Экваториальная Гвинея'), ('Эритрея', 'Эритрея'), ('Эстония', 'Эстония'), ('Эфиопия', 'Эфиопия'), ('Южная Георгия и Южные Сандвичевы острова', 'Южная Георгия и Южные Сандвичевы острова'), ('Южно-Африканская Республика', 'Южно-Африканская Республика'), ('Ямайка', 'Ямайка'), ('Япония', 'Япония')], max_length=100, null=True),
        ),
    ]
