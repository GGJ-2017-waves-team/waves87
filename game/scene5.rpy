label scene5:

    image bg pirate_waves1 = "pirate_waves1.png"
    image fugu story = "characters/fugu_story.png"
    image fugu miss = "characters/fugu_miss.png"
    image fugu up = "characters/fugu_up.png"
    image tomo story = "characters/tomo.png"
    image terry story = "characters/terry.png"
    image bg kanji_group_leader = "kanji_group_leader.png"

    scene bg kanji_group_leader with dissolve

    play sound "waves.ogg"
    "{color=#FF1493}G  R  O  U  P    L  E  A  D  E  R{/color}"
    stop sound fadeout 1.5

    play music "cruisin_tough.mp3" loop 
    scene bg waves1 with dissolve:
        "pirate_waves1.png"
        pause 0.75
        "pirate_waves2.png"
        pause 0.75
        "pirate_waves3.png"
        pause 0.75
        repeat

    show fugu story at left with moveinbottom
    show tomo story at right with moveinbottom

    "(Back on the pirate ship...)"

    F "That was a close one!"

    T "Now way, Fugu, you really showed her!"

    F "I am growing stronger and stronger. Soon, no one will stop me."

    hide fugu story
    show fugu up at left

    F "I feel so powerful, I could challenge the Captain right now!"

    image terry_dropdown:
        "characters/terry.png"
        xalign 0.5 yalign -1.0
        linear 0.5 yalign 1.0

    show terry_dropdown

    tr "WHAT DID YOU SAY, YOU WORM??? I CRUSHED MAGGOTS LIKE YOU IN 'NAM EVERY DAY!!"

    F "It's the Captain of the Rigger!"

    T "Take him out Terry."

    hide fugu up
    show fugu story at left

    menu:
        "I challenge you! (Punch Terry in the stomach)":
            jump fight_terry

        "I'm the strongest here! (Kick Terry in the teeth)":
            jump fight_terry

label fight_terry:
    
    call terry_begin_hunt

    scene bg waves1 with dissolve:
        "pirate_waves1.png"
        pause 0.75
        "pirate_waves2.png"
        pause 0.75
        "pirate_waves3.png"
        pause 0.75
        repeat

    play music "cruisin_tough.mp3" loop
    show fugu story at left with moveinbottom
    show tomo story at right with moveinbottom

    tr "BARF!!"

    show terry story at center with pixellate

    tr "This guy is tough!!! Ungh... I'm gonna go lie down... You take over as captain now, Fugu..."

    hide terry story with moveoutbottom

    hide fugu story
    show fugu up at left

    T "Whoa!!"

    F "YUSSSSSSS."

    T "Well Captain, what do we do now?"

    T "I've got an old boss that I'd like to pay a visit to..."

    hide fugu story with moveoutbottom
    hide tomo story with moveoutbottom

    scene black with dissolve
    stop music fadeout 2.0 
    jump scene6