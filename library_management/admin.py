from django.contrib import admin
from .models import Author, Book, Customer, BookOrder



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')  
    search_fields = ('name',)



class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title',)
    list_filter = ('author',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)


class BookOrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'customer', 'rental_date', 'deadline', 'returned')
    search_fields = ('book__title', 'customer__email')
    list_filter = ('returned', 'rental_date')



admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(BookOrder, BookOrderAdmin)

