# parser_RSS_news
# Описание:<br/> 
  1. Программа парсит новости с RSS лент и добавляет их в базу данных. В базе данных создаются две таблицы со всеми новостями и с отфильтрованными новостями. <br/>
  2. Новости фильтруются по любым словам, для этого достаточно изменить массив с словами. <br/>
  3. Также в программе есть функция для удаления таблиц, чтения данных из базы данных <br/>

# 2. Как работать: <br/> 
  1. У программы нет интерфейса, но для того чтобы загружать другие новости достаточно добавить\удалить\заменить ссылки в массиве sites <br/>
  2.Для того, чтобы фильтровать по другим словам, достаточно изменить добавить\удалить\заменить слова в массиве words <br/>
  3.Для чтения данных из базы используется функция read_db, для удаления таблицы из базы используется функция delete_table_db. Достаточно их расскомментировать и передать              соответсвующие аргументы.
