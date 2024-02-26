import pytest
from main import BooksCollector

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

@pytest.fixture # фикстура, которая создаёт спиcок книг для детей
def children_books():
    children_books = BooksCollector()
    # добавляем две книги
    children_books.add_new_book('Три поросенка')
    children_books.add_new_book('Золушка')
    # устанавливаем жанр для книг
    children_books.set_book_genre('Три поросенка', 'Мультфильмы')
    children_books.set_book_genre('Золушка', 'Мультфильмы')
    return children_books

@pytest.fixture # фикстура, которая создаёт спиcок избранных книг
def favorite_books():
    favorite_books = BooksCollector()

    # добавляем книгу
    favorite_books.add_new_book('Чебурашка')
    favorite_books.add_new_book('Кристина')
    favorite_books.add_new_book('Сияние')
    favorite_books.add_new_book('10 негритят')
    favorite_books.add_book_in_favorites('Чебурашка')
    favorite_books.add_book_in_favorites('Кристина')
    favorite_books.add_book_in_favorites('Сияние')
    favorite_books.add_book_in_favorites('10 негритят')
    return favorite_books

@pytest.fixture  # фикстура, которая создаёт спиcок избранных книг
def strange_book():
    strange_book = BooksCollector()
    strange_book.books_genre = {'Чебурашка': 'Мультфильмы', 'Кристина': 'Ужасы', 'Сияние': 'Ужасы', '10 негритят': 'Детективы'}
    strange_book.favorites = ['Чебурашка', 'Кристина', 'Сияние', '10 негритят']
    return strange_book
