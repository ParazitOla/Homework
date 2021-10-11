### Task 6.7  Implement a Pagination class helpful to arrange text on pages and list content on given page.
# The class should take in a text and a positive integer which indicate how many symbols will be allowed per
# each page (take spaces into account as well).
# You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method
# that accepts the page number and return quantity of symbols on this page.
# If the provided number of the page is missing print the warning message "Invalid index. Page is missing".
# If you're familliar with using of Excpetions in Python display the error message in this way.
# Pages indexing starts with 0.


class Pagination:

    def __init__(self, text, symbols):
        self.text = text
        self.symbols = symbols

    def item_count(self):
        return len(self.text)

    def page_count(self):
        if self.item_count() % self.symbols != 0:
            self.page = int(self.item_count() // self.symbols) + 1
        else:
            self.page = int(self.item_count() / self.symbols)
        return self.page

    def count_items_on_page(self, page):
        try:
            self.page = page
            self.pages_list = [self.text[i:i + self.symbols] for i in range(0, self.item_count(), self.symbols)]
            self.items_on_page_X = len(self.pages_list[self.page])
        except IndexError:
            print('Invalid index. Page is missing')
        return self.items_on_page_X, self.pages_list


pages = Pagination('Your beautiful text', 5)
print(pages.item_count())
print(pages.page_count())
print(pages.count_items_on_page(4))
# 5
