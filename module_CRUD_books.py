import requests


class CRUD:
    host = 'http://pulse-rest-testing.herokuapp.com/'
    book_url = 'books'

    def create_book(self, body):
        book_response = requests.post(url=self.host + self.book_url, data=body)
        return book_response

    def get_book(self, book_id):
        book_response = requests.get(url=self.host + self.book_url + '/' + str(book_id))
        return book_response

    def update_book(self, book_id, body_updated_book):
        updated_book_response = requests.put(url=self.host + self.book_url + '/' + str(book_id),
                                             data=body_updated_book)
        return updated_book_response

    def delete_book(self, book_id):
        deleted_book_response = requests.delete(url=self.host + self.book_url + '/' + str(book_id))
        return deleted_book_response



    # updated_book_access = requests.get(url=host + book_url + '/' + str(book_id))
    # print(updated_book_access.json())


# host = 'http://pulse-rest-testing.herokuapp.com/'
# book_url = 'books'
# body_created_book = {"title": "Illiad", "author": "Homer"}

# создаем книгу
# book_response = requests.post(url=host + book_url,  data=body_created_book)
# my_book = book_response.json()

# CRUD_object = CRUD()
# my_book = CRUD_object.create_book(body_created_book)
# book_id = my_book['id']
# print(my_book)
# print(book_id)

# book_check_response = requests.get(url=host + book_url+'/'+str(book_id))
# book_check = book_check_response.json()

# проверяем наличие

# assert body_created_book["title"] == book_check["title"]
# assert body_created_book["author"] == book_check["author"]
# print(book_check["title"] + ' ' + book_check["author"])

# вносим изменения

# body_updated_book = {"title": "Iliad and Odyssey", "author": "Homer"}
#
# updated_book_response = requests.put(url=host + book_url+'/'+str(book_id), data=body_updated_book)
# updated_book = updated_book_response.json()
#
# # проверяем изменения
# assert body_updated_book["title"] == updated_book["title"]
# assert body_updated_book["author"] == updated_book["author"]
# print(updated_book["title"], updated_book["author"])
#
# # проверяем доступность по ссылке
#
# updated_book_access = requests.get(url=host + book_url+'/'+str(book_id))
# print(updated_book_access.json())
#
# # удаляем
#
# delete_book_response = requests.delete(url=host + book_url+'/'+str(book_id))
# check_deleted_book_response = requests.get(url=host + book_url+'/'+str(book_id))
# print(check_deleted_book_response.status_code)
# assert check_deleted_book_response.status_code == 404
# print('Not found')

