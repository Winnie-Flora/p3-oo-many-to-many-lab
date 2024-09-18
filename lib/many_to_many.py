class Book:
    all_books = []
    
    def __init__(self, title: str):
        if not isinstance(title, str) or not title.strip():
            raise Exception("Title must be a non-empty string.")
        self.title = title.strip()
        Book.all_books.append(self)
    
    def contracts(self):
        """Return a list of contracts related to this book."""
        return [contract for contract in Contract.all_contracts if contract.book == self]
    
    def authors(self):
        """Return a list of authors related to this book via contracts."""
        return [contract.author for contract in self.contracts()]
    
    def __repr__(self):
        return f"Book({self.title!r})"


class Author:
    all_authors = []
    
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Name must be a non-empty string.")
        self.name = name.strip()
        Author.all_authors.append(self)
    
    def contracts(self):
        """Return a list of all contracts related to this author."""
        return [contract for contract in Contract.all_contracts if contract.author == self]
    
    def books(self):
        """Return a list of all books related to this author via contracts."""
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        """Create and return a new contract for this author."""
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str) or not date.strip():
            raise Exception("Date must be a non-empty string.")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer.")
        
        contract = Contract(self, book, date.strip(), royalties)
        return contract
    
    def total_royalties(self):
        """Return the total royalties earned from all contracts."""
        return sum(contract.royalties for contract in self.contracts())
    
    def __repr__(self):
        return f"Author({self.name!r})"


class Contract:
    all_contracts = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str) or not date.strip():
            raise Exception("Date must be a non-empty string.")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer.")
        
        self.author = author
        self.book = book
        self.date = date.strip()
        self.royalties = royalties
        
        Contract.all_contracts.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        """Return a sorted list of all contracts for a specific date."""
        if not isinstance(date, str) or not date.strip():
            raise Exception("Date must be a non-empty string.")
        
        # Filter contracts by date
        filtered_contracts = [contract for contract in cls.all_contracts if contract.date == date.strip()]
        
        # Sort by book title and author name to ensure deterministic order
        return sorted(filtered_contracts, key=lambda x: (x.book.title, x.author.name))
    
    def __repr__(self):
        return f"Contract({self.author.name!r}, {self.book.title!r}, {self.date!r}, {self.royalties}%)"
