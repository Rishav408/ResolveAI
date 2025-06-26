# ResolvAI

ResolvAI is an offline AI-powered tool designed for small businesses to draft professional, empathetic responses to customer complaints. Using a local Large Language Model (LLM) via Ollama, it analyzes complaint text, aligns responses with company policies and business profiles, and ensures privacy by processing all data locally. Ideal for restaurants, small shops, or freelancers, ResolvAI saves time, enhances customer relations, and operates without internet dependency.

## Table of Contents

- Features
- Installation
- Usage
- Project Structure
- Dependencies
- Configuration
- Testing
- Contributing
- License
- Contact

## Features

- **Offline Operation**: Runs entirely locally, ensuring data privacy and accessibility in low-connectivity areas.
- **Empathetic Responses**: Generates professional, policy-compliant replies with customizable tones (e.g., empathetic, formal).
- **Business Profile Integration**: Incorporates restaurant history and special policies from profile documents.
- **Conversation History**: Maintains complete chat history during sessions.
- **User-Friendly Interface**: Streamlit-based GUI with sidebar navigation and chat-style interaction.
- **Local LLM Integration**: Uses lightweight LLMs (e.g., Mistral 7B, Llama3) via Ollama for efficient text processing.
- **Modular Design**: Extensible for additional features like multilingual support or email integration.

## Installation

### Prerequisites

- **Hardware**:
  - Minimum: 16GB RAM, CPU (e.g., Intel i5 or equivalent).
  - Recommended: NVIDIA GPU (e.g., RTX 3060 with 6GB VRAM) for faster inference.
- **Software**:
  - Python 3.8+.
  - Ollama (for local LLM inference).
  - SQLite (included with Python).
- **Operating System**: Linux, macOS, or Windows.

### Steps

1. **Install Python Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Install Ollama**:

   - Download and install Ollama from ollama.ai.

   - Pull your preferred LLM model:

     ```bash
     ollama pull llama3  # or mistral
     ```

   - Note: Use quantized models (e.g., `llama3:8b-q4`) for lower memory usage.

3. **Set Up Required Files**:

   - Create these text files in the project root:
     - `complaint.txt` - Sample customer complaints
     - `response.txt` - Template responses
     - `policies.txt` - Business policies
     - `veera_dhabha_profile.txt` - Business profile/history
   - Ensure all files use UTF-8 encoding.

## Usage

1. **Launch the Application**:

   ```bash
   streamlit run main.py
   ```

   - Opens a web interface at `http://localhost:8501`.

2. **Using the Interface**:

   - Left sidebar displays business profile.
   - Main chat area shows conversation history.
   - Right sidebar shows quick policy reference.
   - Bottom chat input for new complaints/questions.

3. **Features**:

   - Automatic policy-aware response generation.
   - Persistent chat history during session.
   - Business-context aware replies.

4. **Example Workflow**:

   - User: "My food arrived cold"
   - ResolvAI: "We sincerely apologize for this. As per our quality policy, we'd like to offer you a free replacement meal on your next visit. - Veera Dhabha"

## Project Structure

```
ResolvAI/
│
├── README.md                # Project documentation
├── main.py                  # Streamlit GUI and core logic
├── policies.db              # SQLite database for policies (legacy)
│
├── data/                    # Text data files
│   ├── complaint.txt        # Customer complaints
│   ├── response.txt         # Template responses
│   ├── policies.txt         # Business policies
│   └── veera_dhabha_profile.txt # Business profile
│
├── requirements.txt         # Python dependencies
```

## Dependencies

Updated `requirements.txt`:

```
langchain-community==0.2.1
streamlit==1.32.0
python-dotenv==1.0.1
ollama==0.2.1
langchain-core==0.2.2
```

Install with:

```bash
pip install -r requirements.txt
```

## Configuration

- **Key configurations**:
  - Set `OLLAMA_MODEL` in code (default: `llama3`).
  - Edit text files in `data/` directory:
    - Add business-specific policies.
    - Update profile information.
    - Maintain complaint/response templates.

## Testing

Run unit tests:

```bash
python -m unittest tests/test_resolver.py
```

Test coverage includes:

- Response generation with sample complaints.
- Policy alignment verification.
- Business profile integration.
- Chat history functionality.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit changes.
4. Push to branch.
5. Open a pull request.

**Guidelines**:

- Maintain UTF-8 encoding for all text files.
- Include tests for new features.
- Update documentation for changes.

