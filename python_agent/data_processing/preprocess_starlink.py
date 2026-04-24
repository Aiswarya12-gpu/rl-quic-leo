import pandas as pd
import numpy as np
import glob
import json

def process_starlink_data(data_path="data/starlink/"):
    files = glob.glob(data_path + "*.csv")

    delays = []

    for f in files:
        df = pd.read_csv(f)

        if "owd_t0_t1" not in df.columns:
            continue

        d = df["owd_t0_t1"].values / 1e6  # ns → ms

        d = d[d > 0]
        d = d[d < 1000]  # remove extreme outliers

        delays.extend(d)

    delays = np.array(delays)

    stats = {
        "mean_delay": float(np.mean(delays)),
        "std_delay": float(np.std(delays)),
        "p50": float(np.percentile(delays, 50)),
        "p90": float(np.percentile(delays, 90)),
        "p99": float(np.percentile(delays, 99))
    }

    with open("starlink_stats.json", "w") as f:
        json.dump(stats, f, indent=4)

    print("Starlink stats saved")

if __name__ == "__main__":
    process_starlink_data()
