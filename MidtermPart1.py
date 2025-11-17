# Ask the user to enter number of books
books = int(input('Enter the number of books you have purchased:'))

# Find the number of points earned with if, elif, else
if books <= 0:
    points = 0
elif books <= 2:
    points = 5
elif books <= 4:
    points = 15
elif books <= 6:
    points = 30
else: #8 books or more
    points = 60

#display the output
print(f'You earned {points} points this month.')




