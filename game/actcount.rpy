# 劇情進度
default act_history = []
default act_no = 0

# 所有角色的位置（初始都在 None 或者指定地點）
default character_positions = {
    "sheng": None,      # 角色「生」，即姚繼
    "dan": None,   # 角色「旦」，即曹小姐
    "yaofu": None,     # 角色姚父
    "yaowife": None,     # 角色姚夫人
    "wai": None,     # 角色「外」，即尹小樓
    "laodan": None, # 角色「老旦」，即尹妻
}

# 團圓檢查的目標地點
define reunion_location = "鄖陽"  # 可以改成其他地點

init python:
    def start_new_run():
        store.act_history = []
        store.act_no = 0
        for k in store.character_positions:
            store.character_positions[k] = None

init python:
    def end_of_act(act_name):
        if act_name in store.act_history:
            idx = store.act_history.index(act_name)
            store.act_history = store.act_history[:idx + 1]
        else:
            store.act_history.append(act_name)
        store.act_no = len(store.act_history)
        renpy.log(f"[DEBUG] Act history: {store.act_history}, Current act_no: {store.act_no}")

init python:
    def check_reunion():
        """
        在第33齣檢查所有角色是否在同一個地點。
        判定成功 / 失敗 / 太早結束。
        """
        if store.act_no < 33:
            return  # 還沒到第33齣，不檢查

        # 檢查角色位置
        positions = [pos for pos in store.character_positions.values() if pos is not None]
        if len(set(positions)) == 1 and len(positions) > 0:
            # 所有角色齊聚
            renpy.jump("ending_reunion_success")
        else:
            renpy.jump("ending_reunion_fail")

# 劇情label中所需之齣數判定
label act_a:
    "這是 A 劇情"
    $ character_positions["mo"] = "漢陽"
    $ character_positions["sheng"] = "鄖陽"
    $ end_of_act("act_a")
    jump next_menu

label ending_reunion_success:
    scene bg room
    "所有角色在第33齣齊聚一地，團圓大成功！"
    return

label ending_reunion_fail:
    scene bg room
    "第33齣結束，但角色沒有齊聚，團圓失敗！"
    return

# 劇情提早結束
label premature_end:
    "劇情過早結束，李漁認為尚未成戲。"
    return
# 放在提前結束的劇情結尾
if act_no < 33:
    jump premature_end
