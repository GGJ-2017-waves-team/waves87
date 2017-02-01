
init python:
    config.screen_width = 1280
    config.screen_height = 720
    build.name = "waves87"

define Kawa = Character("Kawa", color=(0, 100, 255, 255))
define coWorkers = Character("Co-Workers")
define Fujitsu = Character("Fujitsu-San (THE BOSS)", color=(200, 0, 200, 255))
define Misc = Character("Miscellaneous Co-Workers")
define Seagull = Character("Seagull")
define Inu = Character("Inu")
define Tomo = Character("Tomo (PIRATE)", color=(0, 200, 0, 255))
define Crowd = Character("Crowd")
define Mai = Character("Mai (NOTORIOUS RIVAL GANG LEADER)", color=(0, 200, 200, 255))
define Terry = Character("Terry (CAPTAIN OF THE RIGGER)", color=(200, 0, 200, 255))
define T = Character("Tomo", color=(0, 200, 0, 255))
define K = Character("Kawa", color=(0, 100, 255, 255))
define Doge = Character('Doge', color=(200, 200, 0, 255))
define Strange_Voice = Character('Strange Voice')
define Tomo = Character('Tomo', color=(0, 200, 0, 255))
define F = Character("Fugu", color=(0, 100, 255, 255))
define tr = Character("Terry")
define fugu = Character("Fugu", color=(0, 100, 255, 255))
define tomo = Character('Tomo', color=(0, 200, 0, 255))
define boss = Character("Fujitsu-San (THE BOSS)", color=(200, 0, 200, 255))
define terry = Character("Terry (Captain)", color=(200, 200, 200, 255))
define f = Character("Fugu", color=(0, 100, 255, 255))
define t = Character("Tomo", color=(0, 200, 0, 255))
define m = Character("Mai", color=(0, 200, 200, 255))

image fujitsu = "images/characters/fujitsu_story.png"
image Mai = "images/characters/mai1.png"
image waves = "waves 2.png"
image cruiseShipDay = "waves1.png"
image fuguUncomfortable = "images/characters/fugu1.png"
image fuguUncomfortable2 = "images/characters/kawa_story.png"
image dogKanji = "dog.gif"
image kawaPoo = "images/characters/kawa_poo.png"
image fuguThumbsUp = "images/characters/kawa_up.png"
image kawaMiss = "images/characters/kawa_miss.png"

image bg brig1 = "images/brig1.png"
image bg brig2 = "images/brig2.png"
image bg brig3 = "images/brig3.png"

image dog normal = 'images/characters/dog1.png'
image dog aggressive = 'images/characters/dog2.png'
image dog passive = 'images/characters/dog3.png'

image kawa_story normal = "images/characters/kawa_story.png"
image kawa_victory = "images/characters/kawa_up.png"
image kawa_miss = "images/characters/kawa_miss.png"

image tomo_story = "images/characters/tomo.png"

image bg sake = "images/sake.png"
image bg bar1 = "images/bar1.png"
image bg bar2 = "images/bar2.png"
image bg bar3 = "images/bar3.png"
image bg logo = "logo.jpg"
image fugu story = "images/characters/fugu_story.png" #kawa = fugu
image blowfish = "images/characters/tomo.png" #blowfish = tomo
image mai = "images/characters/mai1.png"

# The game starts here.

