# Sustainable AI Tools API

This repository provides an API that recommends sustainable AI tools based on user input. The API is built using **FastAPI** and allows for interactive recommendations through text and dropdown selection.

## Running the API

### 1. Clone the repo and install dependencies:

First, clone the repository and install the required Python dependencies:

    ```
    bash
    git clone https://github.com/yourusername/sustainable-ai-tools.git
    cd sustainable-ai-tools
    pip install -r requirements.txt
    ```

### 2. Place required files in the appropriate paths:

Ensure that the following files are placed in the correct paths for the application to work:

- sustainable_ai_tools_dataset3.csv (Dataset for the AI tools)
- model.h5 (Trained model file)

### 3. Start the FastAPI servers:

- For category and preference selection (Dropdown):
  Run the server that handles category and preference dropdown selections:
        ```
        bash
        uvicorn run:app --host 127.0.0.1 --port 8000 --reload
        ```

- For text-based prompt (Text-based user input):
  Run the server that handles text-based input prompts:
        ```
        bash
        uvicorn chatrun:app --host 127.0.0.1 --port 8001
        ```

### 4. Access the API:

- Access the category and preference dropdown API at:
        ```
        http://127.0.0.1:8000/recommendations/
        ```
  This provides an interactive documentation for the dropdown-based selection of categories and preferences.

- Access the text prompt API at:
        ```
        http://127.0.0.1:8001/
        ```
  This allows the user to send text prompts for recommendations.

### 5. Example API Request (Body: Raw)

- For the dropdown API at http://127.0.0.1:8000/recommendations/, you can send a JSON body like:
    ```
    json
    {
    "category": "Sustainable IoT",
    "preference": "accuracy"
    }
    ```
  This request will return a recommendation based on the selected category and preference.

- For text-based API at http://127.0.0.1:8001/recommendations/, you can send a JSON body like:
    ```
    json
    {
    "user_query": "Please recommend tools for energy-efficient machine learning with a focus on accuracy."
    }
This request will return a recommendation based on the text-based input.
