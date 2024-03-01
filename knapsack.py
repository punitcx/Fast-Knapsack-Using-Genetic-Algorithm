import random as r
p=eval(input("Enter profits list [] seperated by commas"))
w=eval(input("Enter Weights list [] seperated by commas"))
W=int(input("Enter Weight Capacity"))
l=len(p)
mr=0.5
n=100
fi=[]
pop=[]
g=0

def population(n):
	for i in range(n):
		t=[]
		for j in range(l):
			t.append(0) if r.random()>0.5 else t.append(1)
		pop.append(t)
	return pop

def fitness(pop):
	fi=[0]*len(pop)
	for cr in pop:
		s=0
		for k in range(l):
				s=s+cr[k]*p[k]
		fi[pop.index(cr)]=s
	return pop,fi

def selection(pop):
	newpop=[]
	for cr in pop:
		s=0
		for k in range(l):
				s=s+cr[k]*w[k]
		if(s<=9):
			newpop.append(cr)
	newpop,fi=fitness(newpop)
	return newpop,fi

def crossover(pop):
	cp=r.randint(1,6)
	for i in range(int(n/2)):
		p1=list(pop[r.randint(0,n-1)])
		p2=list(pop[r.randint(0,n-1)])
		p1[cp:],p2[cp:]=p2[cp:],p1[cp:]
		pop.append(p1)
		pop.append(p2)
	newpop,fi=fitness(pop)
	return newpop,fi
	
def mutation(pop):
	for i in range(int(mr*n)):
		bit=r.randint(0,6)
		p1=list(pop[r.randint(0,n-1)])
		if(p1[bit]==1):
			p1[bit]=0
		else:
			p1[bit]=1
		pop.append(p1)
	newpop,fi=fitness(pop)
	return newpop,fi

pop=population(n)
pop,fi=fitness(pop)
while g<5:
	#print(pop,fi)
	print('sel',pop,fi)
	n=len(pop)
	pop,fi=crossover(pop)
	print('cro',pop,fi)
	pop,fi=mutation(pop)
	print('mut',pop,fi)
	pop,fi=selection(pop)
	print('Generation:',g,'\n Best fitness: ',max(fi),' length: ',len(pop),'\n',fi,pop)
	g+=1
q=0
s=pop[fi.index(max(fi))]
for i in range(len(s)):
	q=q+s[i]*w[i]
print('sol',pop[fi.index(max(fi))],'profit:',max(fi),'wt',q)
