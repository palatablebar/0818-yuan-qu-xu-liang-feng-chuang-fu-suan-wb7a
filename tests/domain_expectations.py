EXPECTED = {
    "0001": (2, 80, "READY"),
    "0002": (1, 0, "READY"),
    "0003": (0, None, "NO_COMPLETE_WINDOW"),
    "0004": (2, 40, "MISMATCH"),
}
EVIDENCE = {
    "0001": {"peak_start_min": 15, "windows": {0: 60, 15: 80}},
    "0002": {"peak_start_min": 0, "windows": {0: 0}},
}
