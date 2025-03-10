"""
Author: Ashley Francis
Date written: 03/09/2025
Assignment: Module 08 Final Project Submission
Name of GUI Application: Sheree
Purpose of Application: Generate a shopping list from ingredidents in your household
Reason for creating Application: Grocery shopping and cooking can be difficult for some people,
especially neurodivergent people
Application to Accomplish: Make meal preparation easier by allowing the user to create and
store recipes then generate a shopping from one or more of them
Target Audience: People aged 18+, any gender, working class
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk

# Initialize the main application window
class ShereeApp:
    def __init__(self, master):
        self.master = master
        master.title("Sheree - Shopping List Generator")
        # Dictionary to store recipes
        self.recipes = {}
        # Home Window Buttons
        self.label = tk.Label(master, text="Welcome to Sheree!")
        self.label.pack()

        self.image1 = Image.open("welcome_image.png")
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.image_label1 = tk.Label(master, image=self.photo1, text="Sheree, INC.", compound="top")
        self.image_label1.pack()

        self.create_recipe_button = tk.Button(master, text="Create Recipe", command=self.create_recipe)
        self.create_recipe_button.pack()

        self.generate_list_button = tk.Button(master, text="Generate Shopping List", command=self.generate_shopping_list)
        self.generate_list_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=self.exit_app)
        self.exit_button.pack()

    def create_recipe(self):
        recipe_name = simpledialog.askstring("Input", "Enter the recipe name:")
        if recipe_name:
            ingredients = simpledialog.askstring("Input", "Enter ingredients separated by commas:")
            if ingredients:
                # Store recipe in dictionary
                self.recipes[recipe_name] = ingredients.split(",")
                messagebox.showinfo("Success", f"Recipe '{recipe_name}' created with ingredients: {ingredients}")
            else:
                messagebox.showwarning("Warning", "Ingredients cannot be empty.")
        else:
            messagebox.showwarning("Warning", "Recipe name cannot be empty.")

    def generate_shopping_list(self):
        if not self.recipes:
            messagebox.showwarning("Warning", "No recipes available to generate a shopping list.")
            return

        # Use a set to avoid duplicate ingredients
        shopping_list = set()
        for ingredients in self.recipes.values():
            # Add ingredients to the shopping list
            shopping_list.update(ingredients)
        
        shopping_list_str = ", ".join(shopping_list)
        messagebox.showinfo("Shopping List", f"Shopping list generated: {shopping_list_str}")

    def exit_app(self):
        self.master.quit()


if __name__ != "__main__":
    pass
else:
    root = tk.Tk()
    app = ShereeApp(root)
    root.mainloop()
