import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Creating a mock dataset for polio cases and vaccination efforts over the years
data = {
    'Year': [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
    'Polio Cases (Reported)': [150000, 130000, 120000, 110000, 100000, 85000, 70000, 60000, 50000, 40000, 30000, 20000, 15000, 10000, 5000, 0, 0, 0, 0, 0],
    'Vaccination Coverage (%)': [35, 38, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 98, 100, 100, 100, 100, 100]
}

# Converting the dictionary into a DataFrame
df = pd.DataFrame(data)

# Create a figure with two subplots
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Polio Cases on the left y-axis
ax1.set_xlabel('Year')
ax1.set_ylabel('Polio Cases (Reported)', color='tab:red')
ax1.plot(df['Year'], df['Polio Cases (Reported)'], color='tab:red', marker='o', label='Polio Cases')
ax1.tick_params(axis='y', labelcolor='tab:red')

# Create a second y-axis to plot Vaccination Coverage
ax2 = ax1.twinx()
ax2.set_ylabel('Vaccination Coverage (%)', color='tab:blue')
ax2.plot(df['Year'], df['Vaccination Coverage (%)'], color='tab:blue', marker='s', linestyle='--', label='Vaccination Coverage')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Add a title
plt.title('Polio Cases vs. Vaccination Coverage in India (1995-2014)')

# Show the plot
plt.tight_layout()
plt.show()


class PolioEradicationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Polio Eradication in India")
        self.root.geometry("600x400")

        # Create a label for the title
        title_label = tk.Label(self.root, text="Polio Eradication Progress", font=("Helvetica", 16))
        title_label.pack(pady=20)

        # Create a dropdown menu to select the year for analysis
        self.year_var = tk.StringVar()
        years = [str(year) for year in df['Year']]
        year_menu = ttk.Combobox(self.root, textvariable=self.year_var, values=years, state="readonly")
        year_menu.set("Select Year")
        year_menu.pack(pady=10)

        # Create a button to display selected year data
        analyze_button = tk.Button(self.root, text="Analyze Year", command=self.analyze_year)
        analyze_button.pack(pady=10)

        # Create a text box to display results
        self.result_text = tk.Text(self.root, height=8, width=50)
        self.result_text.pack(pady=20)

    def analyze_year(self):
        selected_year = self.year_var.get()
        if selected_year == "Select Year":
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please select a valid year.")
            return

        # Filter data for the selected year
        year_data = df[df['Year'] == int(selected_year)].iloc[0]

        # Display the data for the selected year
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Year: {year_data['Year']}\n")
        self.result_text.insert(tk.END, f"Polio Cases Reported: {year_data['Polio Cases (Reported)']}\n")
        self.result_text.insert(tk.END, f"Vaccination Coverage: {year_data['Vaccination Coverage (%)']}%\n")


# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PolioEradicationApp(root)
    root.mainloop()
