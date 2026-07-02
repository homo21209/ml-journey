import re
import sys
from collections import Counter

def parse_nginx_log(log_path):
    ip_counter = Counter()
    ip_total_time = {}

    pattern = re.compile(r'^(\S+)\s.*\s(\S+)$')

    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                match = pattern.match(line)
                if not match:
                    continue
                ip = match.group(1)
                time_str = match.group(2)
                try:
                    resp_time = float(time_str)
                except ValueError:
                    continue

                ip_counter[ip] += 1
                ip_total_time[ip] = ip_total_time.get(ip, 0.0) + resp_time

    except FileNotFoundError:
        print(f"Файл '{log_path}' не найден.")
        sys.exit(1)

    avg_time = {ip: ip_total_time[ip] / ip_counter[ip] for ip in ip_counter}

    top_ips = ip_counter.most_common(10)

    print(f"{'IP':<20} {'Requests':<10} {'Avg Response Time (s)':<25}")
    print("-" * 55)
    for ip, count in top_ips:
        print(f"{ip:<20} {count:<10} {avg_time[ip]:<25.6f}")
