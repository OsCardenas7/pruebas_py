from random import randint

s = "1000	1987	1988	1989	1990	1991	1992	1993	1994	1995	1996	1997	1998	1999	2000	2001	2002	2003	2004	2005	2006	2007	2008	2009	2010	2011	2012	2013	2014	2015	2016    2017"
x = s.split()

c = 0
r = ""
while r != "2017":
    r = x[randint(0,len(x)-1)]
    c+=1

print(r, " salio en el intento: ", c)


#radnint() numero randnom integer
#uniform() numero random decimal
#random() numero aleatorio entre 0 y 1



