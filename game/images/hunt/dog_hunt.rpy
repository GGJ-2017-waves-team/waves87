
label dog_begin_hunt:
    play music "hunt/BattleSuperShort.mp3" loop

    image bg battle_bg = "battle_bg.jpg"

    image dog_target:
        "hunt/dog_head.png"

    $ targets_needed = 2

    $ shots_fired = 0
    $ targets_hit = 0

    call dog_hunting from _call_dog_hunting

label dog_finished_him:
    return
    
label dog_hunting:
    
    $ import random
    $ xposi = random.randint(340, 940)
    $ yposi = random.randint(100, 420)

    transform dog_moving_target:
        ypos yposi - 50
        linear 3.0 xpos 2000
        xpos -300

    scene bg battle_bg
    show dog_target at dog_moving_target
    $ position = At(ImageReference("dog_target"), dog_moving_target)
    show expression position

    $ ui.imagebutton("hunt/fist.png", "hunt/fist_hover.png", 
        clicked = ui.returns("fired"), xpos= xposi, ypos = yposi)
    $ fired_gun = ui.interact()
    

    show expression position
    if position.xpos > xposi - 50:
        if position.xpos < xposi + 50:
            $ targets_hit = targets_hit + 1
            if targets_hit >= targets_needed:
                jump dog_finish_him
            play audio "punch-hit.ogg"
            with hpunch
            "You Hit! [targets_hit] / [targets_needed] Needed Hits Landed! "
            call dog_hunting from _call_dog_hunting_1
    
    if targets_hit >= targets_needed:
        jump dog_finish_him
    
    play audio "miss_sound.ogg"
    with vpunch
    "You WHIFFED! [targets_hit] / [targets_needed] Needed Hits Landed! "
    
    call dog_hunting from _call_dog_hunting_2
    
    return

label dog_finish_him:
    
    stop music fadeout 3.0

    image dog_finished:
        "hunt/dog_head.png"
        xalign 0.5 yalign 0.5

    hide dog_finished with hpunch
    show dog_finished with pixellate
    stop music fadeout 2.0 
    return