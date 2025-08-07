# 遊戲腳本位於此檔案。
# 宣告該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define yu = Character("李漁")
define you = Character("你")
define narrator = Character(None)
define mo = Character("末")
define sh = Character("姚繼")
define old = Character("鄰翁")
define dan = Character("曹儷人")
define yaofu = Character("姚器汝")
define yaocao = Character("曹玉宇（姚器汝）")
define yaowife = Character("曹夫人（姚夫人）")
define wai = Character("尹小樓")
define waiwife = Character("尹夫人")
define fneigh = Character("表姐丈")
define rneigh = Character("伊大哥")
define fnr = Character("表姐丈、伊大哥")
define tiger = Character("一隻虎")
define wolf = Character ("獨行狼")
define scorpion = Character ("蠍子塊")
define star = Character ("過天星")
define chuang = Character ("李自成")
define soldiers = Character ("眾將")
image bg room = Transform("images/room.png", zoom=1.5)
image bg gate = Transform("images/gate.png", zoom=1.3)
image bg yaoroom = Transform("images/yaoroom.png", zoom=1.5)
image bg yinroom = Transform("images/yinroom.png", zoom=1.5)
image bg stage = Transform("stage.png", zoom=1.5)
image bg childroom = Transform("childroom.png", zoom=1.25)
image chest = "chest.png"
image chest_inner = "chest_inner.png"
image bg garden = Transform("garden.png", zoom=1.25)
image bg fight = Transform("fight.png", zoom=1.25)
image bg childroom_blur = im.Blur(im.FactorScale("images/childroom.png", 1.25), 4.0)
image hand = "hand.png"
image bg_fight_shake = "fight.png"
image bg yaostudy = Transform("yaostudy.png", zoom=1.25)
image bg shengreading = Transform ("sheng_reading3.png", zoom=1.25)
image bg boudoir = Transform ("boudoir.png", zoom=1.25)
image bg military = Transform ("military.png", zoom=1.25)
image bg cottage = Transform ("cottage.png", zoom=1.25)
image bg door_open = Transform ("dooropen.png", zoom=1.5, xalign=1, yalign=1)
image bg dan_out = Transform ("dooropen_dan.png", zoom=1.25)
image bg dan_out_2 = Transform ("dooropen_dan_2.png", zoom=1.25)

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
    $ start_new_run()
    jump date
    return
    show screen skip_to_next_menu_button
    scene bg room with fade
    play music "audio/softbgm.mp3" fadein 3.0
    pause 4.0
    show li yu at Transform(zoom=0.7, xalign=0.5, yalign=0.5)
    with dissolve
    ""
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
    narrator "你可以點擊笠翁新刊書籍，看看他有何指教。"
    narrator "笠翁已將書本奉送給你，你可以隨時翻閱。"
    show screen map_icon
    narrator "笠翁另贈一卷地圖，方便你隨時確認劇中何人位在何地。"
    $ end_of_act("笠翁")

label commit_writing:
    menu:
        "你現在要..."
        "開始寫作":
            narrator "好的，這就為你研墨。"
            scene black with fade
            stop music fadeout 1.0
            jump choose_first_actor
        "再讀一會兒書，能拖則拖":
            show screen book_viewer
            jump commit_writing
        "取地圖來展卷遨遊，能拖則拖":
            call screen world_map
            jump commit_writing
label open_map:
    show screen world_map
    $ ui.interact()  # 等待玩家操作書本
    return

label open_book:
    show screen book_viewer
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
    #if any(x in act_history for x in ["夢訊", "議贅", "爭繼"]):
    if store.act_no > 1:
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
    $ end_of_act("開場")
    menu:
        "下一齣的主角是..."
        "生（姚繼）" if "夢訊" not in act_history:
            "生腳這就換裝，準備登場。"
            scene black with fade
            jump sheng_debut
            
        "旦（曹儷人）及其家人" if "議贅" not in act_history:
            "旦腳這就換裝，準備登場。"
            scene black with fade
            jump dan_debut
            
        "外（尹小樓）及其妻子" if "爭繼" not in act_history:
            "外腳這就換裝，準備登場。"
            scene black with fade
            jump wai_debut
            
