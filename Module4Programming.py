from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
 
app = Flask(__name__) 
 
# Configure SQLite database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db' 
db = SQLAlchemy(app) 
 
# Book Model 
class Book(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    book_name = db.Column(db.String(80), unique=True, nullable=False) 
    author = db.Column(db.String(120), nullable=False) 
    publisher = db.Column(db.String(120)) 
     
    def __repr__(self): 
        return f"{self.book_name} by {self.author}" 
 
# Initialize Database (Run Once) 
with app.app_context(): 
    db.create_all() 
 
# ===================== 
# ROUTES / ENDPOINTS 
# ===================== 
 
@app.route('/') 
def index(): 
    '''Home route''' 
    return 'Welcome to the Book API!' 
 
# READ ALL - Get all books 
@app.route('/books') 
def get_books(): 
    """Retrieve all books""" 
    books = Book.query.all() 
     
    output = [] 
    for book in books: 
        book_data = { 
            'id': book.id, 
            'book_name': book.book_name, 
            'author': book.author, 
            'publisher': book.publisher 
        } 
        output.append(book_data) 
     
    return {'books': output} 
 
# READ ONE - Get a specific book by ID 
@app.route('/books/<int:id>') 
def get_book(id): 
    """Retrieve a single book by ID""" 
    book = Book.query.get_or_404(id) 
    return { 
        'id': book.id, 
        'book_name': book.book_name, 
        'author': book.author, 
        'publisher': book.publisher 
    } 
 
# CREATE - Add a new book 
@app.route('/books', methods=['POST']) 
def add_book(): 
    """Add a new book to the database""" 
    # Extract data from JSON request body 
    new_book = Book( 
        book_name=request.json['book_name'], 
        author=request.json['author'], 
        publisher=request.json.get('publisher', '')  # Optional field 
    ) 
     
    db.session.add(new_book) 
    db.session.commit() 
     
    return {'id': new_book.id}, 201  # Return created status 
 
# UPDATE - Replace entire book (PUT) 
@app.route('/books/<int:id>', methods=['PUT']) 
def update_book(id): 
    """Update an existing book""" 
    book = Book.query.get_or_404(id) 
     
    book.book_name = request.json.get('book_name', book.book_name) 
    book.author = request.json.get('author', book.author) 
    book.publisher = request.json.get('publisher', book.publisher) 
     
    db.session.commit() 
     
    return { 
        'id': book.id, 
        'book_name': book.book_name, 
        'author': book.author, 
        'publisher': book.publisher 
    } 
 
# PATCH - Partially update a book 
@app.route('/books/<int:id>', methods=['PATCH']) 
def patch_book(id): 
    """Partially update a book""" 
    book = Book.query.get_or_404(id) 
     
    if 'book_name' in request.json: 
        book.book_name = request.json['book_name'] 
    if 'author' in request.json: 
        book.author = request.json['author'] 
    if 'publisher' in request.json: 
        book.publisher = request.json['publisher'] 
     
    db.session.commit() 
     
    return { 
        'id': book.id, 
        'book_name': book.book_name, 
        'author': book.author, 
        'publisher': book.publisher 
    } 
 
# DELETE - Remove a book 
@app.route('/books/<int:id>', methods=['DELETE']) 
def delete_book(id): 
    """Delete a book""" 
    book = Book.query.get(id) 
    if book is None: 
        return {"error": "Book not found"}, 404 
     
    db.session.delete(book) 
    db.session.commit() 
     
    return {'message': 'Book deleted successfully'} 
 
# Run the application 
if __name__ == '__main__': 
    app.run(debug=True) 