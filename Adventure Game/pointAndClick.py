import tkinter as tk
import random
from PIL  import Image, ImageTk

score = 0
image2_id = None
image2_coordinates = None
game_running = True
score_window_shown = False
score_window = None  # Define score_window as a global variable

def on_click(event):
    """Check if the player clicked on image2."""
    global score
    if game_running:
        x, y = event.x, event.y
        # Calculate the distance between the click and the center of image2
        distance = ((image2_coordinates[0] - x)**2 + (image2_coordinates[1] - y)**2)**0.5
        if distance < 50:  # Define a threshold for clicking accuracy
            canvas.delete(image2_id)  # Remove image2
            score += 1
            label_score.config(text=f"Score: {score}")
            display_image()  # Display a new image2
        else:
            print("Missed!")

def generate_random_coordinates():
    """Generate random coordinates within the canvas."""
    x = random.randint(0, 400)  # Adjust these values according to your canvas size
    y = random.randint(0, 400)
    return x, y

def reset_score():
    """Reset the player's score."""
    global score, game_running, score_window_shown
    score = 0
    label_score.config(text=f"Score: {score}")
    game_running = True
    score_window_shown = False
    if score_window.winfo_exists():
        score_window.destroy()  # Destroy the score window if it exists

def show_score_window():
    """Create a new window to show the final score."""
    global score_window
    score_window = tk.Toplevel(root)
    score_window.title("Game Over")
    score_label = tk.Label(score_window, text=f"Final Score: {score}", font=("Arial", 24))
    score_label.pack(padx=20, pady=20)

def end_game():
    """End the game."""
    global game_running
    game_running = False
    if not score_window_shown:  # Show the score window only once
        show_score_window()

def show_score_window():
    """Create a new window to show the final score."""
    global score_window_shown
    score_window_shown = True
    score_window = tk.Toplevel(root)
    score_window.title("Game Over")
    score_label = tk.Label(score_window, text=f"Final Score: {score}", font=("Arial", 24))
    score_label.pack(padx=20, pady=20)

def display_image():
    """Display image2 at random coordinates."""
    global image2_id, image2_coordinates, game_running
    if game_running:
        x, y = generate_random_coordinates()
        image2_coordinates = (x, y)
        image2_id = canvas.create_image(x, y, anchor=tk.CENTER, image=photo2, tags="keep")
        root.after(20000, end_game)  # End the game after 20 seconds

root = tk.Tk()
root.title("Simple Point and Click Game")

label_score = tk.Label(root, text="Score: 0")
label_score.pack()

# Load image
image = Image.open(r"C:\Users\adgo1\Pictures\image.png")
image = image.resize((400, 400))
photo = ImageTk.PhotoImage(image)
image2 = Image.open(r"C:\Users\adgo1\Pictures\image.png")
image2 = image2.resize((50, 50))  # Adjust the size as needed
photo2 = ImageTk.PhotoImage(image2)

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Create a background image on canvas
canvas.create_image(0, 0, anchor=tk.NW, image=photo, tags="keep")

button_clear = tk.Button(root, text="Reset Score", command=reset_score)
button_clear.pack()

# Display image2 initially
display_image()

canvas.bind("<Button-1>", on_click)

root.mainloop()