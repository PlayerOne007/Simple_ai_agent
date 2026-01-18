
# Simple AI Agent (Python)

This project demonstrates a minimal, rule-based AI agent implemented in Python.  
The agent follows a basic **perceive → decide → act** loop and runs as an interactive command-line application.

---

## Features

- Interactive command-line interface
- Rule-based decision making
- Simple and extensible agent architecture
- No external dependencies

---

## Project Structure
```
simple_ai_agent/
│
├── agent.py
└── README.md
```

## How to Run

1. Clone or download this repository.

2. Navigate to the project directory:

```
cd simple_ai_agent
```

3. Run code

```
python agent.py
```
## Usage

Once running, type messages into the terminal.

Example

```
You: hello
HelperBot: Hello! How can I help you?

You: what time is it?
HelperBot: The current time is 14:35:22.

You: bye
HelperBot: Goodbye! Have a great day.
```

Type ``exit`` or ``quit`` to stop the program.

## How It Works
The agent consists of four main steps:

2. Perceive – Receives user input

3. Decide – Chooses an action based on rules

4. Act – Executes the action

5. Run Loop – Repeats until exit

