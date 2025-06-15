import json
import matplotlib.pyplot as plt
from collections import Counter

def load_alerts(file_path):
    alerts = []
    with open(file_path, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get("event_type") == "alert":
                    alerts.append(data["alert"]["signature"])
            except:
                continue
    return alerts

def visualize_alerts(alerts):
    counter = Counter(alerts)
    top_alerts = counter.most_common(10)
    
    labels, counts = zip(*top_alerts)
    
    plt.figure(figsize=(10, 6))
    plt.barh(labels, counts, color='crimson')
    plt.xlabel("Alert Count")
    plt.title("Top Detected Alerts by Suricata")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = "/var/log/suricata/eve.json"
    alerts = load_alerts(file_path)
    visualize_alerts(alerts)
