

import re

def compareVersion(version1,version2):
    #split each version number into parts according to ‘.’
    s1=re.split('\.', version1)
    s2=re.split('\.',version2)

    s1=[int(s1[i]) for i in range(len(s1))]
    s2=[int(s2[i]) for i in range(len(s2))]

    if(s1>s2):
        return 'Version1 is greater than version2'
    if(s1<s2):
        return 'Version1 is less than version2'
    if(s1==s2):
        return 'Version1 is equal to version2'


if __name__=="__main__":
    #test case
    print(compareVersion('1.2','0.2.3'))
    print(compareVersion('1.1.1','1.0.1'))
    print(compareVersion('-1.1','-2.3'))
    print(compareVersion('-0.1','0.1'))
    print(compareVersion('3.3.4','3.3.5'))
    print(compareVersion('0.1.1','0.1.1.0'))
    print(compareVersion('1.1','1.2'))
    print(compareVersion('12.1','12.1.1'))
    print(compareVersion('test','abc'))
    print(compareVersion('abc','123'))