label sheng_debut:
    scene black
    $ show_act_title_auto()
    show sheng_2_pensive at Transform(zoom=0.7, xalign=0.5, yalign=0.5) 
    with dissolve
    pause 1.5
    if store.act_no == 2 and "開場" in store.act_history:
        $ renpy.notify("沖場用生，一本戲文之好歹，即於此時定價。")
    ""
    $ character_positions["姚繼"] = "漢陽/Hanyang"
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
    pause 1.0
    if store.act_no == 1:
        $ renpy.notify("可以點開地圖，看看姚繼現在在哪裡！")
        $ renpy.notify("遊戲過程可以隨時檢查人物地點，確保他們在離散之後終能走上團圓之路。")
    elif store.act_no ==2 and "開場" in store.act_history:
        $ renpy.notify("可以點開地圖，看看姚繼現在在哪裡！")
        $ renpy.notify("遊戲過程可以隨時檢查人物地點，確保他們在離散之後終能走上團圓之路。")
    $ end_of_act("夢訊")
    menu:
        "接下來要讓哪個腳色上場？"
        "末" if "開場" not in act_history:
            jump mo_debut
        "旦（曹儷人）及其家人" if "議贅" not in act_history:
            jump dan_debut
        "外（尹小樓）及其妻子" if "爭繼" not in act_history:
            jump wai_debut
        "讓曹玉宇來找姚繼，看看他有何話說" if "議贅" in act_history:
            jump try_sheng
    
    
label dan_debut:
    scene black
    $ show_act_title_auto()
    pause 1.5
    scene bg yaoroom
    show yaofu at Transform(zoom=0.7, xalign=0.5, yalign=0.2) 
    if store.act_no == 2 and "開場" in store.act_history:
        $ renpy.notify("李漁：沖場竟不用生，似乎不是詞場常格。")
    ""
    $ character_positions["曹儷人"] = "漢陽/Hanyang"
    $ character_positions["曹玉宇（姚器汝）"] = "漢陽/Hanyang"
    $ character_positions["曹夫人（姚夫人）"] = "漢陽/Hanyang"
    yaofu "市城戎馬地，決策早居鄉。妻子無多口，琴書只一囊。"
    ""
    yaofu "老夫姚器汝，號東山，蜀川人也。"
    yaofu "本有兩榜科名，一朝事業，因見時事日非，朝綱盡亂，所以請告回四川老家，已經數載。"
    yaofu "誰知近日又有那闖逆揭竿，賊氛四起。"
    yaofu "老夫做了二十年仕宦，萬一遇見賊徒，豈能幸免？"
    yaofu "所以背鄉離井，寄跡他方。"
    yaofu "如今來在漢口地方，扮做個懸壺的醫士，賣藥糊口。"
    yaofu "又怕人看出行徑來，改了一個極俗的姓名，喚做曹玉宇。"
    yaocao "唉，雖然曾經官臻八座，位至三台，不幸亡兒夭折，繼嗣無人。"
    yaocao "至親家眷只有夫人、女兒兩口。連這女兒也不是親生，乃同年至戚之女，名喚曹玉瑤。"
    yaocao "我這養女兒呀，年已及笄，尚未許嫁。"
    yaocao "我盤算著，只待招贅一人，就立為嗣子。如此一來，不只女兒有託，也免了我無嗣之憂。"
    yaocao "且待夫人出來，與他商議則個。"
    hide yaofu
    show yaofu at Transform(zoom=0.7, xalign=0.9, yalign=0.2) 
    show yaowife_worried_norm at Transform(zoom=1.1, xalign=0.5, yalign=0.3)
    with dissolve
    ""
    yaowife "老相公，我和你飄零異鄉，身旁沒有親人，止得這個養女。"
    show dan_scared at Transform(zoom=0.86, xalign=0.005, yalign=0.99)
    with dissolve
    yaowife "當初指望兒子長大，配成一對夫妻，不想兒子夭亡，這句說話講不起了。"
    yaowife "如今年已長成，還不曾替他議婚，萬一闖賊殺來，叫他跟著誰人逃走？"
    yaowife "難道我老夫妻兩口，自己照管不來，還帶著個如花似玉的閨女，去招災惹禍不成？"
    yaowife "且莫說他的姻事，就是我們兩口的終身，也全無著落。當初兒子未亡，不想立嗣，如今靠著何人？"
    yaowife "還不想急急回家，立個螟蛉之子。"
    ""
    yaofu "夫人，你的說話句句是金石之言，老夫豈不知道？"
    yaofu "所以遲疑未決者，只為要把兩樁事情合成一件。"
    ""
    yaowife "我知道了。你說這個女孩子，原在可兒可媳之間，要招個男子在身旁，就接我們的宗祀麽？"
    yaofu "便是這等說。"
    hide yaowife_worried_norm
    show yaowife_worried_norm at Transform(zoom=1.1, xalign=0.5, yalign=0.3, xzoom=-1)
    yaowife "我兒，你的意思何如？"
    menu:
        yaowife "我兒，你的意思何如？"
        "久蒙恩養，不啻親生，正要常依膝下。":
            jump dan_choose_stay
        "若是箇好人才，豈願紆尊入贅？女兒覺得不是擇人之法。":
            jump dan_choose_refuse
    label dan_choose_refuse:
    dan "若是箇好人才，豈願紆尊入贅？女兒覺得不是擇人之法。"
    yaofu "你這孩子，意思是甘教我曹家絕嗣了？"
    dan "不是這個意思。"
    hide yaowife_worried_norm
    show yaowife_worried_norm at Transform(zoom=1.1, xalign=0.5, yalign=0.3)
    jump candidate_yao
    label dan_choose_stay:
    dan "久蒙恩養，不啻親生，正要常依膝下。"
    hide yaowife_worried_norm
    show yaowife_worried_norm at Transform(zoom=1.1, xalign=0.5, yalign=0.3)
    yaowife "若還如此，這段婚姻就草草不得了。"
    label candidate_yao:
    yaowife "我們仕宦人家，女婿還可以將就，兒子卻將就不得。"
    yaowife "你做過三品高官，論理該有恩蔭，萬一大亂之後，忽然平靜起來，回到家中，就是他去補官授職了。"
    yaowife "亂離之世，如何選得出這個人來？"
    yaofu "夫人休得癡想，「太平」二字是不能再見的了。"
    yaofu "只要尋個少年老成之人，做了避亂的幫手，到那賊寇近身的時節，可以見景生情，逃得性命出去，救得家小回來，就是個佳兒佳婿了。"
    yaofu "我眼睛裡面，已相中一個。"
    yaofu "此人雖非宗裔，卻恰巧與我同姓，又正好少室無家。"
    yaowife "端的是誰，你且講來我聽。"
    yaofu "他的房舍與我的寓所，只隔得一層籬笆。你去想來便了。"
    yaowife "莫非是姚小官麽？果然好個孩子。"
    yaowife "只是一件，有人在背後談論他，說不是姚家的真種，三四歲的時節，去幾兩銀子買下來的。"
    yaofu "只要孩子肯學好，那些閒話聽他怎的。"
    ""
    dan "奴家也曾見過，是好一副面龐。"
    yaofu "說便這等說，也還要留心試他。"
    yaofu "這等世界，倒不喜他會讀書，只要老成練達，做得事來就可以相許。"
    yaofu "我明日見他，自有話說。"
    scene black
    pause 1.0
    if store.act_no == 1:
        $ renpy.notify("可以點開地圖，看看曹家人現在在哪裡！")
        $ renpy.notify("遊戲過程可以隨時檢查人物地點，確保他們在離散之後終能走上團圓之路。")
    elif store.act_no ==2 and "開場" in store.act_history:
        $ renpy.notify("可以點開地圖，看看曹家人現在在哪裡！")
        $ renpy.notify("遊戲過程可以隨時檢查人物地點，確保他們在離散之後終能走上團圓之路。")
    $ end_of_act("議贅")
    menu:
        "接下來要讓哪個腳色上場？"
        "末" if "開場" not in act_history:
            jump mo_debut
        "生（姚繼）" if "夢訊" not in act_history:
            jump sheng_debut
        "外（尹小樓）及其妻子" if "爭繼" not in act_history:
            jump wai_debut
        "讓曹玉宇去找姚繼，看他有何話說" if "夢訊" in act_history:
            jump try_sheng

    
