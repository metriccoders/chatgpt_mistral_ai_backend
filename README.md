# Mistral AI Model API

## Overview
This is a FastAPI application that serves as an API endpoint for the Mistral AI model. The API allows users to get answers from the Mistral AI model.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/metriccoders/chatgpt_mistral_ai_backend.git
    ```

2. Navigate to the project directory:
    ```bash
    cd chatgpt_mistral_ai_backend
    ```
## Usage
1. Install all the required dependencies: llama_cpp, fastapi, uvicorn and pydantic.
2. Download the Mistral_ai.gguf model from https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF/tree/main
3. Update the path to the Mistral_ai.gguf model in the code
4. Start the server:
    ```bash
    uvicorn main:app --reload
    ```
## License
MIT
