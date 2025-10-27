# simplistic simulation
import random
def is_anomaly():
    # placeholder logic
    return random.choice([True, False])

if is_anomaly():
    print("::set-output name=anomaly::true")
else:
    print("::set-output name=anomaly::false")
