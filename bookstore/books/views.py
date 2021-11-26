from books.models import Book as Books
from books.utils.responseObjects import Book, FullBookHistory
from books.utils.serializers import BookSerializer
from rest_framework.generics import GenericAPIView
from books.utils.apiPermissions import APIPermission
from rest_framework.response import Response
from rest_framework import status

class IndexView(GenericAPIView):
    permission_classes = [APIPermission]
    template_name = "index.html"
    serializer_class = BookSerializer
    
    def get(self, request):
        # Return a list of all books
        objects = Books.objects.all()
        count = objects.count()
        data = {
            'total': count,
            'books': []
        }
        for record in objects:
            book = Book(record.title, record.isbn13, record.price)
            data['books'].append(book.toJSON())
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        # Check if an existing book with the requested isbn13 already exists
        book = Books.objects.filter(isbn13 = self.request.data['isbn13']).first()
        if book:
            return Response({"status": 1, "message": "Book already exists, use PUT to update" }, status=status.HTTP_409_CONFLICT)
        # Save book
        serializedObj = BookSerializer(data = request.data)
        if serializedObj.is_valid():
            serializedObj.save()
            return Response({"status": 0, "message": "Book added" }, status=status.HTTP_200_OK)
        return Response({"status": 1, "message": "Error with Request Data" }, status=status.HTTP_400_BAD_REQUEST)

class BookView(GenericAPIView):
    permission_classes = [APIPermission]
    template_name = "books.html"
    serializer_class = BookSerializer
    def get(self, request, isbn13):
        # Return all information for the book
        record = Books.objects.filter(isbn13 = isbn13).first()
        if record:
            book = FullBookHistory(record.title, record.isbn13, record.details, record.publisher, record.year, record.price)
            return Response(book.toJSON(), status=status.HTTP_200_OK)
        return Response({"status": 1, "message":"Book does not Exist"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, isbn13):
        # Check if the book exists first
        record = Books.objects.filter(isbn13 = isbn13).first()
        if record:
            # Update book information if the data is present, otherwise use existing
            data = self.request.data
            record.title = data.get('title') if data.get('title') else record.title
            record.details = data.get('details') if data.get('details') else record.details
            record.publisher = data.get('publisher') if data.get('publisher') else record.publisher
            record.year = data.get('year') if data.get('year') else record.year
            record.price = data.get('price') if data.get('price') else record.price
            record.save()
            return Response({"status": 0, "message": "Book updated"}, status=status.HTTP_200_OK)
        return Response({"status": 1, "message":"Book does not Exist"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, isbn13):
        record = Books.objects.filter(isbn13 = isbn13).first()
        if record:
            # Delete the Record
            record.delete()
            return Response({ "status": 0, "message": "Book deleted"}, status=status.HTTP_200_OK)
        return Response({"status": 1, "message":"Book does not Exist"}, status=status.HTTP_404_NOT_FOUND)