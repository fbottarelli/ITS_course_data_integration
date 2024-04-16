from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy database of books as a list of dictionaries
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell', 'year': 1949},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960}
]

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

# Route to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify(book)

# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    if not request.json or not 'title' in request.json:
        return jsonify({'message': 'Invalid request'}), 400
    book = {
        'id': books[-1]['id'] + 1 if books else 1,
        'title': request.json['title'],
        'author': request.json.get('author', ""),
        'year': request.json.get('year', None)
    }
    books.append(book)
    return jsonify(book), 201

if __name__ == '__main__':
    app.run(debug=True)
