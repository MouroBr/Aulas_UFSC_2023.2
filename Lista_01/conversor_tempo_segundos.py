dias, horas, minutos, segundo = input('Digite os valores para dias, horas, minutos e segundos: '). split()
dias = int(dias)
horas = int(horas)
minutos = int(minutos)
segundo = int(segundo)

total_segundos = (((dias * 24) * 60) * 60) + ((horas * 60) * 60) + (minutos * 60) + segundo

print(f'O total de segundo de {dias}dias, {horas}horas, {minutos}minutos, {segundo}segundo é : {total_segundos}s')

