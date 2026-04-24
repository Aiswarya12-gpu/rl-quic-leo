#include <pybind11/embed.h>
#include <iostream>

namespace py = pybind11;

class RLAgent {
private:
    py::object model;

public:
    RLAgent() {
        py::initialize_interpreter();

        try {
            py::module infer = py::module::import("infer");
            model = infer.attr("RLInference")();
        } catch (py::error_already_set &e) {
            std::cerr << "Python error: " << e.what() << std::endl;
        }
    }

    double get_action(double rtt, double loss, double throughput) {
        try {
            py::object result = model.attr("predict")(rtt, loss, throughput);
            return result.cast<double>();
        } catch (py::error_already_set &e) {
            std::cerr << "Python error: " << e.what() << std::endl;
            return 0.0;
        }
    }

    ~RLAgent() {
        py::finalize_interpreter();
    }
};
