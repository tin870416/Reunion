 # variables.rpy（或任何 .rpy）
default current_act = 1          # 目前第幾齣

init python:
    def advance_act(name=None):
        """
        前進到下一齣，可選填段落名稱（例如 家門 / 引子 / 定場白 ……）
        """
        global current_act, current_act_name
        current_act += 1
        if name is not None:
            current_act_name = name
# ui_hud.rpy
screen hud():
    zorder 200
    frame:
        background None
        padding (8, 6)
        xalign 0.95
        yalign 0.05

        vbox:
            spacing 2
            text "第 [current_act] 齣" size 40 color "#fff"
            text "Act [current_act]" size 40 xalign 0.5 color "#fff"
                
