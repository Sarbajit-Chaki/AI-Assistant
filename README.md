# Jarvis AI - Your Personal Voice Assistant

Jarvis AI is a Python-based voice assistant that helps you perform various tasks using voice commands. Inspired by the AI assistant in the Iron Man movies, Jarvis AI can handle tasks like opening websites, providing weather updates, playing music, and more.

## Features

- **Voice Commands**: Interact with Jarvis AI using natural language voice commands.
- **Task Automation**: Perform tasks such as opening websites, fetching weather updates, and playing music hands-free.
- **Generative AI**: Utilizes Google's Generative AI model for generating text-based responses to prompts.
- **Configurable AI**: Customize and configure the behavior of the AI assistant to suit your preferences.
- **Speech Recognition**: Uses the SpeechRecognition library to convert speech to text for processing commands.
- **Text-to-Speech**: Utilizes the PyWin32 library to convert text responses to speech for natural interaction.

## Usage

1. **Installation**:
   - Clone the repository:
     ```bash
     git clone https://github.com/Sarbajit-Chaki/AI-Assistant.git
     cd AI-Assistant
     ```

   - Configure API keys:
     Create a `config.py` file and add your OpenWeatherMap and Google Generative AI API keys:
     ```python
     weather_apiID = "your_openweathermap_api_key"
     api_key = "your_google_generative_ai_api_key"
     ```

2. **Running Jarvis AI**:
   - Run the main script:
     ```bash
     python main.py
     ```
   - Jarvis AI will greet you and wait for voice commands. Simply speak out your command, and Jarvis AI will respond accordingly.

3. **Available Commands**:
   - Open websites like YouTube, Wikipedia, Stack Overflow, or Google.
   - Fetch current weather information by providing the city name.
   - Play calming and healing music.
   - Ask Jarvis AI to generate text-based responses using the Generative AI model.
   - Configure and reset the AI as needed.

## Configuration

Jarvis AI can be configured to suit your preferences. You can adjust parameters such as speech recognition settings, AI response generation configuration, and safety settings for content generation.

## Contributing

Contributions to Jarvis AI are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to open an issue or submit a pull request.

