# 1. Create a Python class called Song with attributes title, artist, and duration (in seconds). Use the __init__ method to initialize these attributes and create two Song objects with different values.
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

song1 = Song("Shape of You", "Ed Sheeran", 233)
song2 = Song("Blinding Lights", "The Weeknd", 200)

print(song1.title, song1.artist, song1.duration)
print(song2.title, song2.artist, song2.duration)


# 2. Build a class named FoodOrder that represents a Zomato-style order with properties: restaurant_name, items (a list), and total_price. Add a method show_order() that prints the order details in a readable format.
class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price
    
    def show_order(self):
        print("Restaurant:", self.restaurant_name)
        print("Items:", self.items)
        print("Total Price:", self.total_price)

order1 = FoodOrder("Pizza Hut", ["Margherita Pizza", "Coke"], 450)
order1.show_order()


# 3. Write a Python class called InstagramPost with attributes caption, likes, and comments (a list). Add a method add_comment(comment_text) that appends a new comment to the comments list and increases the likes by 1.
class InstagramPost:
    def __init__(self, caption, likes, comments):
        self.caption = caption
        self.likes = likes
        self.comments = comments
    
    def add_comment(self, comment_text):
        self.comments.append(comment_text)
        self.likes += 1

post1 = InstagramPost("Chilling at the beach!", 100, ["Nice!", "Wow!"])
post1.add_comment("Awesome view")

print(post1.caption)
print(post1.likes)
print(post1.comments)


# 4. Given the following code, fix the bug so that the object is created with the correct values: class Movie: def __init__(self, title, rating): title = title rating = rating m = Movie('Jawan', 4.5) print(m.title, m.rating) Hint: Check how instance variables should be assigned inside __init__.
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

m = Movie('Jawan', 4.5)
print(m.title, m.rating)