label wai_debut:
    scene black
    $ show_act_title_auto()
    scene bg yinroom
    with dissolve
    pause 1.5
    if store.act_no == 2 and "開場" in store.act_history:
        $ renpy.notify("李漁：沖場竟不用生，似乎不是詞場常格。")
    show yin_fullsize at Transform(zoom=1.2, xalign=0.7, yalign=0.005)
    ""
    $ character_positions["尹小樓"] = "鄖陽/Yunyang"
    $ character_positions["尹夫人"] = "鄖陽/Yunyang"
    wai "{i}天道無知，如聾似瞽，善人後嗣全無。鷙同梟鳥，偏自擁多雛。{/i}"
    ""
    wai "老夫姓尹名厚，別號小樓，湖廣鄖陽人也。"
    wai "祖上以防邊靖難之功，世授錦衣衛千戶，老夫襲職多年，告假還鄉，又經數載。"
    wai "我家屢世單傳，傳到老夫也止生一子，不想於十五年前，隨了一隊孩童上山去玩耍，及至晚上回來，別人的兒子都在，單少我家這條命根。"
    wai "彼時正有虎災，尋覓多時，不見蹤影，定是落於虎口無疑了！"
    wai "所以至今無後，竟把世職空懸。有許多親戚朋友勸我立嗣，我只是不依。"
    show yinwife_fullsize at Transform(zoom=1, xalign=0.2, yalign=0.005)
    with dissolve
    ""
    waiwife "聞得有幾個親朋，不由你我情願，都要攜酒備席，把兒子送上門來勸你承繼，你還是收他不收他？"
    wai "一概不收！"
    waiwife "為什麼不收？"
    wai "你道他勉強要來承繼，果然是一片好心麽？不過要得我的家產，襲我的官職罷了！"
    waiwife "這等，你的意思待怎麼樣？"
    wai "我想立後承先，不是一樁小事，況且平空白地把萬金家產付他，又賠上一個恩蔭，豈是輕易出手的？"
    wai "必須揀個有才有幹，承受得起的人，又要在平日間試他，先有些情意到我，然後許他承繼。"
    wai "這樣的嗣子，後來才不忤逆。夫人，你道我講得是麽？"
    waiwife "是便極是。還有一種世情，你不曾慮到。"
    waiwife "你要試人，不知你便有心，他也未必無意。"
    wai "夫人，你這話是什麼意思？"
    waiwife "他人知道你我無兒，必想一人繼立，故意把虛情哄你，也未見得。"
    wai "夫人也慮得是。我想近處之人，哪個不知道我家的事，要試真情也試他不出。"
    wai "除非丟了故鄉，到別處去交接，才試得出這個人來。"
    wai "我不久就要遠行，夫人在家可耐心等候。"
    hide yinwife_fullsize
    show yin_fullsize at Transform(zoom=1, xalign=0.6, yalign=0.005, xzoom=-1)
    pause 1.0
    ""
    show teenager at Transform(zoom=0.65, xalign=0.05, yalign=1.0) 
    with moveinleft
    show fat_neighbor at Transform(zoom=0.6, xalign=0.25, yalign=1.0)
    with moveinleft
    ""
    fneigh "{i}攜樽酒，過親廬，好把兒相贈，效勤劬。接得他家嗣，便高門戶，這家財不怕不歸吾。{/i}"
    fneigh "{i}從今不穿布，從今不穿布。{/i}"
    ""
    wai "呀，表姊丈來了。許久不見，為甚麽攜著酒盒，又帶了外甥過來？"
    fneigh "此來不為別事，只因老舅沒有公郎，應該是外甥承繼，故此選了吉日，把小兒送上門來，做你現現成成的兒子，你不可不受。"
    wai "承宗立嗣，非同小可，豈有不曾說明，就要承繼之理？且再商量。"
    ""
    show neighbor_red at Transform(zoom=0.7, xalign=0.85, yalign=1.0) 
    show kid at Transform(zoom=0.5, xalign=0.95, yalign=1.0)
    with moveinright
    hide yin_fullsize
    show yin_fullsize at Transform(zoom=1, xalign=0.6, yalign=0.005)
    ""
    rneigh "{i}除家累，逐頑雛，送到鄰家去，作兒呼。坐享榮和貴，不愁親父，到他年不享這歡娛。{/i}"
    rneigh "{i}從今不開舖，從今不開舖。{/i}"
    ""
    wai "呀，這是鄰家的伊大哥。為甚麽也攜了酒盒，也帶著令郎過來？"
    rneigh "此來不為別事，只因老長兄沒有公郎，應該是小兒承繼。故此攜了酒盒，把小兒送上門來，做你嫡嫡親親的兒子，你不可不受。"
    hide fat_neighbor
    show fat_neighbor_mad at Transform(zoom=0.6, xalign=0.25, yalign=1.0)
    fneigh "得！老伊，你好生沒理。外甥繼舅，乃是事理之常，你是何人，也想要來承繼？"
    fneigh "方才說應該是你，這「應該」兩個字，你且講來我聽。"
    rneigh "同宗立嗣，古之常理。我與他是同宗，所以說「應該」二字。"
    fneigh "又來奇了，你姓伊，他姓尹，怎麽叫做同宗？"
    rneigh "尹字比伊字，只少得一個立人。如今把我家的人，移到他家去，他就可以姓伊，我就可以姓尹了。怎麽不是同姓。"
    fneigh "好胡說！"
    fneigh "{i}我笑你學問疏，機謀富，巧支吾，難回護。{/i}"
    fneigh "{i}不分貴賤高低，妄思綿祚。只怕烏紗飛不上頭顱，止堪服役，賣作傭奴。{/i}"
    hide neighbor_red
    show neighbor_red_mad at Transform(zoom=0.7, xalign=0.85, yalign=1.0)
    hide kid with moveoutright
    hide teenager
    hide yin_fullsize 
    with moveoutleft
    rneigh "老丈不要太毒。我聞得你這姐夫郎舅，也不十分嫡親，不過是表而已矣！"
    rneigh "若說表姐丈的兒子定該立嗣，連表子生下的娃娃，也該來承繼了。"
    hide fat_neighbor_mad
    show fat_neighbor_fight at Transform(zoom=0.6, xalign=0.25, yalign=1.0)
    fneigh "好放肆的狗才！叫管家兒子過來，一齊動手，打死這個老賊！"
    hide neighbor_red_mad
    show neighbor_red_fight at Transform(zoom=0.7, xalign=0.85, yalign=1.0)
    rneigh "你有兒子，我也有兒子，你有管家，我也有管家，一個對一個，料想不輸與你。"
    scene bg fight with hpunch
    scene bg fight with hpunch
    scene bg fight with hpunch
    scene bg fight with hpunch

    wai "呀，這兩個人怎麽打起來了？"
    show yin_back at Transform(zoom=1, xalign=0.5, yalign=0.005)
    with dissolve
    wai "二位快不要如此。小弟這一份家私，自有個應得之人走來承受，不是爭奪得去的。"
    ""
    hide yin_back
    scene bg yinroom with dissolve
    show teenager_scared at Transform(zoom=0.65, xalign=0.01, yalign=1.0) 
    with dissolve
    show fat_neighbor_fight at Transform(zoom=0.6, xalign=0.25, yalign=1.0)
    with moveinleft
    fneigh "孩兒過來，拜見你的繼父。"
    show kid_scared at Transform(zoom=0.5, xalign=0.99, yalign=1.0)
    with dissolve
    show neighbor_red_fight at Transform(zoom=0.7, xalign=0.85, yalign=1.0)
    with moveinright
    rneigh "我兒過去，叩見你的親爺。"
    show yin_block_full at Transform(zoom=0.8, xalign=0.5, yalign=0.005)

    wai "尊拜也不敢領，尊呼也不敢當。若還要拜，我只得避進去了。"
    hide neighbor_red_fight
    hide fat_neighbor_fight
    hide yin_block_full
    show neighbor_red_mad at Transform(zoom=0.7, xalign=0.85, yalign=1.0) 
    show fat_neighbor_mad at Transform(zoom=0.6, xalign=0.25, yalign=1.0)
    show yin_block_full at Transform(zoom=0.8, xalign=0.5, yalign=0.005)
    fnr "既然如此，我們只得告別了。"
    scene black
    scene bg gate
    show fat_neighbor_mad at Transform(zoom=0.6, xalign=0.25, yalign=1.0)
    show neighbor_red_mad at Transform(zoom=0.7, xalign=0.85, yalign=1.0)
    show teenager_scared at Transform(zoom=0.65, xalign=0.01, yalign=1.0) 
    show kid_scared at Transform(zoom=0.5, xalign=0.99, yalign=1.0)
    fneigh "{i}且穿粗布暫遮風，紬運如今尚未通。{/i}"
    hide fat_neighbor_mad
    hide teenager_scared
    with moveoutleft
    rneigh "{i}依舊回家開鋪面，命低莫想做封翁。{/i}"
    hide neighbor_red_mad
    hide kid_scared
    with moveoutright
    show yin_headache at Transform(zoom=0.8, xalign=0.5, yalign=1.0)
    ""
    wai "看了這番舉動，我那出門求子的事，一發緩不得了。"
    wai "明日就打點登程，且到途中再商議尋人之法便了。"
    scene black
    pause 1.0
    if store.act_no == 1:
        $ renpy.notify("可以點開地圖，看看尹家人現在在哪裡！")
        $ renpy.notify("遊戲過程可以隨時檢查人物地點，確保他們在離散之後終能走上團圓之路。")
    elif store.act_no ==2 and "開場" in store.act_history:
        $ renpy.notify("可以點開地圖，看看尹家人現在在哪裡！")
        $ renpy.notify("遊戲過程可以隨時檢查人物地點，確保他們在離散之後終能走上團圓之路。")
    $ end_of_act("爭繼")

    ""
    ""
    if store.act_no ==5:
        jump dating
    else:
        menu:
            "接下來要讓哪個腳色上場？" 
            "末" if "開場" not in act_history:
                jump mo_debut
            "生（姚繼）" if "夢訊" not in act_history:
                jump sheng_debut
            "旦（曹儷人）及其家人" if "議贅" not in act_history:
                jump dan_debut
            "讓曹玉宇去找姚繼，看看他有何話說" if "議贅" in act_history:
                jump try_sheng


