from main import BooksCollector
import pytest


class TestBooksCollector:

    # 1. Добавление книг в словарь books_genre
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # 2. Книга не добавляется, если она уже есть в словаре
    def test_add_new_book_cant_add_same_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    # 3. Книга не добавлется, если ее название > 40 символов или без названия
    @pytest.mark.parametrize('incorrect_name', ['', 'Гордость, гордость, гордость и предубеждения'])
    def test_add_new_book_cant_add_book_without_name_or_name_more_then_40_symbols(self, incorrect_name):
        collector = BooksCollector()
        collector.add_new_book(incorrect_name)
        assert collector.get_books_genre() == {}

    # 4. Установка жанра у книги
    def test_set_book_genre_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы'}

    # 5. Жанр у книги не устанавливается, если ее нет в books_genre
    def test_set_book_genre_set_genre_without_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_genre() == {}

    # 6. Вывод жанра книги по ее названию
    def test_get_book_genre_get_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    # 7. Жанр у книги не выводится, если книги нет в books_genre
    def test_get_book_genre_cant_get_genre(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Гордость и предубеждение и зомби') is None

    # 8. Получения словаря
    def test_get_books_genre_get_books_genre(self, books_collector):
        assert books_collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы',
                                                     'Что делать, если ваш кот хочет вас убить': 'Детективы',
                                                     'Котенок Гав': 'Мультфильмы',
                                                     'Веселые приключения': 'Комедии'}

    # 9. Вывод книг с определенным жанром
    def test_get_books_with_specific_genre_get_books_with_specific_genre(self, books_collector):
        assert books_collector.get_books_with_specific_genre('Комедии') == ['Веселые приключения']

    # 10. Вывод книг, подходящих детям
    def test_get_books_for_children_get_books(self, books_collector):
        assert books_collector.get_books_for_children() == ['Котенок Гав', 'Веселые приключения']

    # 11. Добавление книги в избранное
    def test_add_book_in_favorites_add_one_book_in_favorites(self, books_collector):
        books_collector.add_book_in_favorites('Котенок Гав')
        assert 'Котенок Гав' in books_collector.get_list_of_favorites_books()

    # 12. Книга не добавляется, если она уже есть в избранном
    def test_add_book_in_favorites_cant_add_same_book_in_favorites(self, books_collector):
        books_collector.add_book_in_favorites('Котенок Гав')
        books_collector.add_book_in_favorites('Котенок Гав')
        assert len(books_collector.get_list_of_favorites_books()) == 1

    # 13. Удаление книги из избранного
    def test_delete_book_from_favorites_delete_one_book(self, books_collector):
        books_collector.add_book_in_favorites('Котенок Гав')
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        books_collector.delete_book_from_favorites('Котенок Гав')
        assert 'Котенок Гав' not in books_collector.get_list_of_favorites_books()

    # 14. Список избранного остается прежним, если удалить книгу, которой нет в избранном
    def test_delete_book_from_favorites_cant_delete_book_not_in_favorites(self, books_collector):
        books_collector.add_book_in_favorites('Котенок Гав')
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        books_collector.delete_book_from_favorites('Веселые приключения')
        assert books_collector.get_list_of_favorites_books() == ['Котенок Гав', 'Гордость и предубеждение и зомби']

    # 15. Получение списка избранных книг
    def test_get_list_of_favorites_books_get_list(self, books_collector):
        books_collector.add_book_in_favorites('Котенок Гав')
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert books_collector.get_list_of_favorites_books() == ['Котенок Гав', 'Гордость и предубеждение и зомби']
