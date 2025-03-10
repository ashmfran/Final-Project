"""
Author: Ashley Francis
Date written: 03/03/2025
Assignment: Module 06 Project Status Report II

"""

import tkinter as tk
from tkinter import messagebox, simpledialog

class ShereeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sheree - Shopping List Generator")
        
        self.recipes = {}
        
        self.label = tk.Label(root, text="Welcome to Sheree! Create and store your recipes.")
        self.label.pack(pady=10)

        self.add_recipe_button = tk.Button(root, text="Add Recipe", command=self.add_recipe)
        self.add_recipe_button.pack(pady=5)

        self.generate_list_button = tk.Button(root, text="Generate Shopping List", command=self.generate_shopping_list)
        self.generate_list_button.pack(pady=5)

    def add_recipe(self):
        recipe_name = simpledialog.askstring("Input", "Enter the recipe name:")
        ingredients = simpledialog.askstring("Input", "Enter the ingredients (comma separated):")
        if recipe_name and ingredients:
            self.recipes[recipe_name] = ingredients.split(',')
            messagebox.showinfo("Success", f"Recipe '{recipe_name}' added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please provide both recipe name and ingredients.")

    def generate_shopping_list(self):
        if not self.recipes:
            messagebox.showwarning("No Recipes", "Please add some recipes first.")
            return
        
        selected_recipes = simpledialog.askstring("Input", "Enter the recipe names to include (comma separated):")
        if selected_recipes:
            shopping_list = set()
            for recipe in selected_recipes.split(','):
                recipe = recipe.strip()
                if recipe in self.recipes:
                    shopping_list.update(self.recipes[recipe])
                else:
                    messagebox.showwarning("Recipe Not Found", f"Recipe '{recipe}' not found.")
            shopping_list_str = ', '.join(shopping_list)
            messagebox.showinfo("Shopping List", f"Your shopping list: {shopping_list_str}")
        else:
            messagebox.showwarning("Input Error", "Please provide recipe names.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShereeApp(root)
    root.mainloop()
