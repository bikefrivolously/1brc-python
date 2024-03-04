#!/usr/bin/env python3

import sys


def do_calc(file_name: str) -> list[str]:
    STATIONS = {}
    f = open(file_name, "rt")
    for line in f:
        station, measurement = line.split(";")
        measurement = float(measurement)
        if station not in STATIONS:
            # min, max, sum, count
            STATIONS[station] = [measurement, measurement, measurement, 1]
            continue
        data = STATIONS[station]
        if data[0] > measurement:
            data[0] = measurement
        if data[1] < measurement:
            data[1] = measurement
        data[2] += measurement
        data[3] += 1
    results = []
    for station, summary in sorted(STATIONS.items()):
        results.append(
            f"{station}={summary[0]}/{summary[2] / summary[3]:.1f}/{summary[1]}"  # noqa
        )
    return results


def main():
    MEASUREMENTS_FILE = sys.argv[1]
    results = do_calc(MEASUREMENTS_FILE)
    for line in results:
        print(line)


if __name__ == "__main__":
    main()
