import pandas as pd
import numpy as np
import random

def get_sample_data(x, category, s1, a1, s2, a2, s3, a3, s4, a4, s5, a5, s6, a6, s7, a7, s8, a8, s9, a9, s10, a10,
s11, a11, s12, a12, s13, a13, s14, a14, s15, a15, s16, a16, s17, a17, s18, a18, s19, a19, s20, a20,
s21, a21, s22, a22, s23, a23, s24, a24, s25, a25, s26, a26, s27, a27, s28, a28, s29, a29, s30, a30,
s31, a31, s32, a32, s33, a33, s34, a34, s35, a35, s36, a36, s37, a37, s38, a38, s39, a39, s40, a40):
    id = x
    #이름 = fake.name()
    Q1 = random.randrange(s1, a1)
    Q2 = random.randrange(s2, a2)    
    Q3 = random.randrange(s3, a3)    
    Q4 = random.randrange(s4, a4)    
    Q5 = random.randrange(s5, a5)
    Q6 = random.randrange(s6, a6)    
    Q7 = random.randrange(s7, a7)
    Q8 = random.randrange(s8, a8)    
    Q9 = random.randrange(s9, a9)    
    Q10 = random.randrange(s10, a10)    
    Q11 = random.randrange(s11, a11)    
    Q12 = random.randrange(s12, a12)    
    Q13 = random.randrange(s13, a13)    
    Q14 = random.randrange(s14, a14)    
    Q15 = random.randrange(s15, a15)    
    Q16 = random.randrange(s16, a16)    
    Q17 = random.randrange(s17, a17)    
    Q18 = random.randrange(s18, a18)    
    Q19 = random.randrange(s19, a19)    
    Q20 = random.randrange(s20, a20)   
    Q21 = random.randrange(s21, a21)   
    Q22 = random.randrange(s22, a22)   
    Q23 = random.randrange(s23, a23)   
    Q24 = random.randrange(s24, a24)   
    Q25 = random.randrange(s25, a25)   
    Q26 = random.randrange(s26, a26)   
    Q27 = random.randrange(s27, a27)   
    Q28 = random.randrange(s28, a28)   
    Q29 = random.randrange(s29, a29)   
    Q30 = random.randrange(s30, a30)   
    Q31 = random.randrange(s31, a31)   
    Q32 = random.randrange(s32, a32)   
    Q33 = random.randrange(s33, a33)   
    Q34 = random.randrange(s34, a34)   
    Q35 = random.randrange(s35, a35)   
    Q36 = random.randrange(s36, a36)   
    Q37 = random.randrange(s37, a37)   
    Q38 = random.randrange(s38, a38)   
    Q39 = random.randrange(s39, a39)   
    Q40 = random.randrange(s40, a40)    
    
    
    data = [id, category, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, 
            Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20,
            Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30,
            Q31, Q32, Q33, Q34, Q35, Q36, Q37, Q38, Q39, Q40,]

    return data

def create_sample(count, category) :
    datas = []
    id = 1
    s1=s2=s3=s4=s5=s6=s7=s8=s9=s10=s11=s12=s13=s14=s15=s16=s17=s18=s19=s20=s21=s22=s23=s24=s25=s26=s27=s28=s29=s30=s31=s32=s33=s34=s35=s36=s37=s38=s39=s40=1
    a1=a2=a3=a4=a5=a6=a7=a8=a9=a10=a11=a12=a13=a14=a15=a16=a17=a18=a19=a20=a21=a22=a23=a24=a25=a26=a27=a28=a29=a30=a31=a32=a33=a34=a35=a36=a37=a38=a39=a40=8
    if(category == 'A'): # 대식가
        s1 = 6
        s2 = 6
        a22 = 2
    elif(category == 'B'): # 소식좌
        a1 = 2
        a2 = 2
        s15 = 6
        s25 = 4
    elif(category == 'C'): # 애주가
        s3 = 6
        s4 = 6
        s9 = 4
    elif(category == 'D'): # 개척자
        a5 = 3
        s28 = 3
        a28 = 6
        s35 = 6
        s39 = 6
    elif(category == 'E'): # 분석가
        s8 = 4
        s17 = 5
        s38 = 5
        s40 = 6
    elif(category == 'F'): # 인스타
        s6 = 6
        s7 = 6
        s23 = 4
        s32 = 5
        s34 = 5
    elif(category == 'G'): # 내신 1등
        s5 = 5
        s28 = 5
        a35 = 3
        s38 = 5
    elif(category == 'H'): # 푸드슈타인
        s11 = 4
        s30 = 4
        s32 = 6
        s35 = 5
    elif(category == 'I'): # 위장월세형
        s11 = 6
        s13 = 5
        s32 = 6
    elif(category == 'J'): # 위부장님
        s4 = 6
        s9 = 5
        s23 = 6
        a30 = 5
    elif(category == 'K'): # 앙드레 푸드
        a13 = 4
        s14 = 5
        s18 = 6
        s28 = 6
        s33 = 6
    elif(category == 'L'): # 스틸 통규씨
        s10 = 6
        a21 = 3
        s32 = 6
    elif(category == 'N'): # 헨젤이 그랬대
        s2 = 4
        s7 = 5
        a9 = 4
        s12 = 6
        s16 = 6
        s20 = 5
    elif(category == 'M'): # 포세이돈
        s4 = 4
        s9 = 4
        a22 = 5
        s26 = 6
        e31 = 5
        s36 = 6
    elif(category == 'O'): # 배달VVIP
        s13 = 6
        a14 = 5
        a18 = 5
        a22 = 5
        a23 = 5
        s32 = 5
        s37 = 6


    for x in range (count):
        datas.append(get_sample_data(id, category, s1, a1, s2, a2, s3, a3, s4, a4, s5, a5, s6, a6, s7, a7, s8, a8, s9, a9, s10, a10,
        s11, a11, s12, a12, s13, a13, s14, a14, s15, a15, s16, a16, s17, a17, s18, a18, s19, a19, s20, a20,
        s21, a21, s22, a22, s23, a23, s24, a24, s25, a25, s26, a26, s27, a27, s28, a28, s29, a29, s30, a30,
        s31, a31, s32, a32, s33, a33, s34, a34, s35, a35, s36, a36, s37, a37, s38, a38, s39, a39, s40, a40))
        id+= 1
    result = np.array(datas)
   #result = np.array(datas, dtype=np.int32)
    return result