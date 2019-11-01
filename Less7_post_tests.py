import unittest
from module_CRUD_books import CRUD


class PostTests(unittest.TestCase):

    def setUp(self):
        self.body_positive = {"title": "Iliad", "author": "Homer"}
        self.operations = CRUD()
        self.book_response = self.operations.create_book(self.body_positive)
        self.book = self.book_response.json()

    def test_check_that_book_was_created(self):
        self.assertEqual(201, self.book_response.status_code)
        self.assertEqual(self.body_positive["title"], self.book["title"])
        self.assertEqual(self.body_positive["author"], self.book["author"])

# test_check_that_book_with_the_existing_id_was_created_with_the_new_one0

    def test_check_that_book_with_the_existing_id_was_not_created(self):
        body_with_id = {"title": "Iliad", "author": "Homer", "id": str(self.book["id"])}
        book_response = self.operations.create_book(body_with_id)
        self.assertEqual(201, book_response.status_code)
        book2 = book_response.json()
        self.assertNotEqual(self.book["id"], book2["id"])
        self.assertEqual(body_with_id["title"], book2["title"])
        self.assertEqual(body_with_id["author"], book2["author"])

    # def test_check_that_changing_data_with_existing_id_is_ok(self):
    #     self.body_with_changed_data = {"title": "Iliad and Odyssey", "author": "Homer"}
    #     book_response = self.operations.update_book(self.book["id"], self.body_with_changed_data)
    #     self.book2 = book_response.json()
    #     self.assertEqual(self.book2["id"], self.book["id"])
    #     self. assertNotEqual(self.body_with_changed_data["title"], self.book2["title"])
    #     self.assertEqual(self.body_with_changed_data["author"], self.book2["author"])


test_create = PostTests('test_check_that_book_was_created')
test_negative_create = PostTests('test_check_that_book_with_the_existing_id_was_not_created')
# test_change_created = PostTests("test_check_that_changing_data_with_existing_id_is_ok")
test_create.run()
test_negative_create.run()
# test_change_created.run()


