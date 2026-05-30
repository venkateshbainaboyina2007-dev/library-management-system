from datetime import datetime, timedelta

class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.__item_id = item_id
        self.is_available = True

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Item ID: {self.__item_id}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")

    def get_id(self):
        return self.__item_id


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")


class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_all_items(self):
        print("\n📚 Library Collection:\n")
        for item in self.items:
            item.display_info()
            print("-" * 30)

    def search_item(self, title):
        print(f"\n🔍 Search Results for '{title}':\n")
        found = False
        for item in self.items:
            if title.lower() in item.title.lower():
                item.display_info()
                print("-" * 30)
                found = True
        if not found:
            print("No item found.")

    def borrow_item(self, item_id):
        for item in self.items:
            if item.get_id() == item_id:
    
                # check availability
                if item.is_available:
                    item.is_available = False   # mark as borrowed
                    due_date = datetime.now() + timedelta(days=7)
    
                    print(f"\n✅ '{item.title}' borrowed successfully")
                    print(f"📅 Due date: {due_date.date()}")
                    print(f"🔒 Availability changed to: {item.is_available}")
    
                    return due_date
                else:
                    print(f"\n❌ '{item.title}' is already borrowed")
                    return None
    
        print("\n❌ Item ID not found in library")
        return None


    def return_item(self, item_id, due_date): 
        for item in self.items:
            if item.get_id() == item_id:
    
                # check if it was borrowed
                if not item.is_available:
    
                    item.is_available = True   # mark as returned
                    today = datetime.now()
    
                    print(f"\n📚 '{item.title}' returned successfully")
                    print(f"🔓 Availability changed to: {item.is_available}")
    
                    # fine calculation
                    if today > due_date:
                        late_days = (today - due_date).days
                        fine = late_days * 5
                        print(f"⚠ Late return! Fine = ₹{fine}")
                    else:
                        print("✅ Returned on time. No fine.")
    
                    return
    
                else:
                    print("\n❌ This item was not borrowed")
                    return
    
        print("\n❌ Item ID not found in library")


def safe_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("\n⚠ Input not supported in this environment. Please enter a valid input.")
        return None


def run_library():
    library = Library()

    # sample items
    library.add_item(Book("Python Basics", "Guido", "B101", "Programming"))
    library.add_item(Book("JavaScript Guide", "Brendan", "B102", "Web"))
    library.add_item(Magazine("Tech Monthly", "Various", "M201", 2024))

    borrowed_records = {}

    while True:
        print("\n====== 📖 LIBRARY MENU ======")
        print("1. View all items")
        print("2. Search item")
        print("3. Borrow item")
        print("4. Return item")
        print("5. Exit")

        choice = safe_input("Enter choice: ")

        if choice is None:
            break   # exit safely if input not possible

        if choice == "1":
            library.display_all_items()

        elif choice == "2":
            title = safe_input("Enter title to search: ")
            if title:
                library.search_item(title)

        elif choice == "3":
            item_id = safe_input("Enter Item ID to borrow: ")
            if item_id:
                due = library.borrow_item(item_id)
                if due:
                    borrowed_records[item_id] = due

        elif choice == "4":
            item_id = safe_input("Enter Item ID to return: ")
            if item_id in borrowed_records:
                library.return_item(item_id, borrowed_records[item_id])
                del borrowed_records[item_id]
            else:
                print("No record of this item being borrowed.")

        elif choice == "5":
            print("👋 Exiting Library System...")
            break

        else:
            print("Invalid choice!")


# Run program
run_library()