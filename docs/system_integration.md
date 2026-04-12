# System Integration using PyBind11

## Overview

This project integrates a reinforcement learning (RL) agent with a network simulation environment using a PyBind11-based interface.

The goal is to enable adaptive congestion control decisions during simulation runtime.

---

## Integration Concept

The system is composed of:

* C++ simulation layer (QUIC / OMNeT++)
* Python RL agent
* PyBind11 interface connecting both components

---

## Interaction Flow

1. The simulator computes network state:

   * RTT
   * Throughput
   * Packet loss

2. These values are passed to the Python RL agent using PyBind11

3. The RL agent returns an action:

   * pacing rate adjustment

4. The simulator applies the action to control transmission behavior

---

## Design Choice

PyBind11 is used because:

* It enables direct C++ ↔ Python interaction
* It avoids external communication (e.g., sockets or files)
* It allows efficient function-level integration

---

## Implementation Note

The integration is designed at a control-loop level and focuses on decision-making rather than packet-level processing.

This approach ensures simplicity and feasibility within a simulation environment.
