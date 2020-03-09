'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def do_count(count, word_list, word_length, letter1, letter2):
    if letter2 == word_length:  # setup the ending parameter
        if word_list[letter1] == "t" and word_list[letter2] == "h":
            count.append((word_list[letter1], word_list[letter2]))
            return len(count)
        if word_list[letter1] != "t":
            print('not happening on the last pair')
            return len(count)
    else:
        if word_list[letter1] != "t" and letter2 != word_length:
            print(f"letter1 is not 't' it's {word_list[letter1]}")
            print(f"letter1: {letter1}")
            return do_count(count, word_list, word_length, letter1+1, letter2+1)
        # was at end... and letter2 < word_length
        elif word_list[letter1] != "t" and word_list[letter2] != "h":
            print(f"letter1 is 't' but...")
            print(f"letter2 is not 'h' it's {word_list[letter2]}")
            return do_count(count, word_list, word_length, letter1+1, letter2+1)
        elif word_list[letter1] == "t" and word_list[letter2] == "h":
            count.append((word_list[letter1], word_list[letter2]))
            print(letter1, letter2, count)
            return do_count(count, word_list, word_length, letter1+1, letter2+1)
    # pass


def count_th(word, letter1=0, letter2=1):
    if word == '' or word == " ":  # if empty or has a empty value
        return 0
    # TBC
    else:
        word_list = [letter for letter in word]
        word_length = len(word_list)
        print(word_list, len(word_list))
        count = []
        return do_count(count, word_list, word_length, letter1, letter2)


print(count_th("bthhbthhblahdth"))

# print(count_th("THtHThth"))


# MY OTHER VERSION FROM PREVIOUS RUN THROUGH THIS SECTION
# def move_it(together, lower_word, frst, secnd, count):
#     together = lower_word[frst]+lower_word[secnd]
#     if secnd < len(lower_word)-1:
#         if together == "th":
#             count.append(['th'],)
#             print("in does equal th:", len(count))
#             frst += 1
#             secnd += 1
#             print("in if does equal th:", together)
#             # print(frst, secnd)
#             move_it(together, lower_word, frst, secnd, count)
#         elif together != "th":
#             frst += 1
#             secnd += 1
#             move_it(together, lower_word, frst, secnd, count)
#             # print("in elif doesnt equal th:", together)
#             # print(frst, secnd)

#     elif secnd == len(lower_word)-1:
#         if together == "th":
#             count.append(['th'])
#             print(len(count))
#             # print(together)
#             # print(frst, secnd)
#     print(f"this is the final answer... should be 2: {len(count)}")
#     return len(count)


# def count_th(word, frst=0, secnd=1, count=[]):
#     if word == " " or word == "":
#         return 0
#     else:
#         count = []
#         lower_word = word
#         together = lower_word[frst]+lower_word[secnd]
#         # print("together:", together)

#         return move_it(together, lower_word, frst, secnd, count=[])
