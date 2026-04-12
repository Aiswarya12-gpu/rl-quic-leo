# Example interaction with C++ module (conceptual)

import quic_rl

# Get network state

state = quic_rl.get_state()
print("State:", state)

# Example RL decision

action = 1.1  # increase pacing by 10%

# Apply action

quic_rl.apply_action(action)
