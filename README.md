# Telegram ChatBot with Conversation History

This project is a Telegram bot built with `aiogram`, which maintains a conversation history with users. It uses `g4f` for generating responses and supports clearing the chat history with a command.

## Features

- **Maintains Conversation History**: Tracks and remembers the conversation history with each user.
- **Chat History Trimming**: Automatically trims the conversation history to a specified character limit.
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
    - **`/clear`**: Clears the conversation history for the user.

3. **Chat with the bot**:
    - Simply type your messages to start interacting with the bot.

## Code Explanation

- **`trim_history`**: Trims conversation history to a maximum length to ensure it stays within the limit.
- **Command Handlers**:
  - **`/clear`**: Clears the user's conversation history.
  - **Message Handler**: Receives user messages, sends them to the AI model, and returns the generated response.

## Error Handling

If the bot encounters an error while generating a response, it will send a fallback message to the user notifying them of the issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
