import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def books_collector():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
    collector.add_new_book('Котенок Гав')
    collector.set_book_genre('Котенок Гав', 'Мультфильмы')
    collector.add_new_book('Веселые приключения')
    collector.set_book_genre('Веселые приключения', 'Комедии')
    return collector
