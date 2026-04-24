
# RL-Based QUIC Congestion Control in LEO Satellite Networks

## Overview

This repository presents a system-level study on improving QUIC congestion control using Reinforcement Learning (RL) in Low Earth Orbit (LEO) satellite networks.

The objective of this work is not to redesign QUIC internally, but to introduce a learning-based control mechanism that adapts transmission behavior under highly dynamic network conditions caused by satellite mobility.

The system integrates a discrete-event network simulator (OMNeT++) with a Python-based RL agent using a lightweight PyBind11 interface, enabling closed-loop adaptive control of QUIC pacing.

---

## Key Idea

LEO satellite networks introduce:

- Rapid delay variation (due to satellite movement)
- Frequent handovers (~15 seconds)
- Non-congestion-related packet loss

Traditional congestion control algorithms (Reno, CUBIC, BBR) interpret these effects incorrectly as congestion.

This work proposes:

> A reinforcement learning-based control framework that adjusts QUIC pacing dynamically based on observed network conditions.

---

## System Architecture

The system consists of three main components:

### 1. Simulation Layer (C++ / OMNeT++)

- Implements LEO satellite network using FloRaSat
- Handles QUIC protocol execution
- Extracts network state (RTT, throughput, loss)

📂 Code location: `cpp_interface/`

---

### 2. RL Agent (Python / PyTorch)

- Implements PPO-based reinforcement learning agent
- Observes network state
- Outputs pacing control decisions

📂 Code location: `python_agent/`

---

### 3. Integration Layer (PyBind11)

- Connects C++ simulator with Python agent
- Enables real-time state-action exchange

📂 Code location: `cpp_interface/`

---

## Control Loop

The system operates as a closed-loop controller:

1. OMNeT++ simulation runs QUIC
2. Network state is extracted every 100 ms
3. State is passed to RL agent via PyBind11
4. RL agent outputs action
5. Action modifies QUIC pacing rate

---

## RL Design

### State Representation

The RL agent observes:

- RTT (Round Trip Time)
- Throughput
- Packet Loss

These values are normalized to ensure stable learning.

---

### Action Space

Discrete multiplicative pacing adjustments:

- −20%
- −10%
- 0%
- +10%
- +20%


### Control Equation


pacing_new = pacing_old × (1 + action)


### Reward Function



r = Throughput / (RTT + 0.5 × Loss)


This encourages:

- High throughput
- Low delay
- Low packet loss

---

## Training Configuration

- Episode duration: 60 seconds
- Control interval: 100 ms
- Steps per episode: ~600
- Number of episodes: 50
- Total steps: ~30,000

Training follows an episodic PPO framework.

---

## Dataset Usage

This work uses two real-world datasets to ensure realistic simulation conditions.

### 1. Starlink One-Way Delay Dataset

https://zenodo.org/records/16275284

Used for:

- Extracting realistic delay characteristics
- Understanding uplink/downlink latency behavior
- Modeling time-varying delay patterns

---

### 2. WetLinks Dataset

https://github.com/sys-uos/WetLinks

Used for:

- Calibrating RTT range (~60–80 ms)
- Packet loss (~0.3–0.4%)
- Throughput variability
- Weather-related performance impact

---

### Important Note

The datasets are not directly replayed.

Instead, statistical properties are extracted and used to:

- Configure simulation parameters
- Build realistic network dynamics

---

## Simulation Setup

- 10 satellites
- 20 ground stations
- Satellite altitude: 550 km
- Orbital inclination: 53°
- Routing: DSDV
- Handover interval: ~15 seconds

Traffic:

- Variable bitrate (3 Mbps)
- Continuous and burst workloads

---

## Baseline Comparison

The RL-based QUIC controller is compared against:

- QUIC + Reno
- QUIC + CUBIC
- QUIC + BBR

BBR is identified as the strongest deterministic baseline.

---

## Results Summary

The RL-based approach demonstrates:

- Smoother pacing behavior
- Reduced overreaction to delay spikes
- Faster recovery after handovers
- Better adaptation to non-stationary conditions

---

## Repository Structure

```

cpp_interface/     → QUIC integration + PyBind11 interface
python_agent/      → RL model (PPO implementation)
examples/          → Example usage and test scripts
docs/              → Additional documentation

```

---

## Reproducibility

For reproducibility purposes, the complete code is available in this repository.

### Environment Requirements

#### Simulation

- OMNeT++ 6.x
- INET 4.3 – 4.5
- FloRaSat extension

#### Python

Install dependencies:

```

pip install -r requirements.txt

```

---

## Important Notes

- RL controls only QUIC pacing rate
- Core QUIC mechanisms (ACK, retransmission, cwnd) remain unchanged
- Single-flow scenario is used for controlled evaluation

---

## Scientific Contribution

This work contributes:

- A system-level integration of RL with QUIC
- A practical control-loop design using PyBind11
- An evaluation of learning-based congestion control in LEO environments

The contribution focuses on adaptive behavior rather than protocol redesign.

---

## Limitations

- Simulation-based evaluation
- Single-flow scenario
- No real deployment validation

---

## Future Work

- Multi-flow congestion control
- Real-world deployment
- Distributed RL approaches

---

## Summary

This repository demonstrates a practical and reproducible framework for integrating reinforcement learning into QUIC congestion control under LEO satellite conditions.

The approach highlights how adaptive control can improve performance in highly dynamic network environments.

