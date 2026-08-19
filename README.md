Jarvis — Local AI Voice Assistant

Jarvis is a personal AI voice assistant built with Python, designed to provide a hands-free interaction experience using local AI technologies.

The project combines wake-word detection, speech recognition, local Large Language Models (LLMs), and voice interaction to create an assistant capable of understanding and responding to spoken commands.

The main goal of the project is to explore how far a fully local AI assistant can be taken while maintaining a modular and extensible architecture.

Features
-Voice input through a microphone
-Wake-word detection using "Hey Jarvis"
-Speech-to-text using Whisper
-Local AI processing using Ollama and local LLMs
-Voice interaction
-Real-time command processing
-Designed around local AI processing and privacy
-Modular architecture for adding new capabilities

Architecture:
Microphone
    │
    ▼
Wake Word Detection
    │
    │  "Hey Jarvis"
    ▼
Audio Recording
    │
    ▼
Whisper
Speech → Text
    │
    ▼
Local LLM
(Ollama)
    │
    ▼
Response
    │
    ▼
Text-to-Speech
    │
    ▼
Jarvis

Technologies:
Python
Ollama
Whisper / Faster-Whisper
OpenWakeWord
SoundDevice
NumPy
Local LLMs such as Qwen 2.5 7b

Project Goals

Jarvis is an ongoing personal project. The goal is to gradually transform it from a simple voice interface into a more capable local assistant that can:

Understand natural language commands
Interact with the operating system
Execute useful tasks
Work with applications and files
Maintain conversational context
Integrate additional AI capabilities
Operate as locally as possible

Status

Work in progress 

The project is currently under active development. Voice detection, speech recognition, and local LLM integration are being developed and tested incrementally.

New capabilities will be added as the architecture evolves.

Author:

Anthony Barquero

Computer Systems Engineering student and software developer from Costa Rica.
