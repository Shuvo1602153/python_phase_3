def messageToCalTokens(message):
    tokens = len(message.split())
    return round(1.3 * tokens)

def calculateCost(token):
    return token * 0.002
     
print("Welcome to AI Agent Console! I am ready to process your prompts.")

isRunning = True
sessionStatus = ["exit", "quit"]

while isRunning:
    userMessage = input("Enter your prompt/message (or type 'exit' to quit): ")
    
    
    if userMessage in sessionStatus :
        isRunning = False
        print("Your session is closing... Good Bye!")
    
    else:
        try:
            tokens = messageToCalTokens(userMessage)
            if tokens < 0:
                raise ValueError("Tokens can't be negative!")
            if not userMessage.strip():
                print(" Message can't be empty! ")
            totalCost = calculateCost(tokens)
            print(f"For {tokens} tokens your cost is = {totalCost}")
        
        except ValueError as e:
            print(f"Error Handled Successfully -> {e}")
