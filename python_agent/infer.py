import torch
from model import PolicyNetwork
from utils import normalize_state

ACTION_SPACE = [-0.2, -0.1, 0.0, 0.1, 0.2]

class RLInference:
    def __init__(self, model_path="ppo_quic_model.pt"):
        self.model = PolicyNetwork()
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()

    def predict(self, rtt, loss, throughput):
        state = normalize_state(rtt, loss, throughput)

        state = torch.FloatTensor(state)
        probs, _ = self.model(state)

        action_idx = torch.argmax(probs).item()

        return ACTION_SPACE[action_idx]
