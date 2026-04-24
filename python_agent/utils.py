def normalize_state(rtt, loss, throughput):
    rtt_norm = rtt / 200.0
    loss_norm = loss / 1.0
    throughput_norm = throughput / 300.0

    return [rtt_norm, loss_norm, throughput_norm]


def compute_reward(rtt, loss, throughput):
    return throughput / (rtt + 0.5 * loss + 1e-6)