label try_sheng:
    scene black
    $ show_act_title_auto()
    scene bg yaostudy
    show sheng_pensive_full at Transform(zoom=1, xalign=0.7, yalign=0.1)
    ""
    sh "小生自得夢訊以來，心事愈加煩悶。好幾日不看書了，不免展開一卷，吟誦片時。"
    hide sheng_pensive_full
    scene bg shengreading
    ""
    sh "{i}我意兒中撇不下的愁緒，好像這卷兒中析不出的疑義。{/i}"
    sh "{i}我欲待不思親權刪抹了孝思，怎奈這《蓼莪》篇欲廢則是難輕廢。{/i}"
    sh "可惜遇著亂世，我這求名的念頭不十分急切，若在太平之世，把這等文字去求取功名，我姚克承何愁不富，何愁不貴？"
    ""
    scene bg yaostudy with dissolve
    show yaofu_full at Transform(zoom=1, xalign=0.2, yalign=0.001) 
    with dissolve
    yaofu "{i}立後事輕微，也待把諸艱歷試。欲待要覘他動靜，不妨私啟柴扉。{/i}"
    show sheng_greet_full at Transform(zoom=1.1, xalign=0.8, yalign=0.01)
    with dissolve
    sh "呀，曹老伯過來了，有失趨迎，得罪，得罪！"
    yaofu "姚小官，你終日靜坐，不見出門，在家做些甚麽？"
    sh "不是讀書，就是作文，此外並無一事。"
    hide sheng_greet_full
    show sheng_nolaugh_full at Transform(zoom=1.1, xalign=0.8, yalign=0.01)
    yaofu "好沒正經，這等亂離之世，身家性命也難保，還去讀甚麽書？作甚麽文？你也迂闊極了。"
    sh "照老伯這等講來，當今的天下是不能平靜的了？"
    yaofu "萬萬不能。"
    sh "既然如此，讀書何用？只是一件，我們做秀才的人，除了讀書沒有別樣事做，卻怎麽好？"
    yaofu "當此之時，只有三等人好做：第一等是術士，第二等是匠工，第三等是商賈。"
    sh "怎見得這三等人好做？"
    yaofu "處此亂世，遇了賊兵，保得性命就勾了，一應田產家私都不能攜帶。"
    yaofu "那術士、匠工，把技藝當了家私，藏在腹中，隨處可以覓食，所以算做上中二等。"
    yaofu "為商作賈的人，平日做慣貿易，走過江湖。"
    yaofu "把山川形勢、人情土俗，都看在眼里，知道某處可以避兵，某路可以逃難。"
    yaofu "到那危急之際，就好挈帶妻子前行，若留得幾兩本錢，還可以營生度活。"
    yaofu "這雖是最下一等，卻人人可做，又不失體面。"
    yaofu "我且問你，你曾學得些術數技藝麽？"
    sh "據小侄看來，老伯所說的下等，倒是小侄的上著，只可惜沒有本錢，說不起為商作賈的話。"
    yaofu "只怕有了本錢，你也未必會做。"
    sh "拚得吃些辛苦，有什麼做不來？"
    sh "不瞞老伯講，先君在日原以販布為生，慣走松江一路，還有許多賬目放在各莊，不曾收起，都有票約可憑。"
    sh "若借得幾兩盤纏，去走一次回來，定不落空，只可惜沒有這個債主。"
    hide yaofu_full at Transform(zoom=1, xalign=0.2, yalign=0.001) 
    show yaofu_full at Transform(zoom=1, xalign=0.2, yalign=0.001, xzoom=-1) 
    yaofu "我正要試他，不如就從這樁事起。"
    hide yaofu_full
    show yaofu_full at Transform(zoom=1, xalign=0.2, yalign=0.001) 
    yaofu "盤費不難，出在老夫身上。"
    yaofu "我還有幾兩本錢，煩你順帶前去，捎些布匹回來。若還不負所托，將來還有所商。"
    hide sheng_nolaugh_full
    show sheng_greet_full at Transform(zoom=1.1, xalign=0.8, yalign=0.01)
    sh "若得如此，感恩不盡。明日就送券約過來。"
    yaofu "那倒不消。只是早早回家，不使老夫盼望，就是盛情了。"
    

