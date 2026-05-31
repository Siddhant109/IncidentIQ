from prometheus_client import Counter

incident_counter = Counter(
    "incident_total",
    "Total incidents detected"
)

service_failure_counter = Counter(
    "service_failure_total",
    "Total service failures"
)