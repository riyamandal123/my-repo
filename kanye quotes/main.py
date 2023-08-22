# Import the necessary modules
from tkinter import *
import requests


# Function to fetch and display Kanye West quotes
def kanye_quotes():
    # Send a GET request to the Kanye West quotes API
    response = requests.get(url="https://api.kanye.rest")
    #HTTPError if the HTTP request returned an unsuccessful status code
    response.raise_for_status()
    # Extract the quote from the JSON response
    data = response.json()['quote']
    # Update the text of the 'quotes' Canvas item with the fetched quote
    canvas.itemconfig(quotes, text=data)


# Create the main UI window
window = Tk()
window.title("Kanye Quotes")
window.config(padx=50, pady=50, bg="yellow")

# Create a Canvas to display the background image and quotes
canvas = Canvas(width=300, height=414, bg="yellow", highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
# Create a text item on the canvas to display the quotes
quotes = canvas.create_text(150, 207, text="", width=250, font=("Arial", 23, "italic","bold"))
canvas.grid(row=0, column=0)

# Load Kanye West's image for the button
kanye_img = PhotoImage(file="kanye.png")
# Create a button with Kanye West's image, triggering the kanye_quotes() function when clicked
kanye_button = Button(image=kanye_img, highlightthickness=0, command=kanye_quotes, bg="yellow")
kanye_button.grid(row=1, column=0)

# Initial call to fetch and display a Kanye quote
kanye_quotes()

# Start the main event loop to display the UI
window.mainloop()
