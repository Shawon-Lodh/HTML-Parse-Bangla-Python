

import HtmlParserBangla

import csv
import datetime


def main():

    # a = open('2018-11-29 08:57:08.689280.txt', 'r')
    # b = open('result.txt', 'r')
    # # c = open('2018-11-28 13:57:15.748050.txt', 'r')
    # r = open('result2.txt', 'w+')
    # result = set()
    # for x in a:
    #     result.add(x.replace('\n', ''))
    # for y in b:
    #     result.add(y.replace('\n', ''))
    # # for z in c:
    # #     result.add(z.replace('\n', ''))
    # for word in result:
    #     r.write(word+'\n')









    

    HtmlParserBangla.unique_word(base_url="http://edpdbd.org")   # It takes long time # see the html_parse.txt














    # parts_of_speech_to_word={}
    # parts_of_speech_to_word_count={}
    # word_to_parts_of_speech={}
    # word_with_pos=open('words.csv', 'r')
    # for a in word_with_pos:
    #     line = a.replace('\n', '').split(',')
    #     word_to_parts_of_speech[line[2]] = line[1]
    #     parts_of_speech_to_word_count[line[1]]=0
    #     parts_of_speech_to_word[line[1]] = []
    #
    #     # try:
    #     #     parts_of_speech_to_word[line[1]] += [line[2]]
    #     # except Exception as e:
    #     #     parts_of_speech_to_word[line[1]] = [line[2]]
    # input_words = open('result.txt', 'r')
    # for word in input_words:
    #     try:
    #         w = word_to_parts_of_speech[word.replace('\n', '')]
    #         if len(w) > 0:
    #             parts_of_speech_to_word_count[w] += 1
    #             parts_of_speech_to_word[w] += [word.replace('\n', '')]
    #     except Exception as e:
    #         continue
    # file_word_pos=open(str(datetime.datetime.now())+'.txt', 'w+')
    # file_pos_word=open(str(datetime.datetime.now())+'.txt', 'w+')
    # file_pos_word_count=open(str(datetime.datetime.now())+'.txt', 'w+')
    #
    # for word in word_to_parts_of_speech:
    #     file_word_pos.write(word + ',' + word_to_parts_of_speech[word] + "\n")
    #
    # for word in parts_of_speech_to_word_count:
    #     file_pos_word.write(word + ',' + str(parts_of_speech_to_word_count[word])+"\n")
    #
    # for word in parts_of_speech_to_word:
    #     file_pos_word_count.write(word + ": \n")
    #     for w in parts_of_speech_to_word[word]:
    #         file_pos_word_count.write(w+",")
    #     file_pos_word_count.write("\n")


if __name__ == "__main__":

    main()
