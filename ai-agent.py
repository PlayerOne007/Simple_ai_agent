class SimpleAIAgent:
    def __init__(self, name="Agent"):
        self.name = name

    def perceive(self, environment_input):
        return environment_input.lower()

    def decide(self, perception):
        if "hello" in perception or "hi" in perception:
            return "greet"
        elif "time" in perception:
            return "tell_time"
        elif "bye" in perception:
            return "farewell"
        else:
            return "unknown"

    def act(self, decision):
        if decision == "greet":
            return "Hello! How can I help you?"
        elif decision == "tell_time":
            from datetime import datetime
            return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
        elif decision == "farewell":
            return "Goodbye! Have a great day."
        else:
            return "I'm not sure how to respond to that."

    def run(self, environment_input):
        perception = self.perceive(environment_input)
        decision = self.decide(perception)
        return self.act(decision)


if __name__ == "__main__":
    agent = SimpleAIAgent("HelperBot")

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        response = agent.run(user_input)
        print(f"{agent.name}: {response}")
