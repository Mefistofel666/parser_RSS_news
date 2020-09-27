# Подключение библиотек
import sqlite3
import feedparser
import os
import re

# Глобальные переменные
all_table = 'core_fes'
certain_table = 'certain_news'
data_base = 'all_news_posts.db'
df_certain_news = []  # массив куда добавятся все отфильтрованные по словам новости
df_all_news = []  # массив куда добавятся все новости


# Слова по которым происходит фильтрация
words = [r'\bфутбол\S*', r'\bхоккей\S*', r'\bбаскетбол\S*',
         r'\bзвезд\S*', r'\bчемпионат\S*', r'\bсборная россии\S*', r'\bРФ\S*']


# Функция добавления в массив существующих ссылок на посты(чтоб добавлять только новые посты в дальнейшем)
def read_existing_links(db, table):
    all_news = []
    links = []
    if os.path.exists(db):
        all_news = read_db(db, table)
        all_news = list(map(list, all_news))
    for news in all_news:
        links.append(news[4])
    return links


# Функция удаления данных из базы данных
def delete_table_db(database, table):
    con = sqlite3.connect(database)
    cur = con.cursor()
    query = 'DROP TABLE IF EXISTS '+table
    cur.execute(query)
    cur.close()
    con.close()

# Функция чтения данных из базы данных


def read_db(db, table, column_name=None):
    con = sqlite3.connect(db)
    cur = con.cursor()

    if column_name is None:
        query = f'SELECT * FROM '+table
        cur.execute(query)
        data = cur.fetchall()
    else:
        query = 'SELECT ' + column_name + ' FROM ' + table
        cur.execute(query)
        data = cur.fetchall()

    cur.close()
    con.close()
    return data


# функция создания базы данных
def create_db(data, db_name, table):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute(
        f'CREATE TABLE IF NOT EXISTS {table}(Источник TEXT, Канал TEXT, Заголовок TEXT, Описание TEXT, Новость TEXT, Дата TEXT )')

    for data_unit in data:
        cur.execute(f'INSERT INTO {table} VALUES(?,?,?,?,?,?)', data_unit)

    con.commit()
    cur.close()
    con.close()


# Создание массивов с ссылками на новости которые уже есть в БД
links = read_existing_links(data_base, all_table)
certain_links = read_existing_links(data_base, certain_table)


# Массив с сыллками на rss-ленты
sites = ['https://lenta.ru/rss/', 'https://www.kommersant.ru/RSS/news.xml',
         'https://www.vesti.ru/vesti.rss', 'http://www.alltoday.ru/rss2/rss_sport.xml']


# Вывод информации о работе в консоль
for site in sites:
    d = feedparser.parse(site)
    print("\nИдет работа с сайтом: ", site)
    d.feed.title = (d.feed.title).replace('<![CDATA[ ', '')
    print("Наименование канала: \"" + (d.feed.title).replace(']]>', ''), "\"")
    print('Кол-во постов:', len(d.entries))

    for post in range(0, len(d.entries)):
        # наполнение таблицы всех постов
        news = [d.feed.title, d.feed.link, d.entries[post].title,
                d.entries[post].description, d.entries[post].link, d.entries[post].published]
        if news[4] not in links:
            df_all_news.append(news)

        # фильтр по словам
        for word in words:
            # поиск слов в описании поста
            match1 = re.search(
                word.lower(), (d.entries[post].description).lower())
            # поиск слов в заголовке поста
            match2 = re.search(word.lower(), (d.entries[post].title).lower())
            if match1 or match2:
                # текущая новость
                current_certain_news = [d.feed.title, d.feed.link, d.entries[post].title, d.entries[post].description,
                                        d.entries[post].link, d.entries[post].published]
                # добавление новости, если ее еще не было
                if current_certain_news[4] not in certain_links:
                    df_certain_news.append(current_certain_news)


# Вывозы функций
# Создание базы данных
create_db(df_all_news, data_base, all_table)
create_db(df_certain_news, data_base, certain_table)

# Чтение данных из базы
# read_db(data_base, all_table)

# Удаление таблицы из базы данных
# delete_table_db(data_base, all_table)
