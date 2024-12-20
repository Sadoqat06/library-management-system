from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title


class Customer(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class BookOrder(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rental_date = models.DateField(auto_now_add = True)
    deadline = models.DateField()
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"Order by {self.customer.email} for {self.book.title}"

