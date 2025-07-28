# 遊戲腳本位於此檔案。
# 宣告該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define yu = Character("李漁")
define you = Character("你")
define narrator = Character(None)
define mo = Character("末")
define sh = Character("【生】姚繼")
define old = Character("鄰翁")
define dan = Character("曹小姐")
define yaofu = Character("姚器汝")
image bg room = Transform("images/room.png", zoom=1.5)
image bg stage = Transform("stage.png", zoom=1.5)
image bg childroom = Transform("childroom.png", zoom=1.25)
image chest = "chest.png"
image chest_inner = "chest_inner.png"
image bg garden = Transform("garden.png", zoom=1.25)
image bg childroom_blur = im.Blur(im.FactorScale("images/childroom.png", 1.25), 4.0)
image hand = "hand.png"

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
    yu "你這就替老夫將《生我樓》寫成戲文，何如？"
    you "老先生想是錯認，晚生實在不通..."
    yu "噫，閣下不會是不曾讀過拙作？那也不妨事！閣下解得演習格局之妙，才是重中之重，怕怎地？"
    yu "這小說改作戲文，該改換頭面，不妨暫擬新題，喚作《巧團圓》。"
    yu "成八卦者十六將也，分十六將者三十二候也。這戲就分上下兩部各十六齣，加上開場，共三十三齣，脩短合度，是個好數字！"
    yu "恰好老夫近來刊有一稿，備載演習之精要。汝可少閱，閱畢即請起草。"

label after_skip:
    scene bg room    # 或 scene black
    hide li yu
    show screen book_icon
    $ book_debug = True
    narrator "你可以點擊笠翁新刊書籍，看看他有何指教。"
    narrator "笠翁已將書本奉送給你，你可以隨時翻閱。"
    $ end_of_act("笠翁")

label commit_writing:
    menu:
        "你現在要..."
        "開始寫作":
            narrator "好的，這就為你研墨。"
            scene black with fade
            jump choose_first_actor
        "再讀一會兒書，能拖則拖":
            show screen book_viewer
            jump commit_writing

label open_book:
    show screen book_viewe
    $ ui.interact()  # 等待玩家操作書本
    return


label choose_first_actor:
    narrator "即將搬演第一齣。"
    narrator "要讓哪個腳色先上場呢？"
    menu:
        "哪個腳色先上場，才合乎李漁所授心法？"
        "生":
            $ score_debut(choosemo=False)
            jump sheng_debut
        "旦":
            $ score_debut(choosemo=False)
            jump dan_debut
        "外":
            $ score_debut(choosemo=False)
            jump wai_debut
        "末":
            $ score_debut(choosemo=True)
            jump mo_debut


label mo_debut:
    $ show_act_title_auto()
    show screen actnumber
    $ show_actnumber = True
    scene bg stage
    show mo at Transform(zoom=0.7, xalign=0.5, yalign=0.5)
    pause 1.5
    if any(x in act_history for x in ["夢訊", "議贅", "爭繼"]):
        $ renpy.notify("李漁：此時才讓末腳登場，奇哉怪哉！")
    narrator ""
    menu:
        "末腳上場，該讓他..."
        "先唱一曲《西江月》，為作者立言":
            jump mo_chosen_qu          
        "先吟一闋《鳳凰臺上憶吹簫》，稟明全劇大意":
            jump mo_chosen_ci

label mo_chosen_qu:
    hide mo
    show mo_sing_solemn at Transform(zoom=0.7, xalign=0.5, yalign=0.5)
    with dissolve
    mo "{i}浪播傳奇八種，賺來一派虛名。閒時自閱自批評，愧殺無鹽對鏡。{/i}"
    mo "{i}既辱知音謬賞，敢因醜盡藏形。再為悅己效娉婷，似覺後來差勝。{/i}"
    menu:
        "接著該讓他..."
        "吟一闋《鳳凰臺上憶吹簫》，稟明全劇大意":
            hide mo_sing_solemn
            show mo_speak_solemn at Transform(zoom=0.7, xalign=0.5, yalign=0.5)
            with dissolve
            mo "姚子無親，興嗟風木，夢中時現層樓。遇鄰居窈窕，許訂鴛儔。硬買途人作父，強認母、似沒來由。誰料取，因癡得福，舊美兼收。"
            mo "凝眸，尋家問室，見夢中樓閣，詫是魂遊。驗諸般信物，件件相投。親父子依然完聚，舊翁婿好事重修。爭榮嗣，又兼報捷，三貴臨頭。"
            $ score_mo(correct_order=True)
            ""
            jump mo_jiamen

