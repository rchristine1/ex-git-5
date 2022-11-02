# lire les nombres d'un tableau et calculer la moyenne puis la retourner
def moyenne(L):
 m=0
 for i in L:
  a=i//len(L)
  m += a
  print(i,a,m)
 return (m)
