import time
import random

def trigger_drift():
    malicious_ips = ["192.168.1.50", "10.0.5.22", "172.16.0.10"]
    target_ip = random.choice(malicious_ips)
    
    entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - CRIT - User: admin - Action: unauthorized_access - IP: {target_ip}\n"
    
    print(f"🔥 [ChaosEngine] Injecting malicious drift: {target_ip}")
    with open("data/mock_logs/auth_logs.txt", "a") as f:
        f.write(entry)
    
    return target_ip

if __name__ == "__main__":
    trigger_drift()