label mo_chosen_ci:
    hide mo
    show mo_speak_solemn at Transform(zoom=0.7, xalign=0.5, yalign=0.5)
    with dissolve
    mo "姚子無親，興嗟風木，夢中時現層樓。遇鄰居窈窕，許訂鴛儔。硬買途人作父，強認母、似沒來由。誰料取，因癡得福，舊美兼收。"
    mo "凝眸，尋家問室，見夢中樓閣，詫是魂遊。驗諸般信物，件件相投。親父子依然完聚，舊翁婿好事重修。爭榮嗣，又兼報捷，三貴臨頭。"
    menu:
        "接著該讓他..."
        "唱一曲《西江月》，為作者立言":
            hide mo_speak_solemn
            show mo_sing_solemn at Transform(zoom=0.7, xalign=0.5, yalign=0.5) 
            with dissolve
            mo "{i}浪播傳奇八種，賺來一派虛名。閒時自閱自批評，愧殺無鹽對鏡。{/i}"
            mo "{i}既辱知音謬賞，敢因醜盡藏形。再為悅己效娉婷，似覺後來差勝。{/i}"
            $ score_mo(correct_order=False)
            ""
            jump mo_jiamen

label mo_jiamen:
    ""
    hide mo_speak_solemn
    hide mo_sing_solemn
    show mo at Transform(zoom=0.7, xalign=0.5, yalign=0.5)
    with dissolve
    narrator ""
    mo "恤老婦的偏得嬌妻，姚克承善能致福。"
    mo "防失節的果得全貞，曹小姐才堪免辱。"
    mo "避亂兵的反失愛女，姚東山智也實愚。"
    mo "求假嗣的卻遇真幾，尹小樓斷而忽續。"
    ""
    narrator "末腳報完家門，觀眾已經大致掌握劇情了。"
    narrator "他們非常期待！"
    hide mo
    narrator "接下來，請決定下一齣要讓哪個腳色上場。"
    menu:
        "下一齣的主角是..."
        "生" if "夢訊" not in act_history:
            "生腳這就換裝，準備登場。"
            scene black with fade
            jump sheng_debut
            $ end_of_act("開場")
        "旦" if "議贅" not in act_history:
            "旦腳這就換裝，準備登場。"
            scene black with fade
            jump dan_debut
            $ end_of_act("開場")
        "外" if "爭繼" not in act_history:
            "外腳這就換裝，準備登場。"
            scene black with fade
            jump wai_debut
            $ end_of_act("開場")

