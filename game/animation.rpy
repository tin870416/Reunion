transform from_bottom:
    yalign 2.9        # 一開始在畫面下方（超出螢幕）
    xalign 0.6        # 水平居中
    linear 1.5 yalign 1.5  # 在 1 秒內移動到畫面中間 (yalign=0.5)

init python:
    hpunch = Move((20, 0), (-20, 0), 0.10, bounce=True, repeat=True, delay=0.275)
