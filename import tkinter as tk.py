import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from PIL import Image, ImageTk

def login():
    username = entry_user.get()
    password = entry_pass.get()
    if username == "admin" and password == "admin":
        messagebox.showinfo("Success", "Logged in successfully!")
    else:
        messagebox.showerror("Error", "Invalid username or password password")

# Placeholder functionality
def on_focus_in(event, entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)  # Clear the placeholder text

def on_focus_out(event, entry, placeholder_text):
    if entry.get() == "":
        entry.insert(0, placeholder_text)  # Revert back to placeholder if empty

# Initialize window
root = tk.Tk()
root.title("Instagram Login")
root.geometry("350x540")
root.configure(bg="white")  # White background

# Fonts
title_font = Font(family="Helvetica", size=28, weight="bold")
link_font = Font(family="Helvetica", size=10, underline=True)

# Instagram logo
tk.Label(root, text="Instagram", font=title_font, fg="black", bg="white").pack(pady=30)

# Username input
entry_user = tk.Entry(root, width=32, font=("Arial", 11), bd=1, relief="solid", 
                      bg="#f2f2f2", fg="black", insertbackground="black")
entry_user.insert(0, "Phone number, username, or email")  # Placeholder text
entry_user.pack(pady=8, ipady=7)

# Password input
entry_pass = tk.Entry(root, width=32, font=("Arial", 11), bd=1, relief="solid", 
                      bg="#f2f2f2", fg="black", insertbackground="black")
entry_pass.insert(0, "Password")  # Placeholder text
entry_pass.pack(pady=8, ipady=7)

# Bind focus events for username and password fields
entry_user.bind("<FocusIn>", lambda event: on_focus_in(event, entry_user, "Phone number, username, or email"))
entry_user.bind("<FocusOut>", lambda event: on_focus_out(event, entry_user, "Phone number, username, or email"))
entry_pass.bind("<FocusIn>", lambda event: on_focus_in(event, entry_pass, "Password"))
entry_pass.bind("<FocusOut>", lambda event: on_focus_out(event, entry_pass, "Password"))

# Login button
tk.Button(root, text="Log in", width=30, bg="#0095f6", fg="white", bd=0, pady=10, command=login).pack(pady=10)

# OR separator
tk.Label(root, text="──────────────  OR  ──────────────", bg="white", fg="gray").pack(pady=10)

# Facebook login
tk.Label(root, text="Log in with Facebook", fg="#0095f6", bg="white", font=("Helvetica", 10, "bold")).pack(pady=5)

# Forgot password section
forgot_pass = tk.Label(
    root, 
    text="Forgot password?", 
    fg="#00376b",  # Instagram's link color
    bg="white", 
    font=("Arial", 9),  # Standard Instagram font size
    cursor="hand2"  # Changes cursor to hand pointer
)
forgot_pass.pack(pady=10)
forgot_pass.bind("<Button-1>", lambda e: messagebox.showinfo("Info", "Password reset functionality would go here"))

# Sign up section
signup_frame = tk.Frame(root, bg="white")  # Using tk.Frame instead of ttk for consistency
signup_frame.pack(fill=tk.X, pady=20)


signup_link = tk.Label(
    signup_frame, 
    text="Sign up", 
    fg="#00376b",  # Matching Instagram's link color
    bg="white", 
    font=("Arial", 9, "bold"),  # Slightly bold for emphasis
    cursor="hand2"  # Hand pointer on hover
)

# Sign up prompt
tk.Label(root, text="", bg="white").pack(pady=20)
frame_signup = tk.Frame(root, bg="white")
frame_signup.pack()
tk.Label(frame_signup, text="Don't have an account?", bg="white", fg="black").pack(side="left")
tk.Label(frame_signup, text=" Sign up", fg="#0095f6", bg="white", font=link_font).pack(side="left")

# App promotion
tk.Label(root, text="Get the app.", bg="white", fg="black").pack(pady=15)

# App buttons frame
frame_buttons = tk.Frame(root, bg="white")
frame_buttons.pack(pady=10)

# Load image for both buttons
button_img = Image.open('C:/Users/CHETHAN/OneDrive/Pictures/Screenshots\Screenshot 2025-05-11 184555.png').resize((120, 40), Image.Resampling.LANCZOS)
button_photo = ImageTk.PhotoImage(button_img)

# Display image buttons
tk.Label(frame_buttons, image=button_photo, bg="white").pack(side="left", padx=5)
tk.Label(frame_buttons, image=button_photo, bg="white").pack(side="left", padx=5)

# Prevent garbage collection
root.button_photo = button_photo

root.mainloop()