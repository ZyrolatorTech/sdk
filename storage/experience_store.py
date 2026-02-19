import json

class ExperienceStore:

    @staticmethod
    def save(agent, filepath="agent_state.json"):
        data = {
            "identity": agent.identity.summary(),
            "experiences": agent.memory.to_dict()
        }

        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load(filepath="agent_state.json"):
        with open(filepath, "r") as f:
            return json.load(f)
