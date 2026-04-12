# RL-Based QUIC Congestion Control in LEO Satellite Networks

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
  Enables interaction between the simulation and the RL agent through a lightweight C++–Python interface.

---

## Interaction Workflow

At each control interval during simulation:

1. The simulator extracts network state parameters:

   * Round-trip time (RTT)
   * Packet loss
   * Throughput

2. The state is passed to the RL agent

3. The RL agent computes an action:

   * Multiplicative pacing rate adjustment

4. The action is applied to the QUIC congestion control mechanism

This forms a closed-loop adaptive control system.

---

## Motivation

Traditional congestion control algorithms (e.g., BBR) rely on fixed heuristics and may struggle to adapt to highly dynamic environments such as LEO satellite networks.

Frequent handovers and fluctuating delays require adaptive mechanisms capable of learning from network behavior. Reinforcement learning provides a framework for such adaptive decision-making.

---

## Technical Approach

* Reinforcement Learning Algorithm: Proximal Policy Optimization (PPO)

* State Representation:

  * RTT
  * Packet loss
  * Throughput

* Action:

  * Continuous pacing rate adjustment (multiplicative factor)

* Reward Function:

[
r_t = \frac{\text{Throughput}_t}{\text{RTT}_t + 0.5 \times \text{Loss}_t}
]

This formulation promotes efficient data delivery while penalizing delay and packet loss.

---

## Integration Strategy

The interaction between the simulation (C++) and the RL agent (Python) is achieved using a direct binding mechanism.

Key characteristics:

* In-process communication (no sockets or file exchange)
* Lightweight interface
* Compatible with standard Python ML frameworks

The integration is designed at the control level, avoiding per-packet overhead.

---

## Experimental Context

The evaluation is conducted in a simulated LEO satellite environment with:

* Multi-satellite topology
* Dynamic link conditions
* End-to-end communication between ground stations

The RL-based approach is compared against a deterministic baseline (QUIC with BBR congestion control).

---

## Observations

The RL-based controller demonstrates:

* Improved responsiveness to dynamic network changes
* More stable pacing behavior under varying delay conditions
* Faster adaptation during topology transitions (e.g., handovers)

The improvements are particularly noticeable under non-stationary network conditions.

---

## Benchmark Perspective

The integration layer is implemented using a lightweight binding approach, which minimizes additional overhead compared to traditional alternatives.

The overall system performance is primarily influenced by:

* RL model inference time
* Simulation dynamics

rather than the binding mechanism itself.

---

## Practical Considerations

* The control loop operates at fixed intervals, not per packet
* The state representation is intentionally compact
* The RL model is designed to maintain low inference latency

These design choices ensure feasibility within simulation constraints.

---

## Limitations

* The evaluation is limited to a simulation environment
* Real-world deployment constraints are not considered
* Python execution introduces sequential processing constraints
* Scalability for large-scale multi-agent systems is not explored

---

## Scientific Contribution

This work contributes to:

* Exploring reinforcement learning for QUIC congestion control
* Designing a simulation-level integration between protocol logic and learning models
* Evaluating adaptive behavior in LEO satellite network conditions

The contribution lies in the system-level design and evaluation rather than low-level implementation of transport protocols.

---

## Future Work

Potential directions include:

* Extending the state representation with additional network metrics
* Evaluating performance in larger-scale satellite constellations
* Exploring asynchronous or distributed RL approaches
* Investigating real-world deployment feasibility

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

This project demonstrates a practical approach to integrating reinforcement learning with transport protocol simulation. The design enables adaptive congestion control behavior in dynamic satellite environments while maintaining a manageable system complexity.
