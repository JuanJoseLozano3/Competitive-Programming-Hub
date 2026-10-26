class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        mes = {"01":31, "02":28, "03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31}
        
        m = 1
        d = 1
        flagA = False
        flagB = False
        alice = set()
        bob = set()
        for i in range(1,366):
            me = str(m)
            di = str(d)
            if(len(me)==1):
                me = "0"+me
            if(len(di)==1):
                di = "0"+di
            if(me+"-"+di == arriveAlice):
                flagA = True
            if(me+"-"+di == arriveBob):
                flagB = True
                
            if(flagA):
                alice.add(i)
            if(flagB):
                bob.add(i)
                
            if(me+"-"+di == leaveAlice):
                flagA = False
            if(me+"-"+di == leaveBob):
                flagB = False
                
            d += 1
            if(mes[me]<d):
                d = 1
                m += 1
                
                
        return len(alice.intersection(bob))
            
        
        
        