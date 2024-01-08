duljina = int(input())
shirochina=int(input())
visochina = int(input())
procent=float(input())
sm3=duljina*shirochina*visochina
litri=sm3*0.001
nlitri=litri*(1-procent/100)
print(nlitri)