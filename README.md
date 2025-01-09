# AI Travel Agent App

## Overview

The **AI Travel Agent App** helps users plan their trips effortlessly. It leverages OpenAI's GPT API to provide personalized travel suggestions based on user preferences.

## Features

- Plan trips based on preferences like budget, location, and activities.
- Generate detailed itineraries and recommendations for destinations, accommodations, and more.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ahsan-specs/AI-Travel-Agent-App.git
   cd AI_Travel_Agent_App
   ```



2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key:

   - Create a `.env` file in the project root directory.
   - Add the following line to the `.env` file:

     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Usage

1. Run the application:

   ```bash
   python app/main.py
   ```

2. Enter your travel preferences when prompted (e.g., "I want a 7-day trip to Europe on a $2000 budget").

3. Get personalized travel suggestions.

## Project Structure

```
AI_Travel_Agent_App/
|-- app/
|   |-- main.py
|-- requirements.txt
|-- README.md
|-- .gitignore
```

## License

This project is licensed under the MIT License. Feel free to use and modify it.

## Contributing

Contributions are welcome! Submit a pull request or open an issue for suggestions or improvements.

## Acknowledgments

- OpenAI for their powerful GPT API.
- The Python community for their extensive libraries and tools.
