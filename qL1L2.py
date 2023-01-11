L1 = [10,12,13,14,15,18,20]
#Lista L1
L2 = [10,12,14,18,21]
#Lista L2
for k in range(-1, -len(l1), -1):
	#len de Lista é ogual ao nº de itens
	if L1[k] in L2[-5:-2]:
		#L1[K] seria o item de L1
		#L2[-5:-2] pega uma fatia da Lista L2 e EXCLUSIVE o último termo citado. Neste caso, temos os seguintes itens dentro da fatia: -5 (10), -4 (12) e -3(14).
		print L1[K]