from datetime import datetime
import re

KEY = "TSTFEED0300|7E3E|0400"

def parse_timestamp(line: str) -> datetime | None:
    """
    Ищем timestamp формата HH:MM:SS в строке
    """
    match = re.search(r"\b\d{2}:\d{2}:\d{2}\b", line)
    if match:
        return datetime.strptime(match.group(), "%H:%M:%S")
    return None


def analyze_heartbeat(input_file: str, output_file: str):
    prev_time = None

    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:

        for line in infile:
            if KEY not in line:
                continue

            current_time = parse_timestamp(line)
            if not current_time:
                continue

            if prev_time:
                delta = (current_time - prev_time).total_seconds()

                # если время "перепрыгнуло" через час (например 23:59 → 00:00)
                if delta < 0:
                    delta += 24 * 3600

                if 31 < delta < 33:
                    outfile.write(
                        f"[WARNING] {current_time.time()} - heartbeat {delta} sec\n"
                    )
                elif delta >= 33:
                    outfile.write(
                        f"[ERROR] {current_time.time()} - heartbeat {delta} sec\n"
                    )

            prev_time = current_time


analyze_heartbeat("hblog.txt", "hb_test.log")