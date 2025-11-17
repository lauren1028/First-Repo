import tkinter as tk

# input function to calculate the points earned
def compute_points():
    try:
        global points
        books = int(entry_books.get())
        if books <= 0:
            points = 0
        elif books <=2:
            points = 5
        elif books <=4:
            points = 15
        elif books <=6:
            points = 30
        else: #8 books or more
            points = 60

        result_label.configure(text=f'You earned {points} points this month.')
    except:
        result_label.configure(text=f'Enter a valid number of books.')

#create main window
main_window = tk.Tk()
main_window.title("Serendipity Booksellers Calculator")
main_window.geometry("500x450")

#Input frame
btns_frame = tk.Frame(main_window, padx=10, pady=10)
btns_frame.pack(padx=10, pady=10)

# Label widget to display instruction to the user
label = tk.Label(main_window, text="Enter the number of books purchased:")
label.pack(pady=10)

# Entry widget for user input
entry_books = tk.Entry(main_window, width=10, fg="black", bg="pink")
entry_books.pack()

# Create button that computes and displays the points earned
compute_button = tk.Button(main_window, text="Compute", command=compute_points)
compute_button.pack(pady=10)

# Create label to display the result
result_label = tk.Label(main_window, text="")
result_label.pack(pady=10)

main_window.mainloop()
