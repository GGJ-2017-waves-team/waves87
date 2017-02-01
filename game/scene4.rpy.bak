label scene4:
    
    image bg sake = "images/sake.png"
    image bg bar1 = "images/bar1.png"
    image bg bar2 = "images/bar2.png"
    image bg bar3 = "images/bar3.png"

    image fugu story = "images/characters/fugu_story.png" #kawa = fugu
    image blowfish = "images/tomo.png" #blowfish = tomo
    image mai = "images/characters/mai1.png"

    scene bg sake
    with fade

    play sound "waves.ogg"
    "{color=#FF1493}S  A  K  E{/color}"
    stop sound fadeout 1.5

    play music "cruisin_tough.mp3" loop 
    scene bg bar1:
        "images/bar1.png"
        pause 0.6
        "images/bar2.png"
        pause 0.6
        "images/bar3.png"
        pause 0.6
        repeat

    show fugu story at left
    show blowfish at right
    with moveinbottom

    t "Arrrrgh! Get whatever you want fugu, this rounds on the house! *mean mugs the bartender*" 

    image tomo_mean_mug:

    image fugu_up:
        "images/characters/fugu_up.png"

    show fugu_up at left
    hide fugu story

    f "Okay"

    hide fugu_up
    show fugu story at left
    
    t "It's not often that I get to drink without the captain's smelly odor nearby. A toast to new friends."

    "WHAT ARE YOU DOING ON MY SIDE OF THE SEA!!!"
    

    show mai
    with moveinright

    menu:
        "Who's that babe?":
            jump heymai

        "CRAPPPPPPPP":
            jump heymai

    label heymai:
        t "Mai! We left you for dead! Get out of here before you kill my buzz."
        m "This time it is YOU who will DIE Tomo, along with the rest of the crew of the Rigger!"
        m "My men are outside, and we have you surrounded." 
        t "I can't even see straight! Get in there Fugu!" 

    call mai_begin_hunt 

    play music "cruisin_tough.mp3" loop 
    scene bg bar1:
        "images/bar1.png"
        pause 0.6
        "images/bar2.png"
        pause 0.6
        "images/bar3.png"
        pause 0.6
        repeat

    show fugu story at left
    show blowfish at right
    with moveinbottom

    t "Nice goin, Fugu! (hiccup)"
    f "Yeaaaaaaaaaa. Don't mess with us, lady!!"
    f "Tomo, let's get back to the ship"

    scene black with fadeout

jump scene5