print("--- AI Chatbot Simulator Initialized ---")
print("Type 'exit' or 'quit' to end the conversation.\n")

is_rinnung = True
status = ["exit","quit"]

while is_rinnung:
    user_input = input("Your message here: ")
    if user_input in status:
        is_rinnung = False
        print("AI is shutting down ")
    else:
        print(f"I received your message : {user_input}")