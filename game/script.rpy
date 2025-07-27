# 遊戲腳本位於此檔案。
# 宣告該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define yu = Character("李漁")
define you = Character("你")
define narrator = Character(None)
define mo = Character("末")
image bg room = Transform("images/room.png", zoom=1.5)
image bg stage = Transform("stage.png", zoom=1.5)
default preferences.skip_unseen = True

init python:
    # 自訂動作：略過直到下一個 menu
    class SkipToMenu(Action):
        def __call__(self):
            renpy.skip()
            renpy.pause(0.1)

# 遊戲從這裡開始。
label restore_window:
    window show
    return
label start:
    show screen skip_to_next_menu_button
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
            jump act1
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

label act1:
    scene black
    show expression Text("第一齣 / Act One", size=150, color="#e7c96f", xalign=0.5, yalign=0.4) at appear_zoom_fade
    $ renpy.pause(8, hard=True) 
    narrator "即將搬演第一齣。"

label act1_choosedebut:
    narrator "要讓哪個腳色先上場呢？"
    menu:
        "哪個腳色先上場，才合乎李漁所授心法？"
        "生":
            "錯了"
            jump act1_choosedebut
        "旦":
            "錯了"
            return
        "淨":
            "錯了"
            return
        "末":
            jump mo_debut
        "丑":
            "錯了"
            return

label mo_debut:
    scene bg stage
    show mo at Transform(zoom=0.7, xalign=0.5, yalign=0.5)
    narrator ""
    menu:
        "末腳上場，該讓他..."
        "先唱一曲《西江月》":
            jump act1_chosen_qu          
        "先吟一闋《鳳凰臺上憶吹簫》":
            jump act1_chosen_ci

label act1_chosen_qu:
    mo "浪播傳奇八種，賺來一派虛名。閒時自閱自批評，愧殺無鹽對鏡。"
    mo "既辱知音謬賞，敢因醜盡藏形。再為悅己效娉婷，似覺後來差勝。"
    menu:
        "接著該讓他..."
        "吟一闋《鳳凰臺上憶吹簫》":
            mo "姚子無親，興嗟風木，夢中時現層樓。遇鄰居窈窕，許訂鴛儔。硬買途人作父，強認母、似沒來由。誰料取，因癡得福，舊美兼收。"
            mo "凝眸，尋家問室，見夢中樓閣，詫是魂遊。驗諸般信物，件件相投。親父子依然完聚，舊翁婿好事重修。爭榮嗣，又兼報捷，三貴臨頭。"
            $ score_act1(correct_order=True)
            jump act1_jiamen

label act1_chosen_ci:
    mo "姚子無親，興嗟風木，夢中時現層樓。遇鄰居窈窕，許訂鴛儔。硬買途人作父，強認母、似沒來由。誰料取，因癡得福，舊美兼收。"
    mo "凝眸，尋家問室，見夢中樓閣，詫是魂遊。驗諸般信物，件件相投。親父子依然完聚，舊翁婿好事重修。爭榮嗣，又兼報捷，三貴臨頭。"
    menu:
        "接著該讓他..."
        "唱一曲《西江月》":
            mo "浪播傳奇八種，賺來一派虛名。閒時自閱自批評，愧殺無鹽對鏡。"
            mo "既辱知音謬賞，敢因醜盡藏形。再為悅己效娉婷，似覺後來差勝。"
            $ score_act1(correct_order=False)
            jump act1_jiamen
label act1_jiamen:
    mo "恤老婦的偏得嬌妻，姚克承善能致福。"
    mo "防失節的果得全貞，曹小姐才堪免辱。"
    mo "避亂兵的反失愛女，姚東山智也實愚。"
    mo "求假嗣的卻遇真幾，尹小樓斷而忽續。"


label sheng_debut:
label dan_debut:

    return


    # 遊戲結束。

