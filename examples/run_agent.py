from core.agent import ZyrolatorAgent
from storage.experience_store import ExperienceStore

if __name__ == "__main__":
    agent = ZyrolatorAgent(
        name="Atlas",
        purpose="Build resilient distributed intelligence",
        traits=["calm", "analytical"]
    )

    agent.experience("Handled system isolation failure", 0.85)
    agent.experience("Optimized multi-agent coordination", 0.9)

    response = agent.respond(
        context="Design strategy for isolated autonomous agents",
        stress_level=0.3
    )

    print(response)

    ExperienceStore.save(agent)
