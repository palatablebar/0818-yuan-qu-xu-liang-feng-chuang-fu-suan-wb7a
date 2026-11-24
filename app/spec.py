COLUMNS = ("minute", "meter", "kw", "window_min", "required")
KINDS = ("meter", "reading", "invoice")
PROJECT = {
    "name": "园区需量峰窗复算",
    "actor": "园区能源数据专员",
    "stages": [
        ("intake", "样例采信"),
        ("prepare", "窗口对齐"),
        ("calculate", "并发峰值"),
        ("policy", "账单复核"),
        ("balance", "运行对账"),
    ],
    "chart": "窗口需量",
}
