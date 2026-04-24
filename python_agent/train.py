
import numpy as np
from agent import PPOAgent
from utils import normalize_state, compute_reward
import torch

# Simulated environment (replace later with OMNeT++ feedback if needed)
def simulate_network():
    rtt = np.random.uniform(60, 80)
    loss = np.random.uniform(0.0, 0.01)
    throughput = np.random.uniform(150, 250)

    return rtt, loss, throughput

agent = PPOAgent()

EPISODES = 50
STEPS = 600

for ep in range(EPISODES):
    for step in range(STEPS):

        rtt, loss, throughput = simulate_network()

        state = normalize_state(rtt, loss, throughput)

        action_idx, action, log_prob = agent.select_action(state)

        # simulate effect of action
        throughput = throughput * (1 + action)

        reward = compute_reward(rtt, loss, throughput)

        agent.store((state, action_idx, reward, log_prob))

    agent.update()

    print(f"Episode {ep} completed")

# Save trained model
torch.save(agent.policy.state_dict(), "ppo_quic_model.pt")
