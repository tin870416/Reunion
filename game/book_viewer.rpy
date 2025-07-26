define BOOK_WIDTH = 1540
define BOOK_HEIGHT = 1322

default book_pages = [
    "images/book/p01.png",
    "images/book/p02.png",
    "images/book/p03.png",
    "images/book/p04.png",
    "images/book/p05.png",
    "images/book/p06.png",
    "images/book/p07.png",
]

default book_highlights = [
    [
        { "rect": (830, 554, 37, 223), "tip": "頁1-區域1", "translation": "開場用末，沖場用生。" },
    ],
    [
        { "rect": (912, 301, 32, 220), "tip": "頁2-區域1", "translation": "開場數語，謂之家門。" },
    ],
    [
        { "rect": (912, 301, 32, 220), "tip": "頁3-區域1", "translation": "開場數語，謂之家門。" },
        { "rect": (912, 301, 32, 220), "tip": "頁3-區域2", "translation": "開場數語，謂之家門。" },
    ],
    [
        { "rect": (912, 301, 32, 220), "tip": "頁4-區域1", "translation": "開場數語，謂之家門。" },
    ],
    [
        { "rect": (912, 301, 32, 220), "tip": "頁5-區域1", "translation": "開場數語，謂之家門。" },
    ],
    [
        { "rect": (912, 301, 32, 220), "tip": "頁6-區域1", "translation": "開場數語，謂之家門。" },
        { "rect": (912, 301, 32, 220), "tip": "頁6-區域2", "translation": "開場數語，謂之家門。" },
        { "rect": (912, 301, 32, 220), "tip": "頁6-區域3", "translation": "開場數語，謂之家門。" },
        { "rect": (912, 301, 32, 220), "tip": "頁6-區域4", "translation": "開場數語，謂之家門。" },
    ],
    [
        { "rect": (912, 301, 32, 220), "tip": "頁7-區域1", "translation": "開場數語，謂之家門。" },
    ],
]

default book_index = 0
default book_tooltip = ""
default book_translation = None
default persistent.book_last_index = 0
default book_zoom = 1.0
default book_debug = False
default debug_box = [100, 100, 150, 80]

init python:
    def book_zoom_in(step=0.1, max_zoom=3.0):
        global book_zoom
        book_zoom = min(max_zoom, book_zoom + step)
        renpy.restart_interaction()

    def book_zoom_out(step=0.1, min_zoom=0.4):
        global book_zoom
        book_zoom = max(min_zoom, book_zoom - step)
        renpy.restart_interaction()

    def book_reset_zoom():
        global book_zoom
        book_zoom = 1.0
        renpy.restart_interaction()

    def _book_len():
        return len(book_pages)

    def book_next():
        global book_index
        if book_index < _book_len() - 1:
            book_index += 1
        renpy.restart_interaction()

    def book_prev():
        global book_index
        if book_index > 0:
            book_index -= 1
        renpy.restart_interaction()

    def toggle_debug():
        global book_debug
        book_debug = not book_debug
        renpy.restart_interaction()

    def print_debug_box():
        x, y, w, h = debug_box
        renpy.notify(f"座標: ({x}, {y}, {w}, {h})")
        renpy.log(f"DEBUG BOX: x={x}, y={y}, w={w}, h={h}")

    def update_debug_box():
        if not book_debug:
            return
        mx, my = renpy.get_mouse_pos()
        viewport_x, viewport_y = 50, 50
        offset_x = (1200 - BOOK_WIDTH * 0.5 * book_zoom) / 2
        offset_y = (700 - BOOK_HEIGHT * 0.5 * book_zoom) / 2
        book_x = (mx - viewport_x - offset_x) / (0.5 * book_zoom)
        book_y = (my - viewport_y - offset_y) / (0.5 * book_zoom)
        global debug_box
        if 0 <= book_x <= BOOK_WIDTH and 0 <= book_y <= BOOK_HEIGHT:
            debug_box[0] = int(book_x)
            debug_box[1] = int(book_y)

