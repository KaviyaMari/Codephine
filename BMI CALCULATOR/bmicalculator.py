import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BMI_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.weight_label = ttk.Label(root, text="Weight (kg):")
        self.weight_label.grid(row=0, column=0, padx=10, pady=10)

        self.weight_entry = ttk.Entry(root)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=10)

        self.height_label = ttk.Label(root, text="Height (cm):")
        self.height_label.grid(row=1, column=0, padx=10, pady=10)

        self.height_entry = ttk.Entry(root)
        self.height_entry.grid(row=1, column=1, padx=10, pady=10)

        self.calculate_button = ttk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.plot_button = ttk.Button(root, text="Plot BMI Trend", command=self.plot_bmi_trend)
        self.plot_button.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100  # Convert height to meters
            bmi = weight / (height ** 2)
            self.result_label.config(text=f"BMI: {bmi:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

    def plot_bmi_trend(self):
        # Placeholder for BMI trend plot
        x_values = [1, 2, 3, 4, 5]
        y_values = [25, 26, 24, 28, 27]

        fig, ax = plt.subplots()
        ax.plot(x_values, y_values, marker='o', linestyle='-')
        ax.set_xlabel('Time')
        ax.set_ylabel('BMI')
        ax.set_title('BMI Trend Over Time')

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=5, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()