label handkerchief:
    scene black
    $ show_act_title_auto()
    scene bg boudoir
    with dissolve
    pause 1.5
    show dan_foldarms at Transform(zoom=0.9, xalign=0.5, yalign=0.999) 
    ""
    dan "奴家幼失父母，寄養於姚氏之門，蒙他愛若親生，又許我贅夫承繼，這是極遂心的事了。"
    dan "怎奈爹爹過於詳慎，定要把艱難困苦之事，試過幾樁，才與他完姻締好。"
    dan "此時賊氛四起，刻刻有喪亂之憂，既得其人，就該速許，為甚麽還要遲疑觀望？"
    dan "聞得昨日給了資本，著他往松江貿易，許親的話並不提起。"
    dan "我想如此亂世，凡有閨女的人家，個個都想贅婿，有他這種才貌，那一處不得良緣？"
    dan "萬一在途路之間，被人要截了去，我再想這等一位才郎，就萬萬不能勾了。"
    dan "我與姚生的婚姻，既出父母之口，又處離亂之世，若還父母不決斷，自己又不決斷，就叫做見義不為，豈不誤了終身之事？"
    dan "我不如會他一面，許下婚姻，然後待他出去，方才穩妥。"
    ""
    dan "我想夜間會他，到底不妥，明人不作暗事，竟在青天白日之下，何等不好！"
    dan "不如借筆墨傳情，寫幾句話兒示意於他便了。"
    dan "筆硯在此，待我取一幅綾帕出來。"
    hide dan_foldarms
    show handkerchief
    ""
    narrator "寫點什麼好呢？"
    label choose_write:
    menu: 
        "寫點什麼好呢？"
        "窈窕淑女，君子好逑":
            ""
            dan "我道為甚麽寫不下去，原來被「窈窕」二字礙住了手。"
            dan "這「窈窕」二字，乃是風人的口氣，豈有做婦人家的自誇窈窕之理？"
            jump choose_write
        "窈窕君子，淑女好逑":
            hide handkerchief
            with dissolve
            show yaotiao
            with dissolve
            ""
            dan "帕已寫完，待我藏在袖中，遇見他的時節，擲在籬邊，且看他怎生回答？"
            jump handkerchief_end

