#map icon
screen map_icon():
    zorder 100
    imagebutton:
        idle Transform("images/mapicon.png", zoom=0.08)
        hover Transform("images/mapicon.png", zoom=0.11)
        xalign 0.95
        yalign 0.9
        action Show("world_map", is_inline=True)


#map
init python:
    style.close_button = Style(style.default)
    style.close_button.xalign = 0.83
    style.close_button.yalign = 0.12
    style.close_button.padding = (10,10)
    style.close_button.background = Frame("#052953db", 2, 2)
    style.close_button.hover_background = Frame("#1f242e9f", 2, 2)
    style.close_button_text.size = 30
    style.close_button_text.font = "font/BigCaslon.ttf"

    # 正確設定字體顏色：text部分的樣式需獨立設定
    style.close_button_text.color = "#ffffff"
default hovered_location = None
screen world_map(is_inline=False):
    modal True
    fixed:
        frame:
            xalign 0.5
            yalign 0.5
            xsize 1300
            ysize 720

            viewport:
                xsize 1300
                ysize 720
                draggable True
                mousewheel True         # ✅ 建議保留，支援滾輪
                scrollbars "horizontal"


                fixed:
                    xsize int(2500 * 0.9)  # 地圖縮放後實際寬度
                    ysize int(800 * 0.9)

                    add Transform("images/gamemap.png", zoom=0.9)

                    imagebutton:
                        idle "chuanshu.png"
                        hover Transform("chuanshu.png", alpha=0.7)
                        at Transform(zoom=0.5)
                        xpos int(150 * 0.9)
                        ypos int(500 * 0.9)
                        action NullAction()
                        hovered [SetVariable("hovered_location", "川蜀")]
                        unhovered [SetVariable("hovered_location", None)]

                    imagebutton:
                        idle "xiantao.png"
                        hover Transform("xiantao.png", alpha=0.7)
                        at Transform(zoom=0.5)
                        xpos int(950 * 0.9)
                        ypos int(480 * 0.9)
                        action NullAction()
                        hovered [SetVariable("hovered_location", "仙桃鎮/Xiantao Village")]
                        unhovered [SetVariable("hovered_location", None)]

                    imagebutton:
                        idle "hanyang.png"
                        hover Transform("hanyang.png", alpha=0.7)
                        at Transform(zoom=0.5)
                        xpos int(1100 * 0.9)
                        ypos int(300 * 0.9)
                        action NullAction()
                        hovered [SetVariable("hovered_location", "漢陽/Hanyang")]
                        unhovered [SetVariable("hovered_location", None)]
                    
                    imagebutton:
                        idle "yunyang.png"
                        hover Transform("yunyang.png", alpha=0.7)
                        at Transform(zoom=0.5)
                        xpos int(1350 * 0.9)
                        ypos int(270 * 0.9)
                        action NullAction()
                        hovered [SetVariable("hovered_location", "鄖陽/Yunyang")]
                        unhovered [SetVariable("hovered_location", None)]
                        

                    imagebutton:
                        idle "songjiang.png"
                        hover Transform("songjiang.png", alpha=0.7)
                        at Transform(zoom=0.5)
                        xpos int(2150 * 0.9)
                        ypos int(250 * 0.9)
                        action NullAction()
                        hovered [SetVariable("hovered_location", "松江")]
                        unhovered [SetVariable("hovered_location", None)]

            if hovered_location is not None:
                $ chars_here = [char for char, loc in character_positions.items() if loc == hovered_location]

                frame:
                    xalign 0.5
                    yalign 0.05
                    xpadding 25
                    ypadding 20
                    background "#900000ff"

                    vbox:
                        spacing 1
                        xalign 0.5

                        if chars_here:
                            # 中文名列成一行
                            $ chinese_str = "、".join(chars_here)

                            # 從中文名找對應英文名（預設 fallback 回原名）
                            $ english_list = [character_engnames.get(char, char) for char in chars_here]
                            $ english_str = ", ".join(english_list)
                            $ verb = "is" if len(english_list) == 1 else "are"

                            text "[chinese_str] 在這裡。" size 15 xalign 0.5 color "#ffffff"
                            text "[english_str] [verb] here." size 15 xalign 0.5 color "#ffffff" 
                        else:
                            text "目前無要角在此地。No major characters here." size 15 xalign 0.5 color "#ffffff"
    if is_inline:
        textbutton "Close":
            style "close_button"
            action Hide("world_map")
    else:
        textbutton "Close":
            style "close_button"
            action Return()

            
