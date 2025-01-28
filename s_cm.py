import tkinter as tk

# Function to convert inches to centimeters
def convert_to_cm():
    try:
        inches = float(entry_inch.get())
        centimeters = inches * 2.54
        label_result.config(text=f'{inches} inches is equal to {centimeters:.2f} centimeters')
    except ValueError:
        label_result.config(text="Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Inches to Centimeters Converter")

# Create and place widgets in the window
label_prompt = tk.Label(window, text="Enter length in inches:")
label_prompt.grid(row=0, column=0, padx=10, pady=10)

entry_inch = tk.Entry(window)
entry_inch.grid(row=0, column=1, padx=10, pady=10)

button_convert = tk.Button(window, text="Convert", command=convert_to_cm)
button_convert.grid(row=1, column=0, columnspan=2, pady=10)

label_result = tk.Label(window, text="Result will be displayed here.")
label_result.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
window.mainloop()
