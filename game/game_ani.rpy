################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Main
################################################################################
screen game_ani_start():

    # tag game_map_street
    modal True

    add 'f_1_110' xpos 622 ypos 650 align(0.5, 1.0)

    timer 1.2 action Hide('game_ani_start')