label start:

    scene waves
    with fade
    play sound "waves.ogg"
    "{color=#FF1493}W  A  V  E  S{/color}"
    stop sound fadeout 1.5
    play music [ "<silence 2.0>", "cruisin_2.mp3" ] fadein 1.5 loop

    coWorkers "Hey Fugu, you feeling alright there sport?"
    coWorkers "Hah, this loser. Late on filing his TPS reports for the third time, now he's seasick on a cruiseship." 
    coWorkers "Wouldn't be the first time we've seen him puke his brains out. Remember the last company dinner?"
    coWorkers "Haha yeah that's right! Hey you been laying off the seafood there, buddy?"
    
    
    scene backgrounds:
        "images/waves1.png"
        pause 0.75
        "images/waves2.png"
        pause 0.75
        "images/waves3.png"
        pause 0.75
        repeat
    
    show fuguUncomfortable
    with slideleft


    # These display lines of dialogue.

    Kawa "..."
   
    Kawa "(Quick. Think of a comeback!)"

    menu:
        "(Insult your co-workers' mothers)":
            jump failureMom
        "(Insult your co-workers' ties)":
            jump failureTies

    label failureMom:
        Kawa "yeah...well, your Mom...lays off..."
        Kawa "...seafood. Because she's fat."
        with zoomin
        Kawa "..."
        coWorkers "..."
        with zoomout
        jump awkward 

    label failureTies:
        Kawa "Yeah well, you should lay off..."
        Kawa "...stupid ties."
        hide fuguUncomfortable
        show kawaMiss
        coWorkers "..."
        jump awkward 
       
    label awkward:  
    coWorkers "What was that, Fugu? You forgetting you're still a temporary hire?"
    hide kawaMiss
    hide fuguUncomfortable
    show fuguThumbsUp
    
    Kawa "...I mean. Hahah yeah, well, no more adventurous eating for me."
    Kawa "Fugu. Yep. Thaaaaat's my nickname."
    coWorkers "Right. You know, there's been talk that Fujitsu-San will be letting some people go at the end of the quarter..."
    Fujitsu "KAWA. WHERE HAVE YOU BEEN?"
    hide fuguThumbsUp
    show kawaMiss
    show fujitsu at right with moveinright
    Kawa "Fujitsu-san! I've been..."
    Fujitsu "SHUT UP."
    hide kawaMiss
    
    show fuguUncomfortable2 
    Fujitsu "DO YOU HAVE ANY IDEA HOW ANGRY OUR CLIENTS WERE ABOUT THOSE LATE FILINGS. DO YOU UNDERSTAND THE DISHONOR YOU'VE BROUGHT UPON MY BELOVED KANJI CORP.???"
    
    menu: 
        "(Say you will dishonor Fujitsu-San's beloved Mom)":
            jump rhetorical_dude
        "(Insult Fujitsu-san's waistline)":
            jump rhetorical_dude 
        "(Say Nothing)":
            jump offBoat
    label rhetorical_dude: 
    Kawa "Oh yea well..."
    Fujitsu "THAT WAS RHETORICAL." 
    label offBoat:
    Fujitsu "LISTEN UP. I WANT YOU TO THINK ABOUT OUR COMPANY VALUES. YOU SEE..."
    Kawa "(...why did I have to eat that blowfish and get sick? They call me Fugu now. Great. Who wants to be a blowfish...)"
    Fujitsu "...COMPANY VALUE #4 IS INTEGRITY. YOU FAILED TO DEMONSTRATE INTEGRITY WHEN I SENT YOU THE TPS REPORTS ON..."
    Kawa "(... I justed wanted to impress management...Working for KANJI Corp. is all I've ever wanted. Years of school..."
    Fujitsu "HEY. ARE YOU EVEN LISTENING?" 
    play audio "phone-ringing.ogg"
    "(PHONE RINGS)"
    Fujitsu "OK, NO SHUT UP. I NEED TO TAKE THIS CALL ON MY CELLULAR PHONE. "
    Fujitsu "WHEN I COME BACK WE'RE GONNA TALK ABOUT YOUR FUTURE AT THIS COMPANY." 
    hide fujitsu with moveoutright 
    Kawa "..."
    stop music fadeout 2.0
    play sound "waves.ogg" loop
    hide fuguUncomfortable2
    show kawaMiss
    Kawa "(...He's going to fire me. I'm going to get fired on the company cruise.)" 
    Kawa "(I refuse to go on as Fugu. I'm done)"
    hide kawaMiss
    show fuguUncomfortable
    '...'
    image fuguUncomfortableSlide:
        "images/characters/fugu1.png"
        xalign 0.5 yalign 1.0
        linear 3.5 xalign 0.0
    hide fuguUncomfortable
    show fuguUncomfortableSlide
    "Goodbye ocean. Goodbye cruiseship. Goodbye seagulls."
    
    hide fuguUncomfortableSlide
    show kawaPoo at left
    play audio "seagull.ogg"
    "Splat!"
    hide kawaPoo at left
    show kawaMiss at left 
    ''
    hide kawaMiss with moveoutbottom 
    '(Jumps)'
    stop music fadeout 2.0

scene black 
play music "title_track.mp3" loop
scene bg logo 
with dissolve
''
''
stop music fadeout 2.0

label scene2:

    scene black
    scene dogKanji with fade

    play sound "waves.ogg"
    "{color=#FF1493}D  O  G  E{/color}"
    stop sound fadeout 1.5

    scene black
    play music "dogesong.mp3" loop

    Kawa "Ungh... where am I?...."
    Strange_Voice "...you're dead, buddy.."

    scene bg brig1:
        'images/brig1.png'
        pause 0.75
        'images/brig2.png'
        pause 0.75
        'images/brig3.png'
        pause 0.75
        repeat
    with fade


    show dog normal at right with dissolve

    show dog aggressive:
        "images/characters/dog2.png"
        pause 1.5
        "images/characters/dog3.png"
        pause 1.5        
        repeat

    show kawa_story normal at left with dissolve

    show kawa_story:
        "images/characters/kawa_story.png"
        pause 3.55
        "images/characters/kawa_miss.png"
        pause 0.99
        repeat

    "... ...."
    "... .... ..."
    Kawa "Huhh? Who are you!?"
    play sound "dog-bark.ogg"
    Doge "woof woof"
    play sound "dog-bark.ogg"
    Kawa "Oh, good grief. What is this place?! I need to get out of here."
    Kawa "woof"
    Kawa "....I sure am hungry. What's in this bowl over here? Perhaps little doge wouldn't mind if I had just a sip..."
    Doge "..."
    Doge ".... ......"

    transform left_to_right:
        xalign 0.7

    image kawa_slide_right:
        "images/characters/kawa_story.png"
        xalign 0.0 yalign 1.0
        linear 3.5 xalign 0.55

    hide kawa_story normal
    show kawa_slide_right

    play sound "dog-growl.ogg"

    Doge "grrrrr"

    menu:
        "Fight the dog off":
            jump post_fight
        "Try to get the soup and risk fighting the dog":
            jump post_fight

label post_fight:

call dog_begin_hunt from _call_dog_begin_hunt

scene bg brig1:
    'images/brig1.png'
    pause 0.75
    'images/brig2.png'
    pause 0.75
    'images/brig3.png'
    pause 0.75
    repeat

show kawa_victory

play music "cruisin_2.mp3" loop


Kawa "Ah, that wasn't so bad, eh? This old blowfish can still hold his own, after all! Heh hyeh heh!"


show tomo_story at right with moveinright

Tomo "What's all the commotion down here?! And where is Doge?!"
Kawa "......."
Kawa "....... ......"
Tomo "Never mind that. C'mon up to the deck. We're gonna see how tough you really are, scalawag"

hide tomo_story with moveoutright
hide kawa_victory with moveoutright

jump scene3





