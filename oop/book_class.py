class Book:
    # Constructor to initialize the book instance with title, author, and year
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    # Destructor to print a message upon deletion of the object
    def __del__(self):
        print(f"Deleting {self.title}")

    # String representation method (user-friendly string format)
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation method (used for debugging and recreating the object)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
