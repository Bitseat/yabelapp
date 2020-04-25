import re 

def test():
    s = "BANK OF A B YS SIN I A US Embassy Machine Readable Visa Fee Receipt For Non-Immigrant Visa Applications  Date 20200101: Receipt No : TT2000 Credit AC NO :46539 Branch :OLYMPIA BRANCH Payment Identification No. (PIN) 6133416588546 Name of Applicant : BEHAILU DEREJE DEKEBA )     Birr :FIVE THOUSAND SIX HUNDRED ONLY Birr 5,600.0 Prepared by   t  ** * ****** ********** *****  Receiving Teller     Not Refendabl e **********  *  Retain for historic  BANX OF &3YS3INIA  NA RANCH"
    res = re.findall(r"[\w']+", s)
    print(res)

    split_word1 = "Name of Applicant"
    split_word2 = "Date"
    split_word3 = "Birr"

    listToStr = ' '.join([str(elem) for elem in res])

    str_res1 = listToStr.partition(split_word1)[2]
    str_res2 = listToStr.partition(split_word2)[2]
    str_res3 = listToStr.partition(split_word3)[2]

    list1 = list(str_res1.split(" "))
    list1 = list1[0:4]
    list1 = ' '.join([str(elem) for elem in list1])

    list2 = list(str_res2.split(" "))
    list2 = list2[0:2]
    list2 = ' '.join([str(elem) for elem in list2])

    list3 = list(str_res3.split(" "))
    list3 = list3[0:6]
    list3 = ' '.join([str(elem) for elem in list3])

    x = split_word1 + ":" + list1
    y = split_word2 + ":" + list2
    z = split_word3 + ":" + list3

    print("%s : %s " % (split_word1,list1))
    print("%s : %s " % (split_word2,list2))
    print("%s : %s " % (split_word3,list3))
    return list1, list2, list3





