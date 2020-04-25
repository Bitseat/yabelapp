import re 

def test(filename):
    res = re.findall(r"[\w']+", filename)
    split_word1 = "Name of Applicant"
    split_word2 = "Date"
    split_word3 = "Birr"

    listToStr = ' '.join([str(elem) for elem in res])

    str_res1 = listToStr.partition(split_word1)[2]
    str_res2 = listToStr.partition(split_word2)[2]
    str_res3 = listToStr.partition(split_word3)[2]

    res2 = re.findall(r"[\w']+", str_res3)
    listToStr2 = ' '.join([str(elem) for elem in res2 ])
    str_res4 = listToStr2.partition(split_word3)[2]

    print(listToStr2)
    list1 = list(str_res1.split(" "))
    list1 = list1[0:4]
    list1 = ' '.join([str(elem) for elem in list1])

    list2 = list(str_res2.split(" "))
    list2 = list2[0:2]
    list2 = ' '.join([str(elem) for elem in list2])

    list3 = list(str_res3.split(" "))
    list3 = list3[0:6]
    list3 = ' '.join([str(elem) for elem in list3])

    list4 = list(str_res4.split(" "))
    list4 = list4[0:3]
    list4 = ' '.join([str(elem) for elem in list4])

    x = split_word1 + ":" + list1
    y = split_word2 + ":" + list2
    z = split_word3 + ":" + list3
    a = split_word3 + ":" + list4

    return list1, list2, list3, list4





