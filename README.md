# ✈️ AI Travel Planner Agent

## Overview

Planning a trip often involves checking the weather, searching for hotels, finding popular attractions, and estimating the overall budget. To simplify this process, I built an AI-powered Travel Planner Agent that combines multiple travel-related tools into a single conversational interface.

The application allows users to interact naturally and receive travel recommendations, hotel suggestions, attraction details, weather information, and budget estimates through an AI-powered chat experience.

---

## Features

* 🌤️ Real-time weather information for destinations
* 🏨 Hotel recommendations using Geoapify API
* 📍 Tourist attraction discovery
* 💰 Travel budget estimation
* 🤖 AI-generated travel itineraries
* 💬 Chat-based interface built with Streamlit
* 🧠 Conversation memory using Streamlit session state
* 🔀 Query routing to appropriate travel tools

---

## How It Works

The application follows a tool-based agent architecture:

1. The user enters a travel-related query.
2. A routing component identifies the user's intent.
3. The relevant tool is selected and executed.
4. Tool outputs are passed to the language model.
5. The AI generates a final response or travel itinerary.

Examples of supported queries:

* What is the weather in Goa?
* Show hotels in Hyderabad
* Tourist attractions in Jaipur
* Budget for 5 days in Goa
* Plan a 3-day trip to Goa

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & Agent Components

* Hugging Face Inference API
* Qwen 2.5 3B Instruct
* LangChain Tools

### APIs

* Weatherstack API
* Geoapify API
* OpenTripMap API

---

## Project Structure

```bash
AI-Travel-Planner-Agent/
│
├── agent/
│   ├── router.py
│   └── travel_agent.py
│
├── tools/
│   ├── weather.py
│   ├── hotel.py
│   ├── attractions.py
│   └── budget.py
│
├── llm.py
├── memory.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd AI-Travel-Planner-Agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root and add:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
WEATHERSTACK_API_KEY=your_weatherstack_api_key
GEOAPIFY_API_KEY=your_geoapify_api_key
OPENTRIPMAP_API_KEY=your_opentripmap_api_key
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

---

## Sample Queries

```text
What is the weather in Goa?

Show hotels in Goa

Tourist attractions in Goa

Budget for 4 days in Goa

Plan a 3 day trip to Goa
```

---

## Challenges Faced

* Integrating multiple travel-related APIs
* Designing a routing mechanism for tool selection
* Handling API response errors gracefully
* Building a conversational experience with memory
* Creating a modular architecture that can be extended in the future

---

## Future Improvements

* Flight search integration
* Personalized travel recommendations
* Multi-city trip planning
* Interactive maps
* LangGraph-based multi-agent workflow
* Travel history and user profiles

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Building AI-powered applications
* Tool-based agent architectures
* API integration
* Prompt engineering
* Streamlit deployment
* Hugging Face inference models
* Designing end-to-end GenAI projects

---

## Author

**Chaitanya Varma Mudunuru**

Passionate about Generative AI, LLMs, LangChain, and building real-world AI applications.
