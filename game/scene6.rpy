

label scene6:

    image bg blowfish = "images/blowfish.png"
    image bg waves1 = "images/waves1.png"
    image bg waves2 = "images/waves2.png"
    image bg waves3 = "images/waves3.png"
    image bg king = "kanji_king 2.png"

    image fugu down = "images/characters/fugu_down.png"
    image fujitsu = "images/characters/fujitsu_story.png"
    image fdefeated = "images/characters/fujitsu_defeated.png"
    image tomo = "images/characters/tomo.png"


    scene bg king 
    with fade
    play music "title_track.mp3" loop
    "(KING)"

    scene bg waves1:
        "images/waves1.png"
        pause 0.6
        "images/waves2.png"
        pause 0.6
        "images/waves3.png"
        pause 0.6
        repeat

    show fugu down at left
    show tomo at right
    with moveintop
    show fujitsu
    with moveinbottom

    fugu "Arrrrgh!" 
    tomo "Arrrrrgh"
    boss "Kawa! Where have you been? And why are you dressed like an idiot?"

    menu:
        "It's Fugu!":
            jump final

        "I feel beautiful":
            jump final

    label final:
        fugu "We're taking over the ship!"
        boss "huhhhhh?"
        fugu "This is war!!"

        call fujitsu_begin_hunt 

        scene bg waves1
        play music "title_track.mp3" loop

        hide fujitsu
        show fdefeated

        boss "Ahhhh!!! I'll never forgive you for this!!"
        boss "Also, YOU'RE FIRED!!!"
        fugu "I already knew my time was short with the company."
        fugu "Heh... But you're my captive now... and you WILL BE A PIRATE."

        scene black with dissolve

        return