label handkerchief_end:
    scene black
    pause 1.0
    $ end_of_act("書帕")
    menu:
        "主要人物都上場了，下一幕要..."
        "打鐵趁熱，搬演姚繼和曹儷人密會戲碼。":
            jump date
        "調劑氛圍，安排反派登場。":
            jump villain

label date:
    scene black
    $ show_act_title_auto()
    scene bg cottage
    show sheng_foldarms_full at Transform(zoom=1, xalign=0.5, yalign=0.1, xzoom=-1)
    ""
    sh "小生自蒙高鄰仗義，不受券約，假以多金，眼見得治生有賴，行囊早已辦就，只在明日起行。"
    sh "我乃無家無室之人，作客與在家總是一樣。論起理來，今日出門，只該歡歡喜喜，沒有一毫牽掛才是。"
    sh "怎麽這心窩里面，還有些不伶不俐，卻像有些甚麽物件丟不下一般？"
    ""
    hide sheng_foldarms_full
    show sheng_foldarms_full at Transform(zoom=1, xalign=0.5, yalign=0.1)
    sh "哦，是了，這籬笆西首，就是曹小姐的臥房。"
    sh "他時常隔著籬笆，將一雙嬌嬌滴滴的眼兒覷我，所以走到這邊，就覺得依依難捨。"
    sh "原來我不忍離家，就為著這樁心事。"
    $ renpy.notify("李漁：生旦相見，務使委曲婉轉")
    pause 1.5
    $ renpy.notify("最能搖人心魄者，得教移船相近，卻還猶抱琵琶！")
    ""
    hide sheng_foldarms_full
    show bg door_open
    sh "你看臥房門啟，想是曹小姐聽見聲音，知道小生在此，又出來探望了。"
    sh "我且閃在一邊，看他出來做些甚麽？"
    ""
    show bg dan_out
    show sheng_2_contemplate at Transform(zoom=0.4, xalign=0.95, yalign=0.999)
    ""
    sh "你看他遮遮掩掩，欲進不進，分明要待我呼喚，方才近身。"
    sh "噯！我若要招攬他來，有甚難處，只為他父親是個好人，又有恩義到我，我若調戲他令愛，就是個負心漢了。"
    ""
    dan "立了半晌，不見他則聲，可見是個志誠君子，愈加令人起敬。"