label sheng_debut:
    scene black
    $ show_act_title_auto()
    show sheng_2_pensive at Transform(zoom=0.7, xalign=0.5, yalign=0.5) 
    with dissolve
    ""
    sh "{i}飽殺侏儒。嘆饑時曼倩，望米如珠。長貧知有意，天欲盡其膚。{/i}"
    sh "{i}除故我，換新吾，才許建雄圖。看士人，改軀換貌，盡賴詩書。{/i}"
    ""
    sh "小生姚繼，字克承，楚之漢陽人也。"
    sh "幼失二親，長無一恃，孑孑孤行於世上，亭亭獨立於人前。"
    sh "唉，普天下的人，誰家不事父母，那個沒有爺娘？獨是小生不然，自幼喪了二親，記不起當時的面貌。"
    sh "我時常思想要在夢中會一會，好記了面貌，到醒來圖畫真容。"
    sh "怎奈夜夜睡去，再不能勾相逢，只夢見一座小樓..."
    sh "裡面鋪下床帳，又有一個小小枕頭，卻像是我睡過的一樣。夜夜做夢都是如此。"
    sh "此時夜色將闌，正好到夢中樓上去走一走..."
    scene black
    scene bg garden with fade
    show sheng_2_contemplate at Transform(zoom=0.7, xalign=0.8, yalign=0.5) 
    with dissolve
    ""
    sh "柳媚花明止筆耕，倏然隨步出柴荊。腳跟頗與輕車似，偏向從前熟路行。"
    sh "前面一座小樓，是我熟遊之地，不知不覺又來到這邊，不免再去登眺一番，有何不可。"
    scene bg childroom_blur with fade
    show sheng_2_contemplate at Transform(zoom=0.7, xalign=0.8, yalign=0.5)
    ""
    sh "這房子裡面雖則無人，還喜得有鄰有舍。那壁廂坐著一位老者，待我問他。"
    show oldman at Transform(xalign=0.2, yalign=0.5, xzoom=-1) 
    with dissolve 
    ""
    sh "那位老人家請了！"
    sh "小生不知進退，敢借問一聲，這座小樓是誰家的住宅？為甚麽不關不鎖，終日空在這邊？"
    old "你這小孩子又來作怪了，自己生身的所在，竟不知道，反來問我。"
    sh "我生身的所在，另有一處，何嘗在這里。老人家不要取笑，請對我直講。"
    old "誰與你取笑？若還不信，那床帳後面現有一箱，里面所藏之物，都是你做孩子的時節，終日戲耍的東西，取出來看就是了。"
    hide oldman 
    hide sheng_2_contemplate 
    with dissolve
    show chest with Fade(0.5, 0, 0.5) 
    ""
    sh "果然有一箱，喜得不曾封鎖。待我取出物件，細細看來。"
    menu:
        "開箱":
            show hand at from_bottom
            ""
            jump open_chest

label open_chest:   
    hide chest
    hide hand
    pause 0.5
    show chest_inner with dissolve
    pause 0.5
    ""
    sh "呀！{i}既然重進老萊居，何妨再演斑斕具。{/i}"
    sh "看看這裡頭，有泥人、土馬、棒槌、鑼鼓、刀槍、旗幟...都是小兒玩物。"
    ""
    sh "...且住，記得我爹爹是個布客，常以販標為生。臨終的時節，把一根玉尺交與我道，萬一你讀書不成，還做本行生意。"
    sh "這等看來，那一根玉尺是我傳家之寶，為甚麽倒不在裡面？"
    hide chest_inner with dissolve
    show oldman at Transform(xalign=0.2, yalign=0.5, xzoom=-1) 
    show sheng_2_contemplate at Transform (xalign=0.8, yalign=0.5, zoom=0.7) 
    with dissolve
    old "那是後來得的，並非爺娘所賜，你記錯了。"
    old "只是一件，玉尺雖不是爹娘所賜，卻關係你的婚姻，也不可拿來丟棄。"
    old "牢記此言。我如今再不講了。"
    scene black with dissolve
    pause 1.5
    show sheng_2_contemplate at Transform (xalign=0.5, yalign=0.5, zoom=0.7) with Fade (1.0, 0.5, 2.5)
    ""
    sh "呀！原来又是一夢！"
    sh "他說玉尺非爺娘所賜，乃是後來得的。我只有這位爹娘，怎麽說個不是？"
    sh "他又道，玉尺一根，雖不是爺娘所賜，卻關係我的婚姻。"
    sh "我這東鄰有一女子，貌頗傾城，他屢屢顧盼小生，只是瓜李之嫌，不可不避。"
    sh "且自由他，我且把玉尺收好，看到後來有何應驗。"
    scene black
    $ character_positions["sheng"] = "漢陽"
    pause 1.0
    $ renpy.notify(f"角色位置：{character_positions}")
    $ end_of_act("夢訊")
    menu:
        "接下來要讓哪個腳色上場？"
        "末" if "開場" not in act_history:
            jump mo_debut
        "旦" if "議贅" not in act_history:
            jump dan_debut
        "外" if "爭繼" not in act_history:
            jump wai_debut
    
    
label dan_debut:
    scene black
    $ show_act_title_auto()
    show dan_smile at Transform(zoom=0.7, xalign=0.5, yalign=0.5) 
    ""
    yaofu "市城戎馬地，決策早居鄉。妻子無多口，琴書只一囊。"
    yaofu "老夫姚器汝，號東山，蜀川人也。"
label wai_debut:

    return


    # 遊戲結束。

