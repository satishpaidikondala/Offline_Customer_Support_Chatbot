import requests
import json
import os

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# 20 adapted e-commerce queries
QUERIES = [
    "How do I upgrade to the latest Chic Boutique premium membership?",
    "My discount code is not working at checkout.",
    "How do I track the shipping status of my recent order?",
    "I can't find the 'Return Item' button in my account dashboard.",
    "How do I reset my account password if I've forgotten it?",
    "My payment was processed twice for the same order.",
    "How do I add a new shipping address to my profile?",
    "My shopping cart is full, but I can't proceed to checkout.",
    "The order confirmation page failed to load after payment.",
    "How do I update the notification preferences for my account?",
    "I forgot my login email, how can I access my account?",
    "The product images are not loading on the mobile app.",
    "How do I apply multiple gift cards to a single order?",
    "My account is locked after too many failed login attempts.",
    "Is it safe to store my credit card details on your site?",
    "I'm getting an error when trying to access my order history.",
    "How do I change the delivery time slot for my order?",
    "The app crashes every time I try to add an item to the cart.",
    "What is the difference between standard and express shipping?",
    "How do I download the invoice for my previous purchases?",
]

def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        return json.loads(response.text).get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return "Error: Could not get a response from the model."

def main():
    # Load templates
    with open("prompts/zero_shot_template.txt", "r") as f:
        zero_shot_template = f.read()
    with open("prompts/one_shot_template.txt", "r") as f:
        one_shot_template = f.read()

    # Ensure eval directory exists
    os.makedirs("eval", exist_ok=True)

    results_file = "eval/results.md"
    
    with open(results_file, "w", encoding="utf-8") as f:
        f.write("# Evaluation Results\n\n")
        f.write("## Scoring Rubric\n\n")
        f.write("- **Relevance (1-5)**: How well does the response address the customer's query?\n")
        f.write("- **Coherence (1-5)**: Is the response grammatically correct and easy to understand?\n")
        f.write("- **Helpfulness (1-5)**: Does the response provide a useful, actionable answer?\n\n")
        f.write("| Query # | Customer Query | Prompting Method | Response | Relevance (1-5) | Coherence (1-5) | Helpfulness (1-5) |\n")
        f.write("|---------|----------------|-----------------|----------|-----------------|-----------------|-------------------|\n")

        for i, query in enumerate(QUERIES, 1):
            print(f"Processing query {i}/20: {query}")
            
            # Zero-Shot
            zero_shot_prompt = zero_shot_template.format(query=query)
            zero_shot_response = query_ollama(zero_shot_prompt).replace("\n", " ")
            f.write(f"| {i} | {query} | Zero-Shot | {zero_shot_response} | | | |\n")
            
            # One-Shot
            one_shot_prompt = one_shot_template.format(query=query)
            one_shot_response = query_ollama(one_shot_prompt).replace("\n", " ")
            f.write(f"| {i} | {query} | One-Shot | {one_shot_response} | | | |\n")

    print(f"Done! Results written to {results_file}")

if __name__ == "__main__":
    main()