label villain:
    scene black
    $ show_act_title_auto()
    scene bg military
    play music "audio/drums.mp3" fadein 3.0
    pause 4.0
    ""
    show soldier_tiger at Transform(zoom=0.65, xalign=0.95, yalign=0.05)
    with dissolve
    tiger "小將名為一只虎，丈八長矛三尺斧。"
    tiger "殺人最喜殺肥人，好剝寬皮蒙大鼓。"
    tiger "自家非別，闖王部下一個頭目，喚做一只虎的便是。王爺升殿，須索伺候。"
    show soldier_wolf at Transform(zoom=0.9, xalign=0.02, yalign=0.05)
    with dissolve
    wolf "小將名為獨行狼，擾盡中原孰敢當？"
    wolf "殺人最喜殺秀士，好充鮮味呷酸湯。"
    wolf "自家非別，闖王部下一個頭目，喚做獨行狼的是也。王爺升殿，須索伺候。"
    show soldier_scorpion at Transform(zoom=0.7, xalign=0.3, yalign=0.1)
    with dissolve
    scorpion "小將名為蠍子塊，赤手沖鋒不持械。"
    scorpion "殺人最喜殺婦人，下段腌來充淡菜。"
    scorpion "自家非別，闖王部下一個頭目，喚做蠍子塊的是也。王爺升殿，須索伺候。"
    show soldier_star at Transform(zoom=0.8, xalign=0.7, yalign=0.001)
    with dissolve
    star "小將名為過天星，獨自屠城不帶兵。"
    star "殺人最喜殺美女，好從刀下聽嬌聲。"
    star "自家非別，闖王部下一個頭目，喚做過天星的是也。王爺升殿，須索伺候。"
    ""
    hide soldier_tiger
    hide soldier_wolf
    hide soldier_scorpion
    hide soldier_star
    with dissolve
    show chuang_mad_full at Transform(zoom=1, xalign=0.5, yalign=0.2)
    with dissolve
    ""
    chuang "談笑揮戈霸業成，自言吾合繼朱明。"
    chuang "雖然未正官家號，久噪中原帝子名。"
    chuang "孤家李自成是也。"
    chuang "只因孤家不讀兵書，好為野戰，攻城掠地，只以沖突為先。"
    chuang "所以四海聞名，齊上尊號，背後呼為闖賊，當面喚作闖王。"
    chuang "凡是投兵效用之人，聞闖即來，非闖即去。"
    chuang "只要闖得天下到手，就拿這個字眼做了國號，也未嘗不可。"
    chuang "今日分兵遣將，經略中原，不免升殿號令一番，然後起兵前去。"
    ""
    chuang "眾將官齊集東廊聽點！"
    soldiers "嗄！"
    chuang "統領陸師，經略山東、山西等處，權將軍一隻虎。"
    show soldier_tiger at Transform(zoom=0.65, xalign=0.05, yalign=0.05)
    with dissolve
    tiger "有！"
    chuang "那青齊負山面海，晉趙表里山河，都有重兵防守，你有何力量，攻取得來？說與孤家聽者。"
    tiger "{i}何用費焦勞，不是兵微餉少。看蜂屯蟻聚，人人慮閒憂飽；更喜的是貪財慕色，破堅城似渴馬奔池沼。{/i}"
    chuang "好，正合著孤家的意思。與你十萬精兵，沿途去搜刮糧餉。"
    chuang "統領陸師，經略河南、陜西等處，權將軍獨行狼。"
    hide soldier_tiger
    show soldier_wolf at Transform(zoom=0.9, xalign=0.98, yalign=0.05, xzoom=-1)
    with dissolve
    wolf "有！"
    chuang "那中州負嵩繞洛，西秦有百二山河，也都是重兵防守。你有何力量攻取得來？說與孤家聽者。"
    wolf "{i}心高，恨不把全任上肩挑，何況彈丸輕小。只靴尖一踢，把華嵩變做池沼。{/i}"
    chuang "好，也合著孤家的意思。與你十萬精兵，沿途去搜刮糧餉。"
    chuang "統領水陸二師，經略南京、浙江等處，權將軍蠍子塊。"
    hide soldier_wolf
    show soldier_scorpion at Transform(zoom=0.7, xalign=0.05, yalign=0.1)
    with dissolve
    scorpion "有！"
    chuang "這一京一省，乃是中原財賦之地，我要力攻，他也決要死守。你有何計何能，可以一鼓而下？"
    scorpion "{i}富民多，堅城少，重資繁，開門早。這是行兵訣，行兵訣不爽分毫。{/i}"
    chuang "一發講的好，足見胸中的韜略。與你二十萬雄兵，沿途去搜刮糧餉。"
    chuang "統領水陸二師，經略湖廣、江西等處，權將軍過天星。"
    hide soldier_scorpion
    show soldier_star at Transform(zoom=0.8, xalign=0.98, yalign=0.001)
    with dissolve
    star "有！"
    chuang "湖廣、江西二省，這都是中原形勝之地，恐怕黔、蜀二處的援兵順流而下，與我兵相抗起來，勝敗未可知也。你有何必勝之策，保得無虞？"
    star "{i}少聲援，心偏小，靠鄰封，城難保。這也是行兵訣，行兵訣不爽分毫。{/i}"
    star "{i}怕甚麽猛舟師萬櫓齊搖，等援兵來到，頭枯額已焦。{/i}"
    chuang "一發講得妙，足見平日的智謀。與你二十萬雄兵，沿途去搜刮糧餉。"
    pause 0.5
    hide soldier_star with dissolve
    show soldiers_back at Transform(zoom=1.5, xalign=0.5, yalign=-0.4)
    with dissolve 
    ""
    chuang "我且問諸位，行兵之道，當以何事為先？"
    soldiers "古語道得好，三軍未動，糧草先行，措餉是第一著。"
    chuang "說的不差。只是措餉之法多端，你們未必盡曉，待孤家歷數一遍。"
    soldiers "正要求千歲指教。"
    chuang "第一是嚴搜庫藏，第二是洗刮民財，第三是酷比縉紳，第四是多掠婦女。"
    chuang "這四樁事情，都是生財的大道，你們須要緊記在心。"
    soldiers "請問千歲：那嚴搜庫藏，遍掠民財，是臣等做慣的事，不說自明。"
    soldiers "只有酷比縉紳，多掠婦女，這兩句話還不甚解，再求明示一番。"
    chuang "縉紳做過美官，家家都有積蓄，處此亂世，定有法子收藏，決不放在家中，被人搜取，不是嚴刑拷打，如何逼得出來？"
    chuang "婦女各有親人，擄在軍中，不怕不來取贖。等到一兩月之後，沒人來取，就將他變賣，也是一宗軍餉。故此都叫做生財之道。"
    soldiers "千歲極講得是，謹遵聖諭而行。"
    chuang "軍令既已申明，就此起兵前去。"
    scene black
    pause 1.0
    $ end_of_act("闖氛")
return


    # 遊戲結束。

