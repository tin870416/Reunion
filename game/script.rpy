# 遊戲腳本位於此檔案。
# 宣告該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define yu = Character("李漁")
define you = Character("你")
define narrator = Character(None)
define mo = Character("末")
image bg room = Transform("images/room.png", zoom=1.5)
screen skip_button():
    textbutton "跳過" action Jump("after_skip") xpos 0.9 ypos 0.05
init -1:
    python:
        config.has_music = False
        config.has_sound = False
        config.has_voice = False
    define config.side_image_tag = None

# 遊戲從這裡開始。
label restore_window:
    window show
    return
label start:
    show screen skip_button
    # 顯示背景。 預設情況下，它使用佔位符，但您可以
    # 將檔案（名為 "bg room.png" 或 "bg room.jpg"）新增至
    # images 目錄來顯示它。

    scene bg room

    # 這顯示了一個角色精靈。 使用了佔位符，但您可以
    # 透過將名為 "eileen happy.png" 的檔案
    # 新增至 images 目錄來取代它。

    show li yu at Transform(zoom=0.7, xalign=0.5, yalign=0.5)

    # 這些顯示對話行。

    yu "傳奇原為消愁設，費盡杖頭歌一曲。"
    yu "唯我填詞不賣愁，一夫不笑是吾憂。"
    yu "老夫李漁，賤號笠翁，專候閣下已久了！"
    you "晚生久仰尊名了！"
    yu "當今填詞者眾，貴戚通侯亦單重聲音，只惜時無顧曲周郎。最有識見之客，亦作矮人觀場。可怪！可怪！"
    yu "閣下可知，老夫今日何事相請？"
    you "晚生不知。"
    yu "聽說閣下能寫戲，且深得老夫三昧。這卻難得。"
    you "什麼？在下對填詞作戲一竅不通，哪..."
    yu "頃有《生我樓》一篇小說，正有意編為傳奇，今日傳汝，便欲試試閣下手法。"
    you "老先生想是錯認..."
    yu "你這就替老夫將《生我樓》寫成戲文，何如？"
    you "晚生實在不通..."
    yu "噫，閣下不會是不曾讀過拙作？那也不妨事！閣下解得演習格局之妙，才是重中之重，怕怎地？"
    you "先生且慢..."
    yu "老夫近刊有一稿，備載演習之精要。汝可少閱，閱畢即請起草。"

label after_skip:
    scene bg room    # 或 scene black
    hide li yu
    show screen book_icon
    $ book_debug = True
    narrator "你可以點擊笠翁新刊書籍，看看他有何指教。"
    narrator "笠翁已將書本奉送給你，你可以隨時翻閱。"

label commit_writing:
    menu:
        "你現在要..."
        "開始寫作":
            narrator "好的，這就為你研墨。"
            jump drama_start
        "再讀一會兒書，能拖則拖":
            show screen book_viewer
            jump commit_writing

label open_book:
    show screen book_viewer
    $ ui.interact()  # 等待玩家操作書本
    return

# 動畫定義（顯示字出現、放大、淡出）
transform appear_zoom_fade:
    alpha 0.0
    zoom 0.5
    linear 4 alpha 1.0 zoom 1.0  # 淡入+放大
    pause 1                      # 停留
    linear 1 alpha 0.0           # 淡出
    on hide: 
        alpha 0.0             # 確保 hide 時立即隱藏

label drama_start:
    scene black
    show expression Text("第一齣 / Act One", size=150, color="#e7c96f", xalign=0.5, yalign=0.4) at appear_zoom_fade
    $ renpy.pause(8, hard=True) 
    narrator "即將搬演第一齣。"
    narrator "要讓哪個腳色先上場呢？"
    menu:
        "哪個腳色先上場，才合乎李漁所授心法？"
        "生":
            "錯了"
        "旦":
            "錯了"
        "淨":
            "錯了"
            return
        "末":
            jump mo_debut
        "丑":
            "錯了"
            return

label mo_debut:
    mo "i'm singing"
label sheng_debut:
label dan_debut:

    return


    # 遊戲結束。

