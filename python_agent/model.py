import torch
import torch.nn as nn
import torch.nn.functional as F

class PolicyNetwork(nn.Module):
    def __init__(self, input_dim=3, hidden_dim=64, output_dim=5):
        super(PolicyNetwork, self).__init__()

        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)

        # Discrete action output (5 actions)
        self.action_head = nn.Linear(hidden_dim, output_dim)

        # Value head (for PPO critic)
        self.value_head = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))

        action_logits = self.action_head(x)
        action_probs = F.softmax(action_logits, dim=-1)

        state_value = self.value_head(x)

        return action_probs, state_value
