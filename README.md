# AI-Powered Telegram ChatBot with Conversation History

This project is an AI-powered Telegram bot built using `aiogram` and `g4f`. The bot leverages artificial intelligence to generate conversational responses, providing an interactive experience for users. It keeps track of conversation history, enabling more context-aware interactions and offering users the option to reset the chat with a simple command.

## Features

- **AI-Powered Responses**: Uses AI to generate contextually relevant replies, creating an engaging chat experience.
- **Maintains Conversation History**: Tracks and remembers conversation history with each user for more coherent replies.
- **Chat History Trimming**: Automatically trims conversation history to a specified character limit for efficiency.
- **Clear Chat History**: Users can clear their conversation history with the `/clear` command.
- **Error Handling**: Provides a fallback response if the AI model or API encounters an error.

## Prerequisites

- **Python 3.7+**
- **Telegram Bot Token**: Obtain your bot token from [BotFather](https://core.telegram.org/bots#botfather).

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2. **Install required packages**:
    ```bash
    pip install aiogram g4f
    ```

3. **Set up your environment**:
    - Replace `'TOKEN'` in the code with your actual Telegram bot token.

## Usage

1. **Run the bot**:
    ```bash
    python <script-name>.py
    ```

2. **Bot Commands**:
    - **`/clear`**: Clears the conversation history for the user, allowing for a fresh start in the conversation.

3. **Chat with the bot**:
    - Type any message to start a conversation with the AI. The bot will provide responses based on the context of the conversation history.

## Code Explanation

- **AI Integration**: Utilizes `g4f` to access an AI model that processes conversation history and generates responses.
- **`trim_history`**: Ensures conversation history stays within a character limit to prevent overloading the AI model.
- **Command Handlers**:
  - **`/clear`**: Clears the user's conversation history.
  - **Message Handler**: Receives user messages, sends them to the AI model, and returns the generated response.

## Error Handling

If the bot encounters an issue with the AI service, it sends a fallback message to the user, notifying them of the temporary error.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
