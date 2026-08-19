# 🤖 Jarvis — Local AI Voice Assistant
⭐ If you find this project interesting, feel free to explore or fork the repository and gift me a star!.

Jarvis is a personal AI voice assistant built with Python and designed to provide a hands-free interaction experience using local AI technologies.

The project combines wake-word detection, speech recognition, local Large Language Models (LLMs), and voice interaction to create an assistant capable of understanding and responding to spoken commands.

The main goal of the project is to explore how far a locally running AI assistant can be taken while maintaining a modular and extensible architecture.

## ✨ Features

- 🎙️ Voice input through a microphone
- 👂 Wake-word detection using **"Hey Jarvis"**
- 📝 Speech-to-text using **Whisper / Faster-Whisper**
- 🧠 Local AI processing using **Ollama**
- 🤖 Support for local LLMs such as **Qwen**
- 🔊 Voice interaction
- ⚡ Real-time command processing
- 🔒 Designed around local processing and privacy
- 🧩 Modular architecture for adding new capabilities

## 🏗️ Architecture

Jarvis is divided into several components, with each module responsible for a specific part of the voice interaction pipeline.

```text
┌──────────────────────┐
│      Microphone      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Wake Word Engine   │
│    "Hey Jarvis"      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Audio Recording    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│        Whisper       │
│    Speech → Text     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     Ollama / LLM     │
│    Local Inference   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       Response       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Voice Output      │
└──────────────────────┘
```

🧩 Project Structure
```text
Jarvis/
├── asistente.py       # Assistant logic
├── herramientas.py    # Assistant tools and actions
├── ia.py              # Local AI / LLM interaction
├── jarvis.py          # Jarvis functionality
├── main.py            # Application entry point
├── microfono.py       # Microphone and audio capture
├── transcribir.py     # Speech-to-text
├── wakeword.py        # Wake-word detection
├── test_wakeword.py   # Wake-word testing
├── .gitignore
└── README.md
```

🛠️ Technologies
```js
Python
Ollama
Whisper / Faster-Whisper
OpenWakeWord
SoundDevice
NumPy
Qwen 2.5 7B
Local Large Language Models (LLMs)
```

🔄 How It Works

Jarvis follows a voice-processing pipeline:

1. Wake-word detection

The assistant continuously monitors the microphone for the wake word:

"Hey Jarvis"

OpenWakeWord is used to detect when the assistant should begin listening for a command.

2. Audio capture

Once the wake word is detected, Jarvis records the user's command through the microphone.

3. Speech recognition

The recorded audio is processed using Whisper to convert speech into text.

Voice → Text
4. Local AI processing

The resulting text is sent to a locally running LLM through Ollama.

User command
     ↓
Ollama
     ↓
Local LLM
     ↓
Response

This allows the project to experiment with AI inference without relying entirely on external AI APIs.

5. Assistant response

Jarvis processes the generated response and provides it back to the user through voice interaction.


🎯 Project Goals

Jarvis is an ongoing personal project focused on exploring local AI and voice-based human-computer interaction.

The long-term goal is to gradually transform Jarvis from a voice interface into a more capable personal assistant that can:

Understand natural language commands
Interact with the operating system
Execute useful tasks
Work with applications and files
Maintain conversational context
Integrate additional AI capabilities
Operate as locally as possible
🧠 Why Local AI?

One of the main motivations behind Jarvis is exploring what can be accomplished with AI running locally.

Running models locally provides opportunities to experiment with:

Privacy
Offline processing
Local inference
Model selection
Hardware acceleration
AI system architecture
Reduced dependence on external APIs
🚧 Project Status

# Work in Progress 🚧

Jarvis is an active personal project.

The current development focus includes improving:

Wake-word detection
Audio recording reliability
Speech recognition accuracy
Local LLM integration
Voice interaction
Assistant capabilities

New features and improvements will be added as the architecture evolves.

```text
Author: Anthony Barquero
Email: thony.dev@hotmail.com
```

