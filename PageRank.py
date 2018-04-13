#!/usr/bin/env python3
#coding : utf-8


import numpy as np
import os

def VecteurPageRank(P,taille,e):
	#linalg.norm
	# pg = np.zeros(shape=(taille,taille));
	pg = np.full((1,taille) , 1/taille)
  
	while (True) :
		pgPlus1 = pg.dot(P)
		if (np.linalg.norm(pgPlus1-pg) >= e):
			pg = pgPlus1
			break
	pg=pgPlus1
	print(pg)


def transition(P, A,lam, e, taille):
	for i in range (taille):
		somme=A[i].sum()
		for j in range (taille):
			if somme == 0:
				P[i][j] = 1/taille
			else :
				P[i][j]= lam * (A[i][j]/somme) + (1-lam)*(1/taille)
	print(P)

def main():

	lam = 0.85
	e = 0.001
	file=open("small-graph.txt","r")
	f=file.readlines()
	l=[]
	for line in f:
		l.append((str(line)).replace("\n","").split(" "))
	taille = int(l[0][0])
	l.pop(0)
	A=np.zeros(shape=(taille,taille))
	P=np.zeros(shape=(taille,taille))
	
	for i in range (taille):
		t=len(l[i])
		for j in range (1,t):
			A[i][int(l[i][j])] = 1
	print(l)
	print(A)
	transition(P, A,lam,e, taille)
	VecteurPageRank(P,taille,e)
main()