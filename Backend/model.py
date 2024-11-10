import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib  # For saving the model

# Load the dataset
data = pd.read_csv("C:\Users\TIWAR\Desktop\tech\ecoaifinder_shashank\generated_tools_data_sequential.csv")

# Define environmental score with additional environmental parameters
data["Environmental Score"] = (
    (data["Energy Efficiency"] + data["Waste Reduction"] + data["Resource Efficiency"] + data["Lifetime Durability"]) /
    (data["Carbon Footprint"] + data["Energy Consumption"] + data["Water Usage"])
)

# Define features (accuracy, speed, environmental score)
X = data[["Accuracy", "Speed", "Environmental Score"]]
y = data["Environmental Score"]  # Example: You can define y as a composite score based on specific needs

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model pipeline with scaling and regression
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("regressor", DecisionTreeRegressor())
])

# Train the model
pipeline.fit(X_train, y_train)

# Save the model to an H5 file (using joblib)
joblib.dump(pipeline, "C:\Users\TIWAR\Desktop\tech\ecoaifinder_shashank\model.h5")

print("Model trained and saved as 'model.h5'.")
