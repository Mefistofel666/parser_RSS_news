# parser_RSS_news
1.Описание:
Программа парсит новости с RSS лент и добавляет их в базу данных. В базе данных создаются две таблицы со всеми новостями и с отфильтрованными новостями.
Новости фильтруются по любым словам, для этого достаточно изменить массив с словами. 
Также в программе есть функция для удаления таблиц, чтения данных из базы данных 

Как работать: 
2.У программы нет интерфейса, но для того чтобы загружать другие новости достаточно добавить\удалить\заменить ссылки в массиве sites 
Для того, чтобы фильтровать по другим словам, достаточно изменить добавить\удалить\заменить слова в массиве words 
Для чтения данных из базы используется функция read_db, для удаления таблицы из базы используется функция delete_table_db. Достаточно их расскомментировать и передать соответсвующие аргументы.
