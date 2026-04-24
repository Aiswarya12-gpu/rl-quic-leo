RL-Based QUIC Congestion Control in LEO Satellite Networks
Overview

This repository contains the implementation and evaluation framework for a reinforcement learning-based congestion control mechanism integrated with QUIC in Low Earth Orbit (LEO) satellite networks.

The objective of this work is not to propose a new transport protocol, but to investigate whether a learning-based control layer can improve QUIC performance under highly dynamic network conditions typical of LEO systems, such as time-varying delay, satellite handovers, and transient packet loss.

The contribution is positioned as a system-level evaluation of RL-based adaptive control applied to QUIC pacing behavior.

System Architecture

The system follows a hybrid architecture composed of three interacting layers:

Simulation Layer (C++ / OMNeT++)

Implements:

QUIC transport protocol execution
Satellite network topology (LEO constellation)
Dynamic link models (delay, loss)
Runtime extraction of network metrics
RL Agent (Python – PPO)

The reinforcement learning agent:

Observes aggregated network state
Learns adaptive control policy
Outputs continuous pacing adjustment

The policy is implemented using a neural network trained with Proximal Policy Optimization (PPO).

Integration Layer (PyBind11)

The interaction between simulation and RL agent is implemented via PyBind11:

In-process communication
No serialization overhead
Low-latency control exchange

This ensures feasibility within simulation time constraints.

Control Mechanism

The system operates as a periodic closed-loop controller:

Control interval: 100 ms
State extracted from QUIC layer:
RTT
Throughput
Packet loss

The RL agent outputs a bounded continuous action:

a
t
	​

∈[−α,α]

which is applied as:

pacing
new
	​

=pacing
old
	​

⋅(1+a
t
	​

)
Important Design Choice

The RL agent controls only the QUIC pacing rate, while:

congestion window (cwnd) → handled by QUIC
retransmissions → handled by QUIC
ACK processing → unchanged

This ensures:

✔ protocol stability
✔ compatibility with QUIC design
✔ safe integration

Reinforcement Learning Setup
State Representation

The state consists of aggregated values over each control interval:

RTT (ms)
Throughput (Mbps)
Packet loss (%)

These values are normalized based on empirically observed bounds to ensure stable training.

Reward Function
r
t
	​

=
RTT
t
	​

+0.5⋅Loss
t
	​

+ϵ
Throughput
t
	​

	​


This formulation encourages:

high throughput
low latency
low packet loss
Training Configuration
Episode duration: 60 seconds
Control interval: 100 ms
Steps per episode: 600
Total episodes: 50
Total interaction steps: ~30,000

Training is performed in an episodic PPO framework, where policy updates occur after each episode.

Real-World Data Integration

The simulation environment is parameterized using real-world measurements:

Datasets used:
Starlink OWD dataset (Garcia et al., 2025)
WetLinks dataset (TMA 2024)
Mapping to Simulation

The datasets are not replayed directly. Instead, they are used to extract statistical characteristics:

RTT baseline: 40–80 ms
RTT spikes: 80–120 ms
Packet loss: 0.5% – 2.5%
Throughput variability patterns

These are incorporated into OMNeT++ / FloRaSat models to emulate:

satellite handovers (delay spikes)
link degradation (loss bursts)
time-varying channel conditions
Simulation Setup

The evaluation is conducted using:

OMNeT++ with FloRaSat extension
LEO satellite topology (multi-node)
Single end-to-end QUIC flow
Dynamic delay and packet loss models
Scenario Characteristics
Satellite mobility → induces delay variation
Handover events → modeled as RTT spikes
Packet loss → time-varying stochastic model
Baseline Comparison

The RL-based approach is compared against:

QUIC with BBR congestion control

Default BBR configuration is used without tuning.

Experimental Observations

The RL-based controller shows:

smoother pacing adjustments under delay variation
reduced RTT spikes during transient events
improved throughput stability
faster recovery after handover events

The improvements are most visible in non-stationary conditions, rather than steady-state operation.

Reproducibility

To ensure reproducibility:

Simulation configuration is provided
RL training setup is documented
Example scripts are included

For reproducibility purposes, the complete code of this work is publicly available:

👉 https://github.com/Aiswarya12-gpu/rl-quic-leo

Repository Structure
cpp_interface/   → QUIC + simulation integration  
python_agent/    → RL model and training logic  
examples/        → execution scenarios  
docs/            → documentation  
Scientific Contribution

This work contributes:

A learning-based control framework integrated with QUIC pacing
A hybrid simulation-learning architecture
A reproducible evaluation under LEO-like dynamics
Empirical analysis of RL vs BBR behavior

The contribution lies in system design and evaluation, not protocol redesign.

Limitations
Simulation-based evaluation
Single-flow scenario
No real deployment
Synchronous RL interaction
Future Work
Multi-flow congestion scenarios
larger LEO constellations
real-world deployment
distributed RL
Summary

This work demonstrates that reinforcement learning can act as an adaptive control layer over QUIC, enabling improved performance under dynamic LEO network conditions while preserving protocol stability.
