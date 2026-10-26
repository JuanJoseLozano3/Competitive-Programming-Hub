class Solution:
    def restoreIpAddresses(self, co: str) -> list[str]:
        sol = []
        tam = len(co)
        dig1 = 0
        for p in range(0,3):
            if(p+4>tam):
                break
            num1 = int(co[0:p+1])
            dig1 += 1
            dig2 = 0
            if(len(str(num1))!=dig1 or num1>255):
                break
            for s in range(p+1,p+4):
                if(s+3>tam):
                    break
                dig2 += 1
                num2 = int(co[p+1:s+1])
                if(len(str(num2))!=dig2 or num2>255):
                    break
                dig3 = 0
                for t in range(s+1,s+4):
                    if(t+2>tam):
                        break
                    dig3+= 1
                    num3 = int(co[s+1:t+1])
                    if(len(str(num3))!=dig3 or num3>255):
                        break
                    dig4 = 0
                    for q in range(t+1,t+4):
                        dig4+= 1
                        if(q+1<tam):
                            continue
                        elif(q+1>tam):
                            break
                        num4 = int(co[t+1:q+1])
                        if(len(str(num4))!=dig4 or num4>255):
                            break
                        sol.append(str(num1)+"."+str(num2)+"."+str(num3)+"."+str(num4))
        return sol
        