def token_calculation(message):
    return int(round(len(message.split()) * 1.3))

def token_cost(tokens):
    return tokens * 0.002 / 1000


def save_to_log_file(file_name, log_lines):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(log_lines + "\n")


def read_chat_history(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "File is not found yet."


log_file = "chat_history.txt"

print("Welcome to AI console... I am ready to process your prompts/message....")

isRunning = True
total_tokens = 0
total_cost = 0
session_Status = ["exit", "quit"]

while isRunning:
    user_message = input("Please type your message or type 'exit'/'quit' to stop: ")
    if user_message.strip().lower() in session_Status:
        isRunning = False
        print("Your session is closing... ")
        print(f"Your session token:{total_tokens} | cost:{total_cost:.2f}")
        print("-----Save chat history-----")
        print(read_chat_history(log_file))
        print("Good bye... ")
    else:
        try:
            if not user_message.strip():
                raise ValueError("Message can't be empty")
            current_tokens = token_calculation(user_message)
            if current_tokens < 0:
                raise ValueError("Tokens can't be negative!")
            total_tokens += current_tokens
            current_cost = token_cost(current_tokens)
            total_cost += current_cost

            log_entry = (
                f"prompt: {user_message} | current tokens : {current_tokens} "
                f"and total tokens : {total_tokens} | current_cost : {current_cost} "
                f"and total cost : {total_cost}"
            )
            save_to_log_file(log_file, log_entry)
            print(log_entry)
        except ValueError as e:
            print(f"Error Handeld successfully -> {e}")