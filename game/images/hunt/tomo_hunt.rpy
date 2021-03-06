label tomo_begin_hunt:
    play music "hunt/BattleSuperShort.mp3" loop

    image bg battle_bg = "battle_bg.jpg"

    image tomo_target:
        "hunt/tomo_head.png"

    $ targets_needed = 3

    $ shots_fired = 0
    $ targets_hit = 0

    call tomo_hunting from _call_tomo_hunting

label tomo_finished_him:
    return
    
label tomo_hunting:
    
    $ import random
    $ xposi = random.randint(340, 940)
    $ yposi = random.randint(100, 420)

    transform tomo_moving_target:
        ypos yposi - 20
        linear 3.0 xpos 2000
        xpos -300

    scene bg battle_bg
    show tomo_target at tomo_moving_target
    $ position = At(ImageReference("tomo_target"), tomo_moving_target)
    show expression position

    $ ui.imagebutton("hunt/fist.png", "hunt/fist_hover.png", 
        clicked = ui.returns("fired"), xpos= xposi, ypos = yposi)
    $ fired_gun = ui.interact()
    

    show expression position
    if position.xpos > xposi - 50:
        if position.xpos < xposi + 50:
            $ targets_hit = targets_hit + 1
            if targets_hit >= targets_needed:
                jump tomo_finish_him
            play audio "punch-hit.ogg"
            with hpunch
            "You Hit! [targets_hit] / [targets_needed] Needed Hits Landed! "
            call tomo_hunting from _call_tomo_hunting_1
    
    if targets_hit >= targets_needed:
        jump tomo_finish_him
    
    play audio "miss_sound.ogg"
    with vpunch
    "You WHIFFED! [targets_hit] / [targets_needed] Needed Hits Landed! "
    
    call tomo_hunting from _call_tomo_hunting_2
    
    return

label tomo_finish_him:
    
    stop music fadeout 3.0

    image tomo_finished:
        "hunt/tomo_head.png"
        xalign 0.5 yalign 0.5

    hide tomo_finished with hpunch
    show tomo_finished with pixellate
    stop music fadeout 2.0

    return