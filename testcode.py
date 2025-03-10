import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ShereeApp:
    def __init__(self, master):
        self.master = master
        master.title("Sheree - Shopping List Generator")

        self.label = tk.Label(master, text="Welcome to Sheree!")
        self.label.pack()

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
                # Store recipe logic here
                messagebox.showinfo("Success", f"Recipe '{recipe_name}' created with ingredients: {ingredients}")
            else:
                messagebox.showwarning("Warning", "Ingredients cannot be empty.")
        else:
            messagebox.showwarning("Warning", "Recipe name cannot be empty.")

    def generate_shopping_list(self):
        # Logic to generate shopping list from stored recipes
        messagebox.showinfo("Shopping List", "Shopping list generated successfully!")

    def exit_app(self):
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShereeApp(root)
    root.mainloop()
