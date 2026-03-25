# Setup Instructions

This guide explains how to set up and run the Chic Boutique Offline Customer Support Chatbot.

## Prerequisites
1.  **Ollama**: Install from [ollama.com](https://ollama.com).
2.  **Llama 3.2 3B Model**: Pull the model by running:
    ```bash
    ollama pull llama3.2:3b
    ```
3.  **Python 3.8+**: Ensure Python is installed.

## Installation
1.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```
2.  **Activate the Virtual Environment**:
    - Windows: `venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
3.  **Install Dependencies**:
    ```bash
    pip install requests datasets
    ```

## Running the Chatbot
1.  **Start Ollama**: Ensure the Ollama application is running in the background.
2.  **Execute the Script**:
    ```bash
    python chatbot.py
    ```
3.  **View Results**: Once complete, the results will be saved in `eval/results.md`.

## Project Structure
- `chatbot.py`: Main script to query the model and log results.
- `prompts/`: Contains Zero-Shot and One-Shot templates.
- `eval/results.md`: Generated log of all queries and responses with scores.
- `report.md`: Detailed analysis of the experiment findings.
