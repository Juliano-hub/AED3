from Crypto.PublicKey import RSA
from sympy import mod_inverse

Chave_Publica = open("pub.key", "r")
Chave_Publica_RSA = RSA.importKey(Chave_Publica.read())

Chave_Publica.close()


#-------------------Valores para gerar a chave privada-------------------
# p e q gerados colocando o Chave_Publica_RSA.n em: https://www.alpertron.com.ar/ECM.HTM

e = Chave_Publica_RSA.e
p = 1332830227949273521465367319234277279439624789
q = 1371293089587387292180481293784036793076837889
n = p*q

Funcao_Totiente = ((p-1))*((q-1))

d = mod_inverse(e, Funcao_Totiente)

#-------------------Geração da chave-------------------

Chave_Privada_Construida = RSA.construct((int(n),int(e),int(d),int(p),int(q)))

#-------------------Salvando a chave em um arquivo com extensão .key-------------------

Salvar = open('ChavePrivadaGerada.key','wb')
Salvar.write(Chave_Privada_Construida.export_key('PEM'))
Salvar.close()