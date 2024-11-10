import csv
import random

# Define categories and their AI tools
categories = [f"Category {i+1}" for i in range(20)]
ai_tools = [f"Tool {i+1}" for i in range(4)]

# Define a function to generate random attributes for each AI tool
def generate_attributes():
    return {
        "accuracy": round(random.uniform(1, 10), 2),        # Accuracy between 1 and 10
        "speed": round(random.uniform(1, 10), 2),           # Speed between 1 and 10
        "energy_efficiency": round(random.uniform(1, 10), 2),  # Energy efficiency between 1 and 10
        "carbon_footprint": round(random.uniform(1, 10), 2),   # Carbon footprint between 1 and 10
        "waste_reduction": round(random.uniform(1, 10), 2)     # Waste reduction between 1 and 10
    }

# Create the CSV file
filename = "ai_tool_recommendations.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Category", "Tool", "Accuracy", "Speed", "Energy Efficiency", "Carbon Footprint", "Waste Reduction"])

    # Write data for each category and tool
    for category in categories:
        for tool in ai_tools:
            attributes = generate_attributes()
            writer.writerow([category, tool, attributes["accuracy"], attributes["speed"],
                             attributes["energy_efficiency"], attributes["carbon_footprint"], attributes["waste_reduction"]])

print(f"CSV file '{filename}' generated successfully!")
