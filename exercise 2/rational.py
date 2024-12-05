class Rational(object):
    def __init__(self,num,denum):
        # if denum==0:
        #    denum=1
        if denum==0:
            raise ValueError("Zero not allowed")
        self.num=num
        self.denum=denum
    def out(self):
        a=5
        b=5
        return a+b
    
    def __add__(self,other):
        if isinstance(other, Rational):
          new_num=(self.num*other.denum)+ (other.num*self.denum)
          new_denum=self.denum *other.denum
          return Rational(new_num,new_denum)
    def __sub__(self,other):
        new_num=(self.num*other.denum)- (other.num*self.denum)
        new_denum=self.denum *other.denum
        return Rational(new_num,new_denum)
    def __float__(self):
        return self.num/self.denum
    def __str__(self):
        # Return a string representation of the rational number in "numerator/denominator" format
        return f"{self.num}/{self.denum}"
c=1
r1=Rational(2,4)
r2=Rational(2,4)
print("Rationl 1 :", r1)
print("Rationl 1 :", r2)
r3 = r1 + r2
r4=r1-r2
float_r3=float(r3)
float_r4= float(r3)
if(float_r3 ==float_r4):
    print("Equal")
else:
    print("Not equal")
print(r3)
print(r4)
a=Rational(1,4)
k=a.out()+c
print(k)

        
        