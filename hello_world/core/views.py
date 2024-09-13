
from ..models import Book
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Book



def index(request):
    books = Book.objects.all()
    book_count = books.count()  # Get the total number of books
    print("Books", books)
    context = {
        "title": "Django example",
        "books": books,
        "book_count": book_count
        
    }
    return render(request, "index.html", context)


@csrf_exempt
@csrf_exempt
# TO-DO - The add_book functionality has already been built below. Make sure it works, add a book to the library. 
# TO-DO - Add logic in the add_book function so that after a book is added in the post request, the user is redirected back to the index/home page.
# TO-DO - You can also add a "Home" or "Back" button in the /templates/add_book.html file if you would prefer to solve this through the UI. 

def add_book(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            book = Book.objects.create(
                title=data['title'],
                author=data['author'],
                published_date=data['published_date'],
                isbn=data['isbn'],
                price=data['price'],
                stock_quantity=data['stock_quantity']
            )
            return JsonResponse({'id': book.id})
        else:
            book = Book.objects.create(
                title=request.POST['title'],
                author=request.POST['author'],
                published_date=request.POST['published_date'],
                isbn=request.POST['isbn'],
                price=request.POST['price'],
                stock_quantity=request.POST['stock_quantity']
            )
            # return redirect('add_book')
            return redirect('index/home')
    else:
        return render(request, 'add_book.html')


#TO-DO - Write a function to retrieve the details of an individual book.
#`GET /books/<isbn>` - Retrieve book details.

def get_book(request):
    book = None
    if request.method == 'POST':
        isbn = request.POST.get('isbn')
        if isbn:
            try:
                book = Book.objects.get(isbn=isbn)
            except Book.DoesNotExist:
                book = None
        
        author = request.POST.get('author')
        if author:
            try:
                book = Book.objects.get(author=author)
            except Book.DoesNotExist:
                book = None
    return render(request, 'get_book.html', {'book': book})


#TO-DO - Write a function to update the quantity of a book in stock. 
#`PUT /books/<isbn>` - Update stock quantity.

def update_quantity(request):
    if request.method == 'POST':
        # Get the new stock quantity from the form or request data
        new_quantity = request.POST.get('stock_quantity')

        # Retrieve the book by its ISBN
        isbn = request.POST.get('isbn')
        book = Book.objects.get(isbn=isbn)

        # # Validate and update the stock quantity
        # try:
        #     new_quantity = new_quantity
        #     if new_quantity < 0:
        #         raise ValueError("Stock quantity cannot be negative.")
        # except ValueError:
        #     return JsonResponse({'error': 'Invalid quantity. Please enter a valid number.'}, status=400)

        # # Update the stock quantity
        # book.stock_quantity = new_quantity
        # book.save()
        
        # return JsonResponse({
        #     'message': 'Stock quantity updated successfully.',
        #     'new_stock_quantity': book.stock_quantity
        # })
    
    return render(request, 'get_book.html', {'book': book})
    # return render(request, 'update_quantity.html', {'book': book})

#TO-DO - Write a function to delete a book from the library. 
#`DELETE /books/<isbn>` - Delete a book.

def delete_book(request, isbn):
    book = None
    if request.method == 'POST':
        # isbn = request.POST.get('isbn')
        if isbn:
            try:
                book = Book.objects.get(isbn=isbn)
                book.delete();
            except Book.DoesNotExist:
                book = None

    return redirect('index')

def delete_books_with_zero_stock(request):
    if request.method == 'POST':
        # Filter and delete books with zero stock
        books_to_delete = Book.objects.filter(stock_quantity=0)
        count_deleted, _ = books_to_delete.delete()

        return JsonResponse({'message': f'{count_deleted} books deleted.'}, status=200)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def top_5_expensive_books(request):
    # Query to get the top 5 most expensive books
    books = Book.objects.order_by('-price')[:5]
    return render(request, 'top_5_expensive_books.html', {'books': books})