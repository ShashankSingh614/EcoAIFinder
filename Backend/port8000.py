from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

# Initialize the FastAPI app
app = FastAPI()

# Set up CORS to allow your React frontend
origins = [
    "http://localhost:5173",  # React app's address
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the dataset and model once when the application starts
data = pd.read_csv(r"C:\Users\TIWAR\Desktop\tech\ecoaifinder_shashank\generated_tools_data_sequential.csv")
model = joblib.load(r"C:\Users\TIWAR\Desktop\tech\ecoaifinder_shashank\model.h5")

# Calculate Environmental Score for the dataset
data["Environmental Score"] = (
    (data["Energy Efficiency"] + data["Waste Reduction"] + data["Resource Efficiency"] + data["Lifetime Durability"]) /
    (data["Carbon Footprint"] + data["Energy Consumption"] + data["Water Usage"])
)

# Define request body with Pydantic
class RecommendationRequest(BaseModel):
    category: str
    preference: str

# Function to recommend tools based on category and preference
def recommend_tools(category, preference, top_n=3):
    # Filter data by category
    category_tools = data[data["Category"] == category]

    # Define weights based on preference
    if preference == "accuracy":
        alpha, beta, gamma = 0.7, 0.2, 0.1
    elif preference == "speed":
        alpha, beta, gamma = 0.2, 0.7, 0.1
    else:  # mix
        alpha, beta, gamma = 0.4, 0.4, 0.2

    # Calculate combined score with environmental impact
    category_tools["Score"] = (
        alpha * category_tools["Accuracy"] +
        beta * category_tools["Speed"] +
        gamma * category_tools["Environmental Score"]
    )

    # Sort tools by score and select top_n
    top_recommendations = category_tools.nlargest(top_n, "Score")

    # Prepare the recommendations in the specified JSON format, including all metrics
    recommendations = []
    for _, row in top_recommendations.iterrows():
        recommendations.append({
            "Tool": row["Tool"],
            "Score": row["Score"],
            "Accuracy": row["Accuracy"],
            "Speed": row["Speed"],
            "Energy Efficiency": row["Energy Efficiency"],
            "Carbon Footprint": row["Carbon Footprint"],
            "Waste Reduction": row["Waste Reduction"],
            "Energy Consumption": row["Energy Consumption"],
            "Resource Efficiency": row["Resource Efficiency"],
            "Water Usage": row["Water Usage"],
            "Lifetime Durability": row["Lifetime Durability"]
        })

    return recommendations

# Define an endpoint to get recommendations
@app.post("/recommendations/")
async def get_recommendations(request: RecommendationRequest):
    try:
        # Get recommendations
        recommendations = recommend_tools(request.category, request.preference)

        # Return recommendations in the specified format
        return {"recommendations": recommendations}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the FastAPI application with uvicorn if the script is executed directly
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("run:app", host="127.0.0.1", port=8000, reload=True)
#     import subprocess

# # Run the first FastAPI app on port 8000
#     process1 = subprocess.Popen(["uvicorn", "run:app", "--host", "127.0.0.1", "--port", "8000", "--reload"])

#     # Run the second FastAPI app on port 8001
#     process2 = subprocess.Popen(["uvicorn", "chatrun:app", "--host", "127.0.0.1", "--port", "8001", "--reload"])

#     # Wait for both processes to complete
#     process1.wait()
#     process2.wait()

