import tkinter as tk
from tkinter import Scrollbar
from PIL import Image, ImageTk

# Main window setup
window = tk.Tk()
window.title("Carbon Footprint Calculator")
window.geometry("600x400")
window.configure(background="#E0F2F1")

def calculate_carbon_footprint():
  try:
      emission_factor = float(emission_factor_entry.get())
      electricity_consumption = float(electricity_consumption_entry.get())
      carbon_footprint = electricity_consumption * emission_factor
      result_label.config(text=f"Carbon Footprint: {carbon_footprint:.2f} kg CO2")
  except ValueError:
      result_label.config(text="Please enter valid numbers.")

# Add input fields and calculate button
input_frame = tk.Frame(window, bg="#E0F2F1")
input_frame.pack(pady=20)

# Emission factor entry
emission_factor_label = tk.Label(input_frame, text="Emission Factor (kg CO2/kWh):", bg="#E0F2F1", font=("Arial", 12))
emission_factor_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
emission_factor_entry = tk.Entry(input_frame, width=20)
emission_factor_entry.grid(row=0, column=1, padx=10, pady=10)

# Electricity consumption entry
electricity_consumption_label = tk.Label(input_frame, text="Electricity Consumption (kWh):", bg="#E0F2F1", font=("Arial", 12))
electricity_consumption_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
electricity_consumption_entry = tk.Entry(input_frame, width=20)
electricity_consumption_entry.grid(row=1, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(input_frame, text="Calculate", command=calculate_carbon_footprint, bg="#009688", fg="white", font=("Arial", 14))
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Result label
result_label = tk.Label(window, text="", bg="#E0F2F1", font=("Arial", 14))
result_label.pack(pady=20)

def load_logo():
  try:
      logo_image = Image.open("logo.png")  # Replace 'logo.png' with the path to your logo image
      resized_logo_image = logo_image.resize((300, 300))  # Resize image as needed
      logo_photo = ImageTk.PhotoImage(resized_logo_image)
      logo_label = tk.Label(window, image=logo_photo, bg="#E0F2F1")
      logo_label.image = logo_photo  # Keep a reference to avoid garbage collection
      logo_label.pack(pady=20, side=tk.BOTTOM)  # Place the logo below other elements
  except FileNotFoundError:
      print("Logo image file not found. Please check the file path.")

load_logo()  # Call the function to display the logo

# Show facts function
def show_facts():
    facts_window = tk.Toplevel(window)
    facts_window.title("Carbon Footprint Facts")
    facts_window.configure(background="#E0F2F1")

    # Create a frame to hold the canvas and scrollbars
    frame = tk.Frame(facts_window)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create a canvas and scrollbars for the facts window
    canvas = tk.Canvas(frame, bg="#E0F2F1")
    v_scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    h_scrollbar = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
    scrollable_frame = tk.Frame(canvas, bg="#E0F2F1")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    # Pack the canvas and scrollbars
    canvas.pack(side="left", fill="both", expand=True)
    v_scrollbar.pack(side="right", fill="y")
    h_scrollbar.pack(side="bottom", fill="x")

    # Load and display an image at the top of the facts window
    facts_image = Image.open("facts_image.png")  # Replace 'facts_image.png' with the path to your facts image
    resized_facts_image = facts_image.resize((400, 300))  # Resize image as needed
    facts_photo = ImageTk.PhotoImage(resized_facts_image)
    image_label = tk.Label(scrollable_frame, image=facts_photo, bg="#E0F2F1")
    image_label.image = facts_photo  # Keep a reference to avoid garbage collection
    image_label.pack(pady=20)

    # Create a teal frame to hold all facts
    facts_frame = tk.Frame(scrollable_frame, bg="#009688")
    facts_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Create a label for each fact
    facts = [
        "1. The majority of carbon dioxide (CO2) emissions associated with energy use come from the burning of fossil fuels to produce electricity.",
        "2. The world can emit about 2.4 million pounds of CO2 each second, with some of the major emitters being European countries.",
        "3. The 'greenhouse effect' refers to the way that certain gases in the Earth's atmosphere retain long-wave thermal radiation coming from the planet's surface while allowing short-wave radiation to enter.",
        "4. The amount of paper you consume determines how much greenhouse gas emissions you make, similar to how much tap water you use. Even worse, the more deforestation occurs worldwide, the more emissions it produces—more than all the cars, trucks, planes, and ships put together.",
        "5. A study that was published in the journal Environmental Science & Technology discovered that some of the emissions of methane, nitrous oxide, and carbon dioxide that their sheep, cattle, and goats make are the responsibility of businesses that manufacture food."
    ]

    for fact in facts:
        # Create a label for each fact with teal background and white text
        fact_label = tk.Label(facts_frame, text=fact, font=("Arial", 12), bg="#009688", fg="white", wraplength=500, justify="left", anchor="w")
        fact_label.pack(fill="both", expand=True, padx=10, pady=10)

# Show solutions function
def show_solutions():
  solutions_window = tk.Toplevel(window)
  solutions_window.title("Reduce Greenhouse Gas Emissions")
  solutions_window.configure(background="#E0F2F1")

  # Create a frame to hold the canvas and scrollbars
  frame = tk.Frame(solutions_window)
  frame.pack(fill=tk.BOTH, expand=True)

  # Create a canvas and scrollbars for the solutions window
  canvas = tk.Canvas(frame, bg="#E0F2F1")
  v_scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
  h_scrollbar = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
  scrollable_frame = tk.Frame(canvas, bg="#E0F2F1")

  scrollable_frame.bind(
      "<Configure>",
      lambda e: canvas.configure(
          scrollregion=canvas.bbox("all")
      )
  )

  canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
  canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

  # Pack the canvas and scrollbars
  canvas.pack(side="left", fill="both", expand=True)
  v_scrollbar.pack(side="right", fill="y")
  h_scrollbar.pack(side="bottom", fill="x")

  # Load and display an image at the top of the solutions window
  try:
      solutions_image = Image.open("solutions_image.png")  # Replace 'solutions_image.png' with the path to your solutions image
      resized_solutions_image = solutions_image.resize((400, 300))  # Resize image as needed
      solutions_photo = ImageTk.PhotoImage(resized_solutions_image)
      image_label = tk.Label(scrollable_frame, image=solutions_photo, bg="#E0F2F1")
      image_label.image = solutions_photo  # Keep a reference to avoid garbage collection
      image_label.pack(pady=20)
  except FileNotFoundError:
      print("Solutions image file not found. Please check the file path.")

  # Create a teal frame to hold all solutions
  solutions_frame = tk.Frame(scrollable_frame, bg="#009688")
  solutions_frame.pack(pady=10, padx=10, fill="both", expand=True)

  # Create a label for each solution with white text
  solutions = [
      "1. When there is enough natural light and when you leave the room, turn off the lights. It's that easy!",
      "2. While you are in the room, keep the temperature on a moderate level, do not overuse the AC or heater.",
      "3. You can save a lot of energy by reducing the number of appliances you run. For instance, reduce the number of printers in your office and share your mini-fridge with your roommates.",
      "4. Consume low-level foods. This calls for a diet high in grains, beans, fruits, and vegetables. Livestock—meat and dairy—are to blame for 14.5% of human-caused global greenhouse gas emissions."
  ]

  for solution in solutions:
      # Create a label for each solution with teal background and white text
      solution_label = tk.Label(solutions_frame, text=solution, font=("Arial", 12), bg="#009688", fg="white", wraplength=500, justify="left", anchor="w")
      solution_label.pack(fill="both", expand=True, padx=10, pady=10)


# Add buttons to main window to open facts and solutions
facts_button = tk.Button(window, text="Show Facts", command=show_facts, bg="#009688", fg="white", font=("Arial", 14))
facts_button.pack(pady=20)

solutions_button = tk.Button(window, text="Show Solutions", command=show_solutions, bg="#009688", fg="white", font=("Arial", 14))
solutions_button.pack(pady=20)

# Start the Tkinter main loop
window.mainloop()
