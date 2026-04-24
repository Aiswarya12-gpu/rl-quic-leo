# RL-Based QUIC Congestion Control in LEO Satellite Networks

## Overview

This repository presents a system-level study on improving QUIC congestion control using reinforcement learning (RL) in Low Earth Orbit (LEO) satellite networks.

Rather than modifying QUIC internals, this work introduces a learning-based control mechanism that dynamically adjusts the QUIC pacing rate in response to time-varying network conditions caused by satellite mobility.

The system integrates a C++-based discrete-event simulator (OMNeT++) with a Python-based RL agent using PyBind11, enabling real-time adaptive control.

---

## Key Idea

LEO satellite networks exhibit:

- Time-varying delay (RTT fluctuations)
- Frequent handovers (~15 seconds)
- Mobility-induced packet loss (not congestion)

Traditional congestion control algorithms misinterpret these effects as congestion.

This work proposes:

> A reinforcement learning-based control framework that adapts QUIC pacing based on observed network conditions.

---

## System Architecture

The system consists of three components:

### 1. Simulation Layer (C++ / OMNeT++)
- LEO satellite network modeled using FloRaSat
- QUIC protocol execution
- State extraction (RTT, throughput, packet loss)

`cpp_interface/`

---

### 2. RL Agent (Python / PyTorch)
- PPO-based reinforcement learning agent
- Maps network state → control action

`python_agent/`

---

### 3. Integration Layer (PyBind11)
- Efficient C++ ↔ Python communication
- Low overhead, in-process execution

 `cpp_interface/`

---

## Control Loop

At each control interval (100 ms):

1. Simulator extracts network state  
2. State is passed to RL agent  
3. RL agent outputs action  
4. Action adjusts QUIC pacing rate  

---

## RL Design

### State

- RTT  
- Throughput  
- Packet Loss  

State values are normalized based on empirical bounds.

---

### Action Space

Discrete multiplicative adjustments:

- −20%
- −10%
- 0%
- +10%
- +20%

---

### Control Equation

pacing_new = pacing_old × (1 + action)

---

### Reward Function

r = Throughput / (RTT + 0.5 × Loss)

This balances efficiency and stability.

---

## Training Configuration

- Episode duration: 60 seconds  
- Control interval: 100 ms  
- Steps per episode: ~600  
- Episodes: 50  
- Total steps: ~30,000  

Training is performed offline using an episodic PPO framework.  
The trained policy is later deployed during simulation.

---

## Dataset Usage

This work uses real-world Starlink measurements to ensure realistic behavior.

### 1. Starlink One-Way Delay Dataset
https://zenodo.org/records/16275284  

Used for:
- Delay distribution modeling  
- Uplink / downlink latency characteristics  

---

### 2. WetLinks Dataset
https://github.com/sys-uos/WetLinks  

Used for:
- RTT calibration (~60–80 ms)  
- Packet loss (~0.3–0.4%)  
- Throughput variability  
- Weather-induced performance variation  

---

### Important Note

Datasets are not replayed directly.  
Instead, statistical properties are extracted and used to configure simulation parameters.

---

## Simulation Setup

- 10 satellites  
- 20 ground stations  
- Altitude: 550 km  
- Inclination: 53°  
- Routing: DSDV  
- Handover interval: ~15 seconds  

Traffic:

- Variable bitrate (3 Mbps)  
- Continuous and burst workloads  

Experiments are conducted in a **single-flow scenario** to isolate congestion control behavior.

---

## Baseline Comparison

The RL-based controller is compared against:

- QUIC + Reno  
- QUIC + CUBIC  
- QUIC + BBR  

BBR serves as the strongest deterministic baseline.

---

## Results Summary

The RL-based controller demonstrates:

- Smoother pacing behavior  
- Reduced overreaction to delay spikes  
- Faster recovery after handovers  
- Improved adaptation to non-stationary conditions  

---

## Repository Structure

cpp_interface/     → QUIC integration + PyBind11 interface  
python_agent/      → RL training and inference  
examples/          → usage examples  
docs/              → documentation  

---

## How to Run (Reproducibility)

### 1. Simulation Environment

Install:

- OMNeT++ 6.x  
- INET 4.3–4.5  
- FloRaSat  

---

### 2. Python Environment

pip install -r requirements.txt

---

### 3. Training

Run RL training:

python python_agent/train.py

---

### 4. Simulation Execution

- Build OMNeT++ project  
- Enable RL interface  
- Run simulation  

---

## Scientific Contribution

This work contributes:

- A learning-based congestion control framework for QUIC  
- A PyBind11-based integration between simulation and RL  
- A system-level evaluation under realistic LEO conditions  

The contribution focuses on adaptive behavior rather than protocol redesign.

---

## Limitations

- Simulation-based evaluation  
- Single-flow scenario  
- No real deployment  

---

## Future Work

- Multi-flow scenarios  
- Real-world deployment  
- Distributed RL  

---

## Summary

This repository provides a reproducible framework for integrating reinforcement learning with QUIC congestion control in LEO satellite networks.

It demonstrates how adaptive control improves performance under dynamic conditions.
