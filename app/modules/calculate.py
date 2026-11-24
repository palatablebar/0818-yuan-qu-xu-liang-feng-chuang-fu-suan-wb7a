from app.business import measured


def compute(data):
    totals, target = data
    time = max(totals, key=lambda k: (totals[k], -k))
    return measured(
        totals[time], target, "千瓦", {"peak_start_min": time, "windows": totals}
    )
