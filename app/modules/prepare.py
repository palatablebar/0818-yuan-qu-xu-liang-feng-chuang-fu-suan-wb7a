from app.business import DomainIssue, by_kind, prepared, single


def prepare(rows):
    invoice = single(rows, "invoice")
    width = invoice["window_min"]
    meters = {r["meter"] for r in by_kind(rows, "meter")}
    windows = {}
    if not width or len(meters) != invoice["required"] or not meters:
        raise DomainIssue("METER_CONTRACT")
    for r in by_kind(rows, "reading"):
        if r["meter"] not in meters:
            raise DomainIssue("UNKNOWN_METER")
        start = r["minute"] // width * width
        window = windows.setdefault(start, {})
        if r["meter"] in window and window[r["meter"]] != r["kw"]:
            raise DomainIssue("METER_CONFLICT")
        window[r["meter"]] = r["kw"]
    totals = {
        start: sum(value.values())
        for start, value in windows.items()
        if value.keys() == meters
    }
    if not totals:
        raise DomainIssue("NO_COMPLETE_WINDOW")
    return prepared(
        len(totals),
        {"incomplete_windows": len(windows) - len(totals), "window_min": width},
        (totals, invoice["kw"]),
    )