screen book_viewer():
    modal True
    zorder 200

    key "K_ESCAPE" action [
        Hide("book_viewer"),
        SetField(persistent, "book_last_index", book_index),
        SetVariable("book_tooltip", ""),
        SetVariable("book_translation", None)
    ]
    key "K_RIGHT" action Function(book_next)
    key "K_LEFT" action Function(book_prev)

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1300
        ysize 850
        padding (20, 20)

        vbox:
            spacing 10
            xalign 0.5

            viewport:
                xsize 1200
                ysize 700
                draggable False
                mousewheel True

                fixed:
                    xalign 0.5
                    yalign 0.5

                    # 書頁圖片
                    add book_pages[book_index] zoom (0.5 * book_zoom) xalign 0.5 yalign 0.5

                    # Debug 區域
                    if book_debug:
                        python:
                            x, y, w, h = debug_box
                            offset_x = (1200 - BOOK_WIDTH * 0.5 * book_zoom) / 2
                            offset_y = (700 - BOOK_HEIGHT * 0.5 * book_zoom) / 2
                            scaled_x = x * 0.5 * book_zoom + offset_x
                            scaled_y = y * 0.5 * book_zoom + offset_y
                            scaled_w = w * 0.5 * book_zoom
                            scaled_h = h * 0.5 * book_zoom
                            renpy.log(f"Rendering debug box: rect=({x}, {y}, {w}, {h}), pos=({scaled_x}, {scaled_y}), size=({scaled_w}, {scaled_h})")

                        imagebutton:
                            idle Solid((0, 255, 0, 255))
                            hover Solid((100, 255, 100, 255))
                            xpos scaled_x
                            ypos scaled_y
                            xsize scaled_w
                            ysize scaled_h
                            action Function(print_debug_box)

                    # 高光區域
                    python:
                        page_hls = book_highlights[book_index] if 0 <= book_index < len(book_highlights) else []

                    for hl in page_hls:
                        python:
                            x, y, w, h = hl["rect"]
                            offset_x = (1200 - BOOK_WIDTH * 0.5 * book_zoom) / 2
                            offset_y = (700 - BOOK_HEIGHT * 0.5 * book_zoom) / 2
                            scaled_x = x * 0.5 * book_zoom + offset_x
                            scaled_y = y * 0.5 * book_zoom + offset_y
                            scaled_w = w * 0.5 * book_zoom
                            scaled_h = h * 0.5 * book_zoom
                            renpy.log(f"Rendering highlight: page={book_index}, rect=({x}, {y}, {w}, {h}), pos=({scaled_x}, {scaled_y}), size=({scaled_w}, {scaled_h})")

                        imagebutton:
                            idle Solid((255, 255, 0, 255))
                            hover Solid((255, 255, 100, 255))
                            xpos scaled_x
                            ypos scaled_y
                            xsize scaled_w
                            ysize scaled_h
                            hovered [SetVariable("book_tooltip", hl.get("tip", "")),
                                     SetVariable("book_translation", hl.get("translation", None))]
                            unhovered [SetVariable("book_tooltip", ""),
                                       SetVariable("book_translation", None)]
                            action NullAction()

            # 控制列
            hbox:
                spacing 10
                xalign 0.5
                textbutton "上一頁" action Function(book_prev)
                text "[book_index + 1] / [_book_len()]"
                textbutton "下一頁" action Function(book_next)

                null width 30
                textbutton "－" action Function(book_zoom_out)
                text "縮放: [round(book_zoom, 2)]x"
                textbutton "＋" action Function(book_zoom_in)
                textbutton "重置" action Function(book_reset_zoom)

                null width 30
                textbutton "關閉" action [
                    Hide("book_viewer"),
                    SetField(persistent, "book_last_index", book_index),
                    SetVariable("book_tooltip", ""),
                    SetVariable("book_translation", None)
                ]
                textbutton "Debug座標 ({})".format("On" if book_debug else "Off") action Function(toggle_debug)

        # 提示文字
        if book_tooltip:
            frame:
                background Solid((0, 0, 0, 180))
                xfill True
                padding (10, 10)
                text book_tooltip color "#FFFFFF" size 24

        if book_debug:
            timer 0.1 repeat True action Function(update_debug_box)
            python:
                mx, my = debug_box[0], debug_box[1]
            frame:
                xpos 10
                ypos 10
                background Solid((0, 0, 0, 180))
                padding (10, 10)
                text "Mouse: ({}, {})".format(mx, my) color "#FFFFFF" size 20

    if book_translation:
        use book_translation_popup(book_translation)

screen book_translation_popup(text):
    frame:
        xalign 0.5
        yalign 0.95
        xsize 600
        ysize 150
        background Solid((20, 20, 20, 230))
        vbox:
            spacing 20
            text text color "#FFFFFF" size 24 xalign 0.5 yalign 0.5
            textbutton "關閉" xalign 0.5 action SetVariable("book_translation", None)

screen book_icon():
    zorder 100
    imagebutton:
        idle Transform("images/book_icon.png", zoom=0.15)
        hover Transform("images/book_icon_hover.png", zoom=0.15)
        xpos 30
        ypos 80
        action [
            SetVariable("book_index", persistent.book_last_index),
            Show("book_viewer")
        ]