#주어진 str 에서 원하는 걸 파싱하는 연습
# str = 'X-DSPAM-Confidence: 0.8475'

str = 'X-DSPAM-Confidence: 0.8475'

a = str.find(' ')

##print (a)

##b = str[19: ]
##print (b)

## 문장에서 공백을 찾고 그 이후부터의 문자열을 출력함
print (str[a : ])

## 공백 말고  ':' 을 찾아서 그 후의 값을 출력

b = str.find(':')

print (str[b+2: ])


    
