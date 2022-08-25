import math

class Angle:
	def __init__(self,number):
		self.num=number
		self.cut()
	def cut(self):
		self.num/=360
		self.num-=int(self.num)
		if self.num <0: self.num=1+self.num
		self.num*=360	
	def __add__(self,second):
		ret=Angle(second.num)
		ret.num+=self.num
		ret.cut()
		return ret
	def __sub__(self,second):
		ret=Angle(second.num)
		ret.num=self.num-ret.num
		ret.cut()
		return ret
	def __repr__(self):
		return "Angle ("+str(self.num)+"°)"
		
#------------------------------------

def bounds2vec(bounds):
    x=bounds[0]
    y=bounds[1]
    
    if x==0 and y>=0: direction=Angle(0)
    elif x==0 and y<0: direction=Angle(180)
    elif y==0 and x>0: direction=Angle(90)
    elif y==0 and x<0: direction=Angle(270)
    elif y > 0: direction=Angle(math.degrees(math.atan(x/y)))
    elif y < 0: direction=Angle(math.degrees(math.atan(x/y)))+Angle(180)
    return direction,math.sqrt(x**2+y**2)

def list2vector(arr):
	last_hypot=arr[0]
	di_arr=[]
	for i in range(len(arr)-1):
		d,last_hypot=bounds2vec([last_hypot,arr[i+1]])
		di_arr.append(d)
	return di_arr,last_hypot
	
#------------------------------------
	
def vec2arr(vec):
	vec.reverse()
	x=vec[0]
	vec.pop(0)
	bag=[]
	for i in vec:
		x,y=vec2bounds([i,x])
		bag.append(y)
	bag.append(x)
	return list(reversed(bag))
	
def vec2bounds(vec):
	d=vec[0].num
	l=vec[1]
	x=math.sin(math.radians(d))*l
	y=math.cos(math.radians(d))*l
	return x,y

#------------------------------------
	
def sum_arr(arr1,arr2):
	ml=max(len(arr1),len(arr2))
	arr1+=[0]*(ml-len(arr1))
	arr2+=[0]*(ml-len(arr2))
	for i in range(ml):
		arr1[i]+=arr2[i]
	return arr1
	
def sub_arr(arr1,arr2):
	ml=max(len(arr1),len(arr2))
	arr1+=[0]*(ml-len(arr1))
	arr2+=[0]*(ml-len(arr2))
	for i in range(ml):
		arr1[i]=arr1[i]-arr2[i]
	return arr1
	
#------------------------------------
	
class Vector:
	def __init__(self,list=None,angles=None,len=None):
		assert not (len==None and angles==None and list==None)
		if list!=None: self.angles,self.len=list2vector(list)
		if angles!=None:
			self.angles=angles
		if len!=None:
			self.len=len
	def __add__(self,second):
		
		ar1=vec2arr(self.angles+[self.len])
		ar2=vec2arr(second.angles+[second.len])
		ar1=sum_arr(ar1,ar2)
		return Vector(ar1)
	def __sub__(self,second):
		
		ar1=vec2arr(self.angles+[self.len])
		ar2=vec2arr(second.angles+[second.len])
		ar1=sub_arr(ar1,ar2)
		return Vector(ar1)
	def __mul__(self,num):
		new=self
		new.len*=num
		return new
	def __truediv__(self,num):
		new=self
		new.len/=num
		return new
	def __repr__(self):
		return str(len(self.angles)+1)+"d Vector with len "+str(self.len)+" and directions:\n"+str(self.angles)
	def __iter__(self):
		return iter(vec2arr(self.angles+[self.len]))
