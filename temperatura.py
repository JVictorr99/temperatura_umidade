         # versao simples (questao)



# temperatura = 32
# umidade = 19
# if temperatura > 30 and umidade < 20:
#    print("ALERTA possivel alerta de queimada!")
# else:
#    print("Nada a se preocupar.")
 
 
    
         # versao melhorada
 
 
 
# temperatura = float(input("Qual e a temperatura atual: "))
# umidade = float(input("Umidade atual do AR: "))
# temperatura_alta = 35
# umidade_maxima = 20

# if temperatura >= temperatura_alta and umidade <= umidade_maxima:
#    print("ALERTA! Possível alerta de queimada.")
# else:
#    print("Nada a se preocupar.")
    
    
         # versao modificada
    
temperatura = float(input("Qual e a temperatura atual: "))
umidade = float(input("Umidade atual do AR: "))
temperatura_alta = 35
umidade_minima = 20
if temperatura >= temperatura_alta and umidade <= umidade_minima:
    print("ALERTA! Possível queimada na Região.")
elif temperatura <= temperatura_alta and umidade >= 80:
    print("Possível ALERTA de chuva!")
else:
    print("Nada a se preocupar.")
    
