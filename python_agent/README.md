# Python RL Agent

## Overview

This module contains the reinforcement learning (RL) agent used to control QUIC congestion behavior.

The agent is based on the Proximal Policy Optimization (PPO) algorithm and is responsible for selecting pacing rate adjustments based on observed network conditions.

---

## Functionality

The RL agent performs the following tasks:

* Receives network state:

  * Round-trip time (RTT)
  * Throughput
  * Packet loss

* Processes the state using a neural network model

* Outputs an action:

  * Multiplicative pacing rate adjustment

---

## Interaction with Simulation

The agent interacts with the simulation environment through a PyBind11-based interface.

At each control interval:

1. The simulation sends state information to the agent
2. The agent computes an action
3. The action is returned to the simulation

---

## Implementation Notes

* The PPO model is implemented in Python
* The architecture includes fully connected layers
* The design focuses on simplicity and interpretability

---

## Purpose

This module represents the decision-making component of the system, enabling adaptive congestion control in dynamic network conditions.
