from django.core.management.base import BaseCommand
import random
from datetime import datetime, timedelta
from django.utils.text import slugify
from myapp.models import Author, Publisher, Book

class Command(BaseCommand):
    help = 'Seeds the database with 20 authors, 20 publishers, and 20 books'

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")
        self.create_authors()
        self.create_publishers()
        self.create_books()
        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))

    def clear_data(self):
        """Optional: Clear existing data"""
        Book.objects.all().delete()
        Publisher.objects.all().delete()
        Author.objects.all().delete()

    def create_authors(self):
        first_names = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 
                     'William', 'Elizabeth', 'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 
                     'Thomas', 'Sarah', 'Charles', 'Karen', 'Daniel', 'Nancy', 'Matthew', 'Lisa', 
                     'Anthony', 'Margaret', 'Mark', 'Betty', 'Paul', 'Dorothy']
        
        last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 
                    'Rodriguez', 'Wilson', 'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 
                    'Moore', 'Martin', 'Jackson', 'Thompson', 'White', 'Lee', 'Harris', 'Clark', 'Lewis']
        
        # Shuffle to get random combinations
        random.shuffle(first_names)
        random.shuffle(last_names)
        
        for i in range(20):
            first = first_names[i]
            last = last_names[i]
            Author.objects.create(
                name=f"{first} {last}",
                email=f"{first.lower()}.{last.lower()}{i}@example.com",
                bio=f"{first} {last} is a renowned author with {random.randint(1,20)} published works.",
                birth_date=datetime.now() - timedelta(days=random.randint(20*365, 70*365))
            )

    def create_publishers(self):
        publisher_names = ['Penguin Random House', 'HarperCollins', 'Simon & Schuster', 'Macmillan', 
                         'Hachette', 'Scholastic', 'Pearson', 'Oxford University Press', 
                         'Cambridge University Press', 'Wiley', 'Bloomsbury', 'Pan Macmillan', 
                         'Allen & Unwin', 'Houghton Mifflin Harcourt', 'Workman Publishing', 
                         'Chronicle Books', 'Abrams', 'Walker Books', 'Egmont', 'Usborne']
        
        for name in publisher_names:
            Publisher.objects.create(
                name=name,
                address=f"{random.randint(1,500)} {random.choice(['Main', 'Oak', 'Pine', 'Maple'])} St, {random.choice(['New York', 'London', 'Sydney', 'Toronto'])}",
                website=f"https://www.{slugify(name)}.com"
            )

    def create_books(self):
        book_titles = ['The Silent Patient', 'Where the Crawdads Sing', 'The Guest List', 'Educated', 
                      'Becoming', 'The Testaments', 'Normal People', 'The Dutch House', 'Little Fires Everywhere', 
                      'The Institute', 'The Water Dancer', 'The Giver of Stars', 'Such a Fun Age', 
                      'The Starless Sea', 'The Night Fire', 'The Family Upstairs', 'The Silent Patient', 
                      'Nine Perfect Strangers', 'City of Girls', 'The Tattooist of Auschwitz']
        
        book_adjectives = ['Mysterious', 'Forgotten', 'Hidden', 'Secret', 'Last', 'First', 'Dark', 'Bright', 
                         'Lost', 'Stolen', 'Silent', 'Loud', 'Beautiful', 'Ugly', 'Happy', 'Sad', 
                         'Ancient', 'Modern', 'Future', 'Past']
        
        book_nouns = ['House', 'Garden', 'Secret', 'Promise', 'Lie', 'Truth', 'Child', 'Woman', 'Man', 
                     'Journey', 'Road', 'Mountain', 'River', 'Ocean', 'Sky', 'Star', 'Moon', 'Sun', 
                     'Book', 'Letter']
        
        authors = list(Author.objects.all())
        publishers = list(Publisher.objects.all())
        genres = ['FIC', 'NF', 'SCI', 'HIS']
        
        for i in range(20):
            if i < len(book_titles):
                title = book_titles[i]
            else:
                title = f"The {random.choice(book_adjectives)} {random.choice(book_nouns)}"
            
            author = random.choice(authors)
            publication_date = datetime.now() - timedelta(days=random.randint(30, 365*20))
            
            # Generate unique ISBN
            while True:
                isbn = ''.join([str(random.randint(0,9)) for _ in range(13)])
                if not Book.objects.filter(isbn=isbn).exists():
                    break
            
            book = Book.objects.create(
                title=title,
                author=author,
                publication_date=publication_date,
                genre=random.choice(genres),
                price=round(random.uniform(5.99, 29.99), 2),
                isbn=isbn
            )
            
            book_publishers = random.sample(publishers, k=random.randint(1,3))
            book.publishers.set(book_publishers)