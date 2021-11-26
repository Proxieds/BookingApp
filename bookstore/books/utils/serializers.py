from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'isbn13': {'validators': []
        }
}

    def self_update(self, instance, requestData): 
        instance.title = requestData['title']
        instance.details = requestData['details']
        instance.publisher = requestData['publisher']
        instance.year = requestData['year']
        instance.price = requestData['price']
        instance.save()
        return instance