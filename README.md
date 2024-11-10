# EcoAIFinder  Platform

Welcome to the EcoAIFinder Platform, a comprehensive solution for recommending eco-friendly AI tools. This platform allows users to receive recommendations through two methods: selecting a category and preference or inputting a text-based query. The backend is powered by FastAPI, and the frontend is built with React and Vite.

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Backend](#backend)
  - [Running the Backend](#running-the-backend)
  - [API Endpoints](#api-endpoints)
- [Frontend](#frontend)
  - [Running the Frontend](#running-the-frontend)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure
   ```bash

EcoAI
│
├── Backend
│   ├── chatrun.py
│   ├── run.py
│   ├── model.py
│   ├── dtagen.py
│   ├── genrate_dataset.py
│   ├── readme.md
│   └── requirements.txt
│
├── Frontend
│   ├── src
│   │   ├── components
│   │   ├── data
│   │   ├── App.jsx
│   │   └── index.jsx
│   ├── public
│   ├── README.md
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js and npm
- FastAPI
- Postman (for API testing)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ShashankSingh614/EcoAIFinder.git
   cd EcoAIFinder
   ```

2. **Install Backend Dependencies:**

   Navigate to the `Backend` directory and install the required Python packages:

   ```bash
   cd Backend
   pip install -r requirements.txt
   ```

3. **Install Frontend Dependencies:**

   Navigate to the `Frontend` directory and install the necessary npm packages:

   ```bash
   cd ../Frontend
   npm install
   ```


### Running the Backend

1. **Run the Category and Preference API:**

   ```bash
   uvicorn port8000:app --host 127.0.0.1 --port 8000 --reload
   ```

2. **Run the Text-Based Query API:**

   ```bash
   uvicorn port8001:app --host 127.0.0.1 --port 8001 --reload
   ```
## Backend

The backend is built using FastAPI and provides two main endpoints for recommendations.

### API Endpoints

- **Category and Preference Selection:**

  - **Endpoint:** `http://127.0.0.1:8000/recommendations/`
  - **Method:** POST
  - **Request Body:**

    ```json
    {
      "category": "Sustainable IoT",
      "preference": "accuracy"
    }
    ```

- **Text-Based Query:**

  - **Endpoint:** `http://127.0.0.1:8001/recommendations/`
  - **Method:** POST
  - **Request Body:**

    ```json
    {
      "user_query": "Please recommend tools for energy-efficient machine learning with a focus on accuracy."
    }
    ```

## Frontend

The frontend is developed using React and Vite, providing an interactive user interface for selecting categories and entering text queries.

### Running the Frontend

Navigate to the `Frontend` directory and start the development server:

```bash
npm run dev
```

This will launch the application at `http://localhost:5173`.

## Usage

1. **Category and Preference Selection:**

   - Navigate to the appropriate section on the website.
   - Select a category and preference to receive recommendations.

2. **Text-Based Query:**

   - Enter a query describing your AI tool requirements.
   - Submit the query to receive tailored recommendations.

## Contributing

We welcome contributions to enhance the EcoAI Finder Platform. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE file](/LICENSE.txt) file for details.
