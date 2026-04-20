

#  RL-Based QUIC Congestion Control in LEO Satellite Networks

## Overview

This project presents a simulation-based study on improving QUIC congestion control using reinforcement learning (RL) in Low Earth Orbit (LEO) satellite networks. The work focuses on designing an adaptive control mechanism capable of responding to highly dynamic network conditions caused by satellite mobility and frequent topology changes.

The system combines a C++-based network simulation environment with a Python-based RL agent, enabling a hybrid architecture where protocol execution and decision-making are decoupled.

---

## System Architecture

The system is structured into three main components:

* **C++ Simulation Layer (OMNeT++)**
  Handles network modeling, packet transmission, and QUIC protocol behavior.

* **Python RL Agent**
  Implements a reinforcement learning model that observes network conditions and outputs control decisions.

* **Integration Layer (PyBind11)**
  Enables efficient interaction between the simulation and the RL agent through a lightweight C++–Python binding interface.

---

## Control Loop Architecture

```
+-----------------------------------------------------+
|                 OMNeT++ Simulation (C++)             |
|                                                     |
|   QUIC Protocol Execution                           |
|   Network State Extraction                          |
|   (RTT, Throughput, Loss)                           |
|                                                     |
+----------------------|------------------------------+
                       |
                       |  (State via PyBind11)
                       ↓
+-----------------------------------------------------+
|              Python RL Agent (PPO Model)             |
|                                                     |
|   Input: Network State                              |
|   Policy Network (Neural Model)                     |
|   Output: Action (Pacing Adjustment Factor)         |
|                                                     |
+----------------------|------------------------------+
                       |
                       |  (Action via PyBind11)
                       ↓
+-----------------------------------------------------+
|             QUIC Congestion Control Layer           |
|                                                     |
|   Apply Action → Adjust Pacing Rate                 |
|                                                     |
+-----------------------------------------------------+

          Closed-loop control (per control interval)
```

### Control Loop Explanation

The system operates as a closed-loop control mechanism during simulation runtime. At each control interval, the simulator extracts network state parameters and passes them to the RL agent via the PyBind11 interface. The agent computes a pacing rate adjustment, which is applied back to the QUIC congestion control logic.

This design enables adaptive decision-making without modifying the internal protocol structure, ensuring modularity and experimental flexibility.

---

## Motivation

Traditional congestion control algorithms (e.g., BBR) rely on fixed heuristics and may struggle to adapt to highly dynamic environments such as LEO satellite networks.

Frequent handovers and fluctuating delays require adaptive mechanisms capable of responding to non-stationary conditions. Reinforcement learning provides a framework for learning such adaptive behavior directly from observed network dynamics.

---

## Design Rationale

The system is intentionally designed to operate at the control level rather than per-packet level. This reduces computational overhead and ensures compatibility with reinforcement learning inference constraints.

A compact state representation is used to balance model expressiveness and stability. The objective is not to fully model the network, but to provide sufficient information for adaptive decision-making under dynamic conditions.

---

## Technical Approach

* **Reinforcement Learning Algorithm:** Proximal Policy Optimization (PPO)

* **State Representation:**

  * RTT
  * Packet loss
  * Throughput

* **Action:**

  * Continuous pacing rate adjustment (multiplicative factor)

* **Reward Function:**

[
r_t = \frac{\text{Throughput}_t}{\text{RTT}_t + 0.5 \times \text{Loss}_t}
]

This formulation promotes efficient data delivery while penalizing delay and packet loss.

---

## Integration Strategy

The interaction between the simulation (C++) and the RL agent (Python) is achieved using PyBind11.

Key characteristics:

* Direct in-process communication (no sockets or file exchange)
* Memory-efficient data transfer without serialization overhead
* Compatible with standard Python machine learning frameworks

The integration operates at the control level, avoiding per-packet overhead and ensuring low-latency interaction suitable for simulation-time decision making.

---

## Relation to Existing Work

Recent work such as LeoCC proposes model-based congestion control mechanisms that explicitly detect network reconfiguration events in LEO satellite environments.

In contrast, this work explores whether reinforcement learning can implicitly learn adaptive behavior from observed network conditions without requiring explicit modeling of reconfiguration events.

---

## Experimental Context

The evaluation is conducted in a simulated LEO satellite environment with:

* Multi-satellite topology
* Dynamic link conditions
* End-to-end communication between ground stations

The simulation parameters are configured to reflect realistic delay variations and dynamic behavior observed in LEO satellite networks.

The RL-based approach is compared against a deterministic baseline (QUIC with BBR congestion control).

---

## Observations

The RL-based controller shows consistent adaptive behavior under dynamic conditions.

* It avoids overly aggressive rate reduction during transient delay increases
* It demonstrates smoother pacing adjustments compared to heuristic-based approaches
* It adapts more effectively during topology transitions such as handovers

The improvements are more pronounced in non-stationary conditions rather than steady-state operation.

---

## Benchmark Perspective

The integration overhead introduced by PyBind11 is minimal compared to the overall simulation cost.

The dominant factors affecting system performance are:

* RL model inference latency
* Simulation time-step resolution
* Network dynamics

This indicates that the chosen integration approach is not a performance bottleneck.

---

## Practical Considerations

* The control loop operates at fixed intervals, not per packet
* The state representation is intentionally compact
* The RL model is designed to maintain low inference latency

These design choices ensure feasibility within simulation constraints.

---

## Limitations

The study is conducted within a simulation environment and does not include real-world deployment validation.

The interaction between C++ and Python follows a synchronous execution model, which may introduce constraints for scaling to more complex systems.

The current evaluation focuses on a single-agent scenario and does not explore distributed or multi-agent learning settings.

These limitations are consistent with the scope of a simulation-based study and provide direction for future work.

---

## Scientific Contribution

This work contributes to the study of adaptive congestion control in LEO satellite networks through:

* A system-level design integrating reinforcement learning with transport protocol simulation
* A PyBind11-based interface enabling efficient interaction between C++ simulation and Python learning models
* An evaluation of learning-based adaptive behavior under dynamic network conditions

The contribution is positioned at the system and methodology level, focusing on integration and adaptive control rather than low-level protocol modification.

---

## Future Work

Potential directions include:

* Extending the state representation with additional network features (e.g., delay variation)
* Evaluating performance in larger-scale satellite constellations
* Exploring asynchronous or distributed RL approaches
* Investigating feasibility in real-world or emulated environments

---

## Repository Structure

```
cpp_interface/    → C++ simulation and integration layer  
python_agent/     → RL model implementation  
docs/             → system documentation  
examples/         → demonstration scripts  
```

---

## Summary

This project demonstrates a practical and structured approach to integrating reinforcement learning with transport protocol simulation. The design enables adaptive congestion control behavior in dynamic satellite environments while maintaining manageable system complexity and experimental flexibility.


