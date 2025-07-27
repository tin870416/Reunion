define BOOK_WIDTH = 1540
define BOOK_HEIGHT = 1322
default BOOK_DISPLAY_WIDTH = BOOK_WIDTH * 0.7    # scaled book width (adjust as needed)
default BOOK_DISPLAY_HEIGHT = BOOK_HEIGHT * 0.7   # scaled book height (adjust as needed)
default mouse_pos = (0, 0)
default book_local_pos = (0, 0)
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
        { "rect": (797, 555, 47, 284), "tip": "開塲用末，沖塲用生。", "translation": "開場用末，沖場用生。" },
    ],
    [
        { "rect": (529, 447, 47, 280), "tip": "頁2-區域1", "translation": "開場數語，謂之家門。" },
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

init python:
    def _book_len():
        return len(book_pages)

    def book_next():
        global book_index
        if book_index < _book_len() - 1:
            book_index += 1

    def book_prev():
        global book_index
        if book_index > 0:
            book_index -= 1
init python:
    mouse_pos = (0, 0)
    book_local_pos = (0, 0)

    def _update_mouse_on_book():
        global mouse_pos, book_local_pos
        mouse_pos = renpy.get_mouse_pos()

        # Calculate position relative to book area
        offset_x = (1200 - BOOK_DISPLAY_WIDTH) / 2
        offset_y = (900 - BOOK_DISPLAY_HEIGHT) / 2
        book_local_pos = (
            int(mouse_pos[0] - offset_x),
            int(mouse_pos[1] - offset_y)
        )

screen book_viewer():
    modal True
    zorder 200
    # Update mouse position
    timer 0.05 repeat True action Function(_update_mouse_on_book)
    frame:
        xpos 10
        ypos 10
        background Solid((0, 0, 0, 180))
        padding (5, 5)
        text "Mouse: [mouse_pos[0]], [mouse_pos[1]]\nBook: [book_local_pos[0]], [book_local_pos[1]]" color "#FFFFFF" size 16

    frame:
        xalign 0.5
        yalign 0.5
        background None
        xsize 1300
        ysize 1000
        padding (10, 10)

        vbox:
            spacing 10
            xalign 0.5
            yalign 0.0

            viewport:
                xsize 1200
                ysize 900
                draggable False
                mousewheel True

                fixed:
                    # Draw book image
                    add book_pages[book_index] zoom 0.7 xalign 0.5 yalign 0.5

                    # Get book position and size (centered)
                    $ book_w = BOOK_WIDTH * 0.7
                    $ book_h = BOOK_HEIGHT * 0.7
                    $ book_x = (1200 - book_w) / 2
                    $ book_y = (900 - book_h) / 2

                    # Debug log
                    $ renpy.log(f"Book pos=({book_x},{book_y}), size=({book_w},{book_h})")

                    # Highlights
                    for hl in book_highlights[book_index] if 0 <= book_index < len(book_highlights) else []:
                        $ x, y, w, h = hl["rect"]
                        # Scale highlight relative to book position
                        $ sx = book_x + (x / BOOK_WIDTH) * book_w
                        $ sy = book_y + (y / BOOK_HEIGHT) * book_h
                        $ sw = (w / BOOK_WIDTH) * book_w
                        $ sh = (h / BOOK_HEIGHT) * book_h

                        # Debug log
                        $ renpy.log(f"HIGHLIGHT: {hl['tip']} -> ({sx},{sy}) size=({sw},{sh})")

                        imagebutton:
                            idle Solid((255, 255, 0, 120))
                            hover Solid((255, 255, 0, 180))
                            xpos sx
                            ypos sy
                            xsize sw
                            ysize sh
                            hovered SetVariable("book_tooltip", hl.get("tip", ""))
                            unhovered SetVariable("book_tooltip", "")
                            action SetVariable("book_translation", hl.get("translation", None))

            # Control bar
            hbox:
                spacing 20
                xalign 0.5
                yalign 1.0
                textbutton "上一頁" action Function(book_prev)
                text "[book_index + 1] / [_book_len()]"
                textbutton "下一頁" action Function(book_next)
                null width 150
                textbutton "闔書" action Hide("book_viewer")
        # Tooltip
        if book_tooltip:
            frame:
                background Solid((0, 0, 0, 180))
                xfill True
                padding (10, 10)
                text book_tooltip color "#FFFFFF" size 24

    # Debug: Show mouse coordinates
    frame:
        xpos 10
        ypos 10
        background Solid((0, 0, 0, 180))
        padding (5, 5)
        text "Mouse: [mouse_pos[0]], [mouse_pos[1]]\nBook: [book_local_pos[0]], [book_local_pos[1]]" color "#FFFFFF" size 16

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
            Show("book_viewer")        ]