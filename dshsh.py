def skat(n):
    for i in n:
        yield i


def f_e(g,skat):
    while g > 0:
        e = next(skat)
        print(f'Первый сьел {e} и написал:',str(e))
        g -= 1

def s_e(g,skat):
    while g > 0:
        e = next(skat)
        print(f'Второй сьел {e} и написал:',str(e) * 4)
        g -= 1
def t_e(g,skat):
    while g > 0:
        e = next(skat)
        print(f'Третий сьел {e} и написал:',str(e)*10)
        g -= 1
sk_den = skat([1,2342,23,4235,2342,234234,2342,34234,234,234,234,23])
g1 = 2
g2 = 3
g3 = 4

try:
    f_e(g1,sk_den)
    s_e(g2,sk_den)
    t_e(g3,sk_den)
except StopIteration:
    print('Заряды закончились')
f_e(2,sk_den)