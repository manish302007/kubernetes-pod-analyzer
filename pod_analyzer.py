import time
import random

def loading(text, delay=0.6):
    print(text)
    time.sleep(delay)

def analyze_pod(pod):
    print("\n===== POD ANALYSIS REPORT =====\n")
    time.sleep(0.5)

    print(f"Pod Name        : {pod['name']}")
    print(f"Namespace       : {pod['namespace']}")
    print(f"Status          : {pod['status']}")
    print(f"Restart Count   : {pod['restarts']}")
    print(f"CPU Usage       : {pod['cpu']}")
    print(f"Memory Usage    : {pod['memory']}")

    print("\n--- AI Analysis (Simulated Mistral LLM) ---\n")
    time.sleep(0.5)

    if pod["status"] == "CrashLoopBackOff":
        print("Issue Detected  : Application is repeatedly crashing.")
        print("Root Cause      : Possible misconfiguration or insufficient memory.")
        print("Recommendation  : Check container logs and increase memory limits.")
    elif pod["status"] == "Running":
        print("Status          : Pod is healthy and running normally.")
        print("Recommendation  : Continue monitoring resource usage.")
    else:
        print("Status          : Unknown state. Further inspection required.")

    print("\n===== ANALYSIS COMPLETE =====")

# Simulated pod data
pod_data = {
    "name": "payment-service",
    "namespace": "production",
    "status": "CrashLoopBackOff",
    "restarts": random.randint(3, 7),
    "cpu": "87%",
    "memory": "512Mi / 512Mi"
}

loading("Fetching pod details from Kubernetes cluster...")
loading("Connecting to cluster API server...")
loading("Analyzing pod with Mistral LLM...\n")

analyze_pod(pod_data)

