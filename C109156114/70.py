de={"00":"0","01":"1","100":"2","101":"3","1100":"4","1101":"5","11100":"6","11101":"7","111100":"8","111101":"9"}
conv={"01":"D","02":"E","03":"F","04":"G","05":"H","06":"I","07":"J","08":"K","09":"L","10":"M","11":"N","12":"O","13":"P","14":"Q","15":"R","16":"S","17":"T","18":"U","19":"V","20":"W","21":"X","22":"Y","23":"Z","24":"A","25":"B","26":"C"}
s=input("輸入一串二進制的新編碼").split(" ")
sr1=""
sr1+=de.get(s[0])+de.get(s[1])
print(conv.get(sr1))
