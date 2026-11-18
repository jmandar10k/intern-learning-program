def eta_minutes(distance_km: float, courier_load: int = 0, rain: bool = False) -> float:
    """Rule-of-thumb ETA in minutes."""
    if distance_km < 0 or courier_load < 0:
        raise ValueError("distance_km and courier_load must be non-negative")
    return 12.0 + 4.2 * distance_km + 3.0 * courier_load + (6.0 if rain else 0.0)
