# scoring.rpy — Background Li Yu scoring system for Reunion
# Place this file in Reunion/game/

# Global score variable
default liyu_score = 0

# ------------------ SCORING FUNCTIONS ------------------
screen score_popup(msg):
    zorder 300  # 保證在最上層
    frame:
        at score_popup_anim
        background Solid("#0008")  # 半透明背景
        xalign 1.0   # 靠右
        yalign 0.0   # 靠上
        xpadding 10
        ypadding 50
        text msg color "#FFD700" size 25 xalign 0.5
        timer 2.0 action Hide("score_popup")  # 2 秒後自動消失

# 動畫：淡入 -> 等待 -> 淡出
transform score_popup_anim:
    alpha 0.0
    linear 0.3 alpha 1.0
    pause 1.4
    linear 0.3 alpha 0.0

init python:
    def score_act1(correct_order=True):
        global liyu_score
        if correct_order:
            liyu_score += 15
            renpy.call_screen("score_popup", msg="李漁：先有一小曲，再有一詞，開場得法！")
        else:
            liyu_score -= 10
            renpy.call_screen("score_popup", msg="李漁：亂了開場！")

    # Act 2 scoring: 引子 -> 定場白
    def score_act2(correct_order=True):
        """
        Add points if Act 2 follows 引子 -> 定場白 order.
        """
        global liyu_score
        if correct_order:
            liyu_score += 15
        else:
            liyu_score -= 10

    # 小收煞 (mid break)
    def score_xiaoshousha(has_xiaoshousha=True):
        """
        Add points if 小收煞 is included.
        """
        global liyu_score
        if has_xiaoshousha:
            liyu_score += 10
        else:
            liyu_score -= 5

    # 大收煞 (finale)
    def score_dashousha(natural=True):
        """
        Add points if the finale is natural and smooth.
        """
        global liyu_score
        if natural:
            liyu_score += 15
        else:
            liyu_score -= 10

    # Commentary based on final score
    def li_yu_commentary():
        """
        Returns Li Yu's comment based on the final score.
        """
        if liyu_score >= 40:
            return "李漁：『收場一出，勾魂攝魄，真絕技也！』"
        elif liyu_score >= 20:
            return "李漁：『尚能遵法，然猶見痕跡。』"
        else:
            return "李漁：『此非道中絕技，仍需涵泳吾法。』"