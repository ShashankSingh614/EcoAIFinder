from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

# Initialize FastAPI app
app = FastAPI()
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

# Initialize the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L12-v2')

# Predefined categories and preferences
categories = [
    "Machine Learning Optimization", "Energy-Efficient NLP", "Green Computer Vision", 
    "Sustainable Edge Computing", "Resource-Optimized Deep Learning", "Eco-Friendly Data Processing", 
    "Smart Grid AI", "Waste Management AI", "Renewable Energy AI", "Carbon Footprint Analytics", 
    "Environmental Monitoring", "Green Cloud Computing", "Sustainable IoT", "Energy Management Systems", 
    "Resource Planning AI", "Climate Modeling AI", "Eco-Logistics AI", "Green Manufacturing AI", 
    "Sustainable Agriculture AI", "Water Management AI"
]

preferences = ["accuracy", "speed", "mix"]

# Load the dataset once when the script starts
data = pd.read_csv(r"C:\Users\TIWAR\Desktop\tech\ecoaifinder_shashank\generated_tools_data_sequential.csv")

# Calculate Environmental Score for the dataset
data["Environmental Score"] = (
    (data["Energy Efficiency"] + data["Waste Reduction"] + data["Resource Efficiency"] + data["Lifetime Durability"]) /
    (data["Carbon Footprint"] + data["Energy Consumption"] + data["Water Usage"])
)

# Function to process the user query and extract category and preference
def extract_category_and_preference(user_query):
    try:
        # Encode the user query and predefined lists
        user_query_embedding = model.encode(user_query)
        categories_embeddings = model.encode(categories)
        preferences_embeddings = model.encode(preferences)
        
        # Find the most similar category and preference
        category_scores = util.cos_sim(user_query_embedding, categories_embeddings)[0]
        preference_scores = util.cos_sim(user_query_embedding, preferences_embeddings)[0]
        
        # Get the category and preference with the highest similarity score
        matched_category = categories[category_scores.argmax()]
        matched_preference = preferences[preference_scores.argmax()]
        
        return {
            "Category": matched_category,
            "Preference": matched_preference
        }
    except Exception as e:
        return f"An error occurred: {str(e)}"

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
    category_tools.loc[:, "Score"] = (
        alpha * category_tools["Accuracy"] +
        beta * category_tools["Speed"] +
        gamma * category_tools["Environmental Score"]
    )

    # Sort tools by score and select top_n
    top_recommendations = category_tools.nlargest(top_n, "Score")
    
    recommendations = []
    for index, row in top_recommendations.iterrows():
        recommendations.append({
            "Tool": row['Tool'],
            "Score": round(row['Score'], 2),
            "Accuracy": row['Accuracy'],
            "Speed": row['Speed'],
            "Energy Efficiency": row['Energy Efficiency'],
            "Carbon Footprint": row['Carbon Footprint'],
            "Waste Reduction": row['Waste Reduction'],
            "Energy Consumption": row['Energy Consumption'],
            "Resource Efficiency": row['Resource Efficiency'],
            "Water Usage": row['Water Usage'],
            "Lifetime Durability": row['Lifetime Durability']
        })

    return recommendations


# Define the Pydantic model to handle input
class UserQuery(BaseModel):
    user_query: str


# API endpoint to receive user query and return recommendations
@app.post("/recommendations/")
async def recommend(user_query: UserQuery):
    # Extract category and preference from the user query
    result = extract_category_and_preference(user_query.user_query)
    if isinstance(result, str):  # Error in extraction
        raise HTTPException(status_code=400, detail=result)

    category = result['Category']
    preference = result['Preference']

    # Get recommendations based on the extracted category and preference
    recommendations = recommend_tools(category, preference)
    
    return {"recommendations": recommendations}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("chatrun:app", host="127.0.0.1", port=8001, reload=True)

# To run the FastAPI app on a different port, use the following command:
# uvicorn chatrun:app --host 127.0.0.1 --port 8001
