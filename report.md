# Customer Support Chatbot Evaluation Report

## Introduction
This project evaluated the feasibility of deploying a local Large Language Model (LLM) for automated customer support in an e-commerce context. Using **Ollama** and **Llama 3.2 3B**, we compared two prompting techniques—**Zero-Shot** and **One-Shot**—across 20 diverse customer queries.

## Methodology
- **Model**: Llama 3.2 3B (Quantized)
- **Deployment**: Local Ollama server (Offline)
- **Data**: 20 technical support queries from the Ubuntu Dialogue Corpus, adapted for e-commerce (Chic Boutique).
- **Evaluation Criteria**: 
  - **Relevance (1-5)**: Alignment with the customer's intent.
  - **Coherence (1-5)**: Grammatical correctness and readability.
  - **Helpfulness (1-5)**: Actionability and accuracy of the advice.

## Results & Analysis

### Quantitative Summary (Average Scores)
| Metric | Zero-Shot | One-Shot |
|--------|-----------|----------|
| Relevance | **4.85** | 3.95 |
| Coherence | **5.00** | 5.00 |
| Helpfulness | **4.60** | 3.70 |

### Qualitative Observations
1.  **Zero-Shot Excellence**: The Llama 3.2 3B model demonstrated a remarkably strong internal model of "helpful customer support." Even without examples, it consistently provided detailed, step-by-step instructions for tasks like password resets and shipping tracking.
2.  **One-Shot confusion**: Contrary to expectations, One-Shot prompting sometimes degraded performance. 
    - **Context Leaking**: In Query 10 (notification preferences), the model hallucinated an answer about "in-store pickup," likely getting confused by the brevity of the one-shot example or over-generalizing from a limited context.
    - **Brevity vs. Detail**: One-Shot responses were often more concise but missed out on helpful troubleshooting steps that Zero-Shot included.
3.  **Refusal Patterns**: One-Shot tended to "refuse" or claim ignorance more often for specific requests (e.g., Query 17 regarding delivery time slots), whereas Zero-Shot attempted to provide a path forward (e.g., "log into your account and check the My Orders section").

## Conclusion & Limitations
Llama 3.2 3B is highly suitable for basic customer support tasks in an offline environment. It maintains high coherence and relevance. However, the project revealed that **Zero-Shot** is often more robust for general inquiries. 

### Limitations
- **Lack of Integration**: The chatbot cannot access "live" order data; it provides procedural guidance rather than account-specific data.
- **Hallucination Risk**: While rare in Zero-Shot, hallucinations can occur if the prompt structure is not carefully tuned.
- **Hardware Constraints**: Local inference speed is slower than cloud APIs, which could affect real-time interaction.

### Next Steps
- Implement **Retrieval-Augmented Generation (RAG)** to provide the model with actual store policies and product details.
- Fine-tune the one-shot examples to be more representative of broader query types.
