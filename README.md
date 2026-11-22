python_phase_3

A Python learning project: a console-based AI Agent Console that simulates an LLM chat session, estimates token usage and cost, and saves the conversation log to a file.

Status: Work in progress. The console does not call a real LLM yet. Token counts are estimates. Connecting a real API is the next step.

Features
Interactive chat loop that runs until the user types exit or quit (case-insensitive)
Estimated token count per message (about 1.3 tokens per word)
Estimated cost per message and per session (placeholder rate: $0.002 per 1,000 tokens)
Chat log saved to chat_history.txt (append mode, UTF-8)
Chat history shown when the session ends
Input validation: empty messages are rejected with a clear error instead of crashing
How to run

Requires Python 3.

bash
python AI_Agent_Console_File_Handling.py

Type a message and press Enter. Type exit or quit to end the session.

Example output:

prompt: Hello there | current tokens : 3 | current_cost : 6e-06 and total tokens : 3 | ...
Project structure
File	Description
AI_Agent_Console_File_Handling.py	Main console: token and cost tracking, file logging, history reading
interactive_AI_session_and_cost_manager.py	Earlier version: interactive session and cost manager
Phase3 _Step_3.py	While loop and interactive chat automation
phase3_step1.py, phase3_step4.py	Earlier practice steps
List_of_Dictionaries.py	Practice with lists of dictionaries (the message format used by LLM APIs)
chat_history.txt	Sample chat log produced by the console
What I practiced
Functions and return values
while loops and session state
File handling: open() in "a" and "r" modes, with blocks, FileNotFoundError
Error handling with try / except and raise ValueError
f-string formatting
Lists and dictionaries
Next steps
[ ] Connect a real LLM API (Anthropic SDK)
[ ] Keep conversation memory and send it with each request
[ ] Use real token counts from the API response instead of estimates
[ ] Store chat history as JSON
[ ] Load API keys from a .env file (never committed to Git)
[ ] Handle network and API errors gracefully
Author

Belayet Hosen, learning Python with a goal of becoming an LLM engineer. GitHub: Shuvo1602153
