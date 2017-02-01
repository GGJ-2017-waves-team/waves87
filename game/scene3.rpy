label scene3:

    image bg pirate_waves1 = "pirate_waves1.png"
    image kawa story = "characters/kawa_story.png"
    image kawa miss = "characters/kawa_miss.png"
    image kawa up = "characters/kawa_up.png"
    image tomo story = "characters/tomo.png"
    image bg kanji_friend = "kanji_friend.png"

    scene bg kanji_friend with dissolve

    play sound "waves.ogg"
    "{color=#FF1493}F  R  I  E  N  D{/color}"
    stop sound fadeout 1.5

    play music "cruisin_2.mp3" loop
    scene bg waves1 with dissolve:
        "pirate_waves1.png"
        pause 0.75
        "pirate_waves2.png"
        pause 0.75
        "pirate_waves3.png"
        pause 0.75
        repeat

    show kawa story at left with moveinbottom
    show tomo story at right with moveinbottom

    "(Back on the top deck...)"

    K "Listen, you've got me all wrong..."

    T "Oh no, big boy, it's time I show the crew what happens to weaklings on this ship."

    hide kawa story
    show kawa miss at left

    K "I'm not a tough guy. I don't want to fight..."

    image tomo_slide_left:
        "characters/tomo.png"
        xalign 1.0 yalign 1.0
        linear 0.5 xalign 0.3

    hide tomo story
    show tomo_slide_left

    T "That's too bad, baby."

    menu:
        "Kick Tomo in the face!":
            jump fight_tomo

        "Punch Tomo in the stomach!":
            jump fight_tomo

label fight_tomo:
    
    call tomo_begin_hunt

    scene black

    scene bg waves1 with dissolve:
        "pirate_waves1.png"
        pause 0.75
        "pirate_waves2.png"
        pause 0.75
        "pirate_waves3.png"
        pause 0.75
        repeat

    hide tomo_slide_left with hpunch
    play music "cruisin_2.mp3" loop
    hide kawa miss
    show kawa up at left
    show tomo story at right with dissolve

    T "HEY! THAT REALLY HURTS!"

    K "Wow... I... I did it..."

    T "You know what, you're a little blowfish! Unsuspecting, but brutal."

    T "I'm gonna call you Fugu, for blowfish. You're alright. Let's go have a drink, on me."

    hide tomo story with moveoutbottom
    hide kawa story with moveoutbottom
    stop music fadeout 2.0 

jump scene4