import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # тестируем add_new_book
    def test_add_new_book_addition_result(self):
        collector = BooksCollector()
        collector.add_new_book('Книга джунглей')                  # вызываем метод
        assert collector.books_genre['Книга джунглей'] == ''      # тестируем значение, которое он меняет, поскольку метод ничего не возвращает

    #тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # словарь имеет длину 2
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('set_genre', ["Мультфильмы"])
    def test_set_book_genre_get_genre(self, set_genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        set_book = 'Чебурашка'
        collector.add_new_book(set_book)
        collector.set_book_genre(set_book, set_genre)
        assert  collector.books_genre == {'Чебурашка': 'Мультфильмы'}

    # получаем жанр книги по её имени
    def test_get_book_genre_using_name(self, three_books):
        assert three_books.get_book_genre('Сияние') == 'Ужасы'

    # выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_horror(self, three_books):
        assert  'Кристина', 'Сияние' in three_books.get_books_with_specific_genre

    # получаем словарь books_genre
    def test_get_books_genre_from_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Сияние')
        collector.add_new_book('10 негритят')
        # устанавливаем жанр
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('10 негритят', 'Детективы')
        assert collector.get_books_genre() == {'Сияние': 'Ужасы', '10 негритят': 'Детективы'}

    # возвращаем книги, подходящие детям
    def test_get_books_for_children_set_result(self, children_books):
        assert (children_books.books_genre[children_books.get_books_for_children()[0]]  == 'Мультфильмы') and (children_books.books_genre[children_books.get_books_for_children()[1]]  == 'Мультфильмы')

    # добавляем книгу в Избранное
    def test_add_book_in_favorites_create_list(self, three_books):
        three_books.add_book_in_favorites('10 негритят')
        assert three_books.favorites[0] == '10 негритят'

    # # удаляем книгу из Избранного
    def test_delete_book_from_favorites_result(self, strange_book):
        strange_book.delete_book_from_favorites('Кристина')
        assert 'Кристина' not in strange_book.favorites

    # получаем список Избранных книг
    def test_get_list_of_favorites_books_result(self, favorite_books):
        assert favorite_books.get_list_of_favorites_books() == ['Чебурашка', 'Кристина', 'Сияние', '10 негритят']
