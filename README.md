## Проект YaMDb

#### Описание проекта:
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.


#### Как запустить проект:

##### Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:bauman1922/api_yamdb.git
```
```
cd api_yamdb
```
##### Cоздать и активировать виртуальное окружение:
``` 
python -m venv env
```
```
source venv/Scripts/activate
```
##### Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
##### Выполнить миграции:
```
python manage.py migrate
```
##### Запустить проект:
```
python manage.py runserver
```


##### После запуска проекта документация API будет доступна по адресу:
```
http://127.0.0.1:8000/redoc/
```

#### База данных:
Для загрузки данных в составе проекта используйте  management-команды, которые добавляют данные в базу данных через Django ORM.

После выполения миграций загрузить данные CSV из папки static проекта, можно с помощью следующих команд:
```
python manage.py load_csv_user
python manage.py load_csv_category
python manage.py load_csv_genre
python manage.py load_csv_title
python manage.py load_csv_review
python manage.py load_csv_comment
python manage.py load_csv_genre_title

```

#### Авторы проекта
* [Veronika Lapteva](https://github.com/VeronikaLapteva)
* [Daniil Malyshev](https://github.com/YaStirayuLaskoy)
* [Sergey Samorukov](https://github.com/bauman1922)