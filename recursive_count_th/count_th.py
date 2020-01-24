'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def move_it(together, lower_word, frst, secnd, count):
    together = lower_word[frst]+lower_word[secnd]
    if secnd < len(lower_word)-1:
        if together == "th":
            count.append(['th'],)
            print("in does equal th:", len(count))
            frst += 1
            secnd += 1
            print("in if does equal th:", together)
            # print(frst, secnd)
            move_it(together, lower_word, frst, secnd, count)
        elif together != "th":
            frst += 1
            secnd += 1
            move_it(together, lower_word, frst, secnd, count)
            # print("in elif doesnt equal th:", together)
            # print(frst, secnd)

    elif secnd == len(lower_word)-1:
        if together == "th":
            count.append(['th'])
            print(len(count))
            # print(together)
            # print(frst, secnd)
    print(f"this is the final answer... should be 2: {len(count)}")
    return len(count)


def count_th(word, frst=0, secnd=1, count=[]):
    if word == " " or word == "":
        return 0
    else:
        count = []
        lower_word = word
        together = lower_word[frst]+lower_word[secnd]
        # print("together:", together)

        return move_it(together, lower_word, frst, secnd, count=[])


print(count_th('abcdefthgTHHIJKLMNOP'))
