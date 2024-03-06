#!/usr/bin/env python3

import multiprocessing as mp
import os
import os.path
import sys
from functools import partial

NUM_THREADS = 12


def find_chunk_positions(
    file_name: str, num_chunks: int, delim: str = "\n"
) -> list[tuple[int, int]]:
    chunk_positions = []
    file_size = os.path.getsize(file_name)
    chunk_size = file_size // num_chunks
    f = open(file_name, "rb")
    print(f"size: {file_size}, chunk_size: {chunk_size}")
    chunk_start = 0
    for chunk_num in range(num_chunks):
        chunk_end = min(chunk_start + chunk_size, file_size - 1)
        f.seek(chunk_end)
        while f.read(1) != b"\n":
            chunk_end += 1
        chunk_positions.append((chunk_start, chunk_end))
        chunk_start = chunk_end + 1

    f.close()
    return chunk_positions


def process_chunk(file_name: str, start_pos: int, stop_pos: int):
    print(start_pos, stop_pos)
    STATIONS = {}
    f = open(file_name, "rb")
    f.seek(start_pos)
    while start_pos < stop_pos:
        line = f.readline()
        # print(line, len(line))
        start_pos += len(line)
        station, measurement = line.decode().split(";")
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
    return STATIONS


def do_calc(file_name: str) -> list[str]:
    STATIONS = {}
    chunk_positions = find_chunk_positions(file_name, NUM_THREADS)

    with mp.Pool(NUM_THREADS) as p:
        f = partial(process_chunk, file_name)
        chunk_results = p.starmap(f, chunk_positions)

    for chunk_result in chunk_results:
        for station, summary in chunk_result.items():
            if station not in STATIONS:
                STATIONS[station] = summary
                continue
            data = STATIONS[station]
            data[0] = min(data[0], summary[0])
            data[1] = max(data[1], summary[1])
            data[2] += summary[2]
            data[3] += summary[3]

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
