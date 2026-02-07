from tools.calculator import calculate
from agent.memory import add_to_memory, get_memory
from agent.brain import think


def run_agent():
    print("🤖 Agent started")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Agent: Bye!")
            break

        # store user input
        add_to_memory(f"You: {user_input}")

        # TOOL CHECK
        if user_input.lower().startswith("calc"):
            expr = user_input[4:].strip()
            result = calculate(expr)
            response = f"Result is {result}"

        else:
            # ✅ THIS CALLS GEMINI
            response = think(user_input, get_memory())

        # store response
        add_to_memory(f"Agent: {response}")

        print("Agent:", response)


