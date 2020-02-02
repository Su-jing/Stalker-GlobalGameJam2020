################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Game_street
################################################################################
screen game_map_street_1():

    zorder 100

    modal True

    add 'bg_street_ani1' xpos -50 ypos 0 xoffset global_xoffset
    add 'bg_street_bg' xpos -50 ypos 0 xoffset global_xoffset
    add 'bg_street_ani2' xpos -50 ypos 0 xoffset global_xoffset

    timer 0.01 action Show('f_1_110', t=6)

    timer 6+2.6 action Show('m_s', t=1.5, transition=Dissolve(0.5))

    timer start_time_street+2.5 action Show('m_walk_slow', t=2.5)

    timer start_time_street+2.6 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.7 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.8 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.9 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.0 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.1 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.2 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.3 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.4 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.6 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.7 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.8 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.9 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.0 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.1 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.2 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.3 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.4 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.6 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.7 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.8 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.9 action SetVariable('global_xoffset', global_xoffset-20)

    timer start_time_street+4.8 action Show('m_s', t=999)

    use bg_street_lights
    # add 'bg_street_lights' xpos -50 ypos 0 xoffset global_xoffset*1.15

    timer start_time_street+4.6 action Return()

screen game_map_street_2():

    zorder 100

    if abs(global_xoffset) >= (3760-1280):
        timer 0.01 action Return('street')

    if interact >= 5:
        timer 0.01 action Return('E1')

    add 'bg_street_ani1' xpos -50 ypos 0 xoffset global_xoffset
    add 'bg_street_bg' xpos -50 ypos 0 xoffset global_xoffset
    add 'bg_street_ani2' xpos -50 ypos 0 xoffset global_xoffset

    timer start_time_street+4.5 action Show('m_s', t=999)

    add 'bg_street_lights' xpos -50 ypos 0 xoffset global_xoffset*1.15

    text _(str(interact)) xpos 200 ypos 50 color '#000'

    use bg_street_lights

    use game_buttonControll(3760-1280)


screen bg_street_lights():

    zorder 111

    add 'bg_street_lights' xpos -50 ypos 0 xoffset global_xoffset*1.15