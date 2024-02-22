Проект содержит три основных файла: main.py, test.py и conftest.py

В файле main.py создан класс BooksCollector, каждый элемент которого имеет:

1. Словарь книг self.books_genre (при созаднии элемента класса  - пустой) с указанием одного из четырех возможных жанров (Название фильма (ключ) : Жанр книги (значение))
2. Список избранных книг (только навания) - self.favorites (при созаднии элемента класса  - пустой)
3. Жанры книг self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
4. Список жанров для определенной возрастной категории self.genre_age_rating = ['Ужасы', 'Детективы']

В классе созданы методы для работы с новыми и существующими эелементами:

1. Добавить новую книгу     add_new_book(self, name)
2. Устанавливить книге жанр   set_book_genre(self, name, genre)
3. Получить жанр книги по её имени    get_book_genre(self, name)
4. Получить список книг с определённым жанром    get_books_with_specific_genre(self, genre)
5. Получить словарь books_genre для элемента класса     get_books_genre(self)
6. Получить список книг, подходящих для детей    get_books_for_children(self)
7. Добавить книгу в список избранных книг    add_book_in_favorites(self, name)
8. Удалить книгу из Избранного списка   delete_book_from_favorites(self, name)
9. Получаем список Избранных книг     get_list_of_favorites_books(self)


В файле test.py создан класс Test_BooksCollector, в котором созданы методы для проверки (тестирования) корректной работы методов класса BooksCollector:
1. Добавление книги   test_add_new_book_addition_result(self)
2. Добавление двух книг   test_add_new_book_add_two_books(self)
3. Установка жанра для книги     test_set_book_genre_get_genre(self, name='Чебурашка', genre='Мультфильмы')
4. Получение жанра книги по её имени     test_get_book_genre_using_name(self, three_books)
5. Вывод списка книг с определённым жанром     test_get_books_with_specific_genre_horror(self, three_books)
6. Получение словаря books_genre      test_get_books_genre_from_two_books(self)
7. Получение списка книг, подходящих для детей    test_get_books_for_children_set_result(self, children_books)
8. Добавление книги в Избранное     test_add_book_in_favorites_create_list(self, three_books)
9. Удаление книги из Избранного списка    test_delete_book_from_favorites_result(self, three_books, first_book)
10. Получение списка Избранных книг    test_get_list_of_favorites_books_result(self, three_books)

  
В проекте создан файл conftest.py, в котором хранятся два созданных элемента класса для проверки методов тестового класса Test_BooksCollector:
1. three_books - элемент класса BooksCollector, в котором имеются три книги с указанными жанрами
2. children_books - элемент класса BooksCollector, в котором имеются две книги с жанром "Мультфильмы"