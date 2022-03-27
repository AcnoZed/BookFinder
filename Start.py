from flask import Flask, render_template, redirect, request
from models.Book import Book
from data.BookDB import BookDB

app = Flask(__name__)
books = BookDB()

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        req = request.form 
        book = Book(req.get('title'), req.get('author'), req.get('genre'))
        books.add(book)
        print(req)
        if books is not None:
            for book in books.get_books():
                book.printBook()
        
        return redirect(request.url)
    

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

    