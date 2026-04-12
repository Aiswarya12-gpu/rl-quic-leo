#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

// Function to simulate sending network state to RL agent
std::vector<double> get_network_state() {
// Example state: RTT, throughput, loss
return {50.0, 200.0, 0.01};
}

// Function to apply RL action (pacing rate adjustment)
void apply_action(double factor) {
// In real simulation, this modifies QUIC pacing rate
// Here we just print for demonstration
std::cout << "Applying pacing factor: " << factor << std::endl;
}

// Binding module
PYBIND11_MODULE(quic_rl, m) {
m.def("get_state", &get_network_state);
m.def("apply_action", &apply_action);
}
