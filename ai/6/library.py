class LibraryExpertSystem:
    def __init__(self):
        self.books = []
        self.rules = []

    def add_book(self, book):
        self.books.append(book)

    def check_availability(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.available
        return False

    def recommend_book(self, genre=None):
        recommendations = []
        for book in self.books:
            if genre:
                if book.genre and book.genre.lower() == genre.lower() and book.available:
                    recommendations.append(book)
            else:
                if book.available:
                    recommendations.append(book)
        return recommendations

    def get_books(self):
        return self.books

    def query_availability(self):
        title = input("Enter the title of the book you want to check: ")
        available = self.check_availability(title)
        if available:
            print(f"'{title}' is available.")
        else:
            print(f"'{title}' is not available.")

    def query_recommendation(self):
        genre = input("Enter the genre you want recommendations for (e.g., Technology, Science, etc.): ")
        recommendations = self.recommend_book(genre)
        if recommendations:
            print(f"\nRecommended Books from the '{genre}' Genre:")
            for book in recommendations:
                print(book)
        else:
            print(f"No books available in the '{genre}' genre.")

    def list_all_books(self):
        print("\nList of all books:")
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")

class Book:
    def __init__(self, title, author, available=True, genre=None):
        self.title = title
        self.author = author
        self.available = available
        self.genre = genre

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"'{self.title}' by {self.author} - Genre: {self.genre} ({status})"

# Create book instances
book1 = Book("Python Programming", "Reema Thareja", available=True, genre="Technology")
book2 = Book("Data Science 101", "Rajendra Verma", available=False, genre="Science")
book3 = Book("Machine Learning Basics", "James Brown", available=True, genre="Technology")
book4 = Book("Fundamentals of Quantum Physics", "Arnold Digger", available=True, genre="Science")
book5 = Book("History of Literature", "Louisa Alcott", available=True, genre="Literature")
book6 = Book("Pride and Prejudice Complete Analysis", "Roald Dahl", available=False, genre="Literature")
book7 = Book("A Brief History of Time", "Stephen Hawking", available=True, genre="Science")
book8 = Book("Steve Jobs", "Walter Isaacson", available=False, genre="Biography")
book9 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", available=True, genre="Fantasy")
book10 = Book("The Art of War", "Sun Tzu", available=True, genre="History")
book11 = Book("The Republic", "Plato", available=False, genre="Philosophy")
book12 = Book("To Kill a Mockingbird", "Harper Lee", available=True, genre="Fiction")

# Add books to the system
library_system = LibraryExpertSystem()
library_system.add_book(book1)
library_system.add_book(book2)
library_system.add_book(book3)
library_system.add_book(book4)
library_system.add_book(book5)
library_system.add_book(book6)
library_system.add_book(book7)
library_system.add_book(book8)
library_system.add_book(book9)
library_system.add_book(book10)
library_system.add_book(book11)
library_system.add_book(book12)

# User interaction
def interactive_query():
    print("Welcome to the Library Expert System!")
    while True:
        print("\nSelect an option:")
        print("1. Check availability of a book")
        print("2. Get book recommendations by genre")
        print("3. List all books")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            library_system.query_availability()
        elif choice == '2':
            library_system.query_recommendation()
        elif choice == '3':
            library_system.list_all_books()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the system
interactive_query()