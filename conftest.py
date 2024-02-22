import pytest

from BookCollector import BooksCollector

@pytest.fixture # фикстура, которая создаёт спиок из трех книг
def three_books():
    three_books = BooksCollector()
    # добавляем три книги
    three_books.add_new_book('Кристина')
    three_books.add_new_book('Сияние')
    three_books.add_new_book('10 негритят')
    # устанавливаем жанр книг
    three_books.set_book_genre('Кристина', 'Ужасы')
    three_books.set_book_genre('Сияние', 'Ужасы')
    three_books.set_book_genre('10 негритят', 'Детективы')
    return three_books

@pytest.fixture # фикстура, которая создаёт спиок книг для детей
def children_books():
    children_books = BooksCollector()
    # добавляем две книги
    children_books.add_new_book('Три поросенка')
    children_books.add_new_book('Золушка')
    # устанавливаем жанр для книг
    children_books.set_book_genre('Три поросенка', 'Мультфильмы')
    children_books.set_book_genre('Золушка', 'Мультфильмы')
    return children_books