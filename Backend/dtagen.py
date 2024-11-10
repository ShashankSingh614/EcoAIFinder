import random
import csv

# Categories and tool types
categories = [
"Machine Learning Optimization", "Energy-Efficient NLP", "Green Computer Vision",
    "Sustainable Edge Computing", "Resource-Optimized Deep Learning", 
    "Eco-Friendly Data Processing", "Smart Grid AI", "Waste Management AI",
    "Renewable Energy AI", "Carbon Footprint Analytics", "Environmental Monitoring",
    "Green Cloud Computing", "Sustainable IoT", "Energy Management Systems",
    "Resource Planning AI", "Climate Modeling AI", "Eco-Logistics AI",
    "Green Manufacturing AI", "Sustainable Agriculture AI", "Water Management AI"
]

# Function to generate random values within a bounded range
def generate_value(min_val, max_val, dist_type='uniform'):
    if dist_type == 'normal':
        mean = (min_val + max_val) / 2
        stddev = (max_val - min_val) / 4
        value = random.gauss(mean, stddev)
    elif dist_type == 'log_normal':
        value = random.lognormvariate(0, 0.3)
        value = min_val + (value % (max_val - min_val))
    else:
        value = random.uniform(min_val, max_val)
    
    # Clamp value within the specified range
    return round(max(min_val, min(value, max_val)), 2)

# Function to generate correlated data within bounds
def generate_correlated_value(base_value, correlation='inverse', min_val=1, max_val=10):
    if correlation == 'inverse':
        value = max_val + min_val - base_value
    elif correlation == 'direct':
        value = base_value
    else:
        value = random.uniform(min_val, max_val)
    return round(max(min_val, min(value, max_val)), 2)

# Function to generate the CSV file
def generate_data(num_entries_per_category):
    with open('generated_tools_data_sequential.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Writing header
        writer.writerow([
            "Category", "Tool", "Tool Description", "Accuracy", "Speed", "Energy Efficiency", 
            "Carbon Footprint", "Waste Reduction", "Energy Consumption", "Resource Efficiency", 
            "Water Usage", "Lifetime Durability"
        ])
        
        # Generate data for each category
        for category in categories:
            for i in range(1, num_entries_per_category + 1):
                tool_name = f"{category}_Tool_{i}"
                tool_description = f"Description of {category} tool {i}"
                
                # Generate values with correlations
                accuracy = generate_value(5, 10, dist_type='normal')
                speed = generate_value(5, 10, dist_type='normal')
                energy_efficiency = generate_value(5, 10, dist_type='log_normal')
                carbon_footprint = generate_correlated_value(energy_efficiency, 'inverse')
                waste_reduction = generate_value(3, 10, dist_type='uniform')
                
                # Additional attributes with environmental focus
                energy_consumption = generate_correlated_value(energy_efficiency, 'inverse')
                resource_efficiency = generate_correlated_value(energy_efficiency, 'direct')
                water_usage = generate_value(1, 10, dist_type='log_normal')
                lifetime_durability = generate_value(7, 10, dist_type='normal')
                
                writer.writerow([
                    category, tool_name, tool_description, accuracy, speed, energy_efficiency, 
                    carbon_footprint, waste_reduction, energy_consumption, resource_efficiency, 
                    water_usage, lifetime_durability
                ])
    
    print("CSV file with generated data has been created.")

# Generate 20 tools for each category
generate_data(30)
