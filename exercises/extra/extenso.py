def decomp(num):
    """decomp(120) == (100, 20)"""
    if num < 20:
        return num, 0
    else:        
        base = 10 ** (len(str(num))-1)
        divisor, resto = divmod(num, base)
        return divisor * base, resto


def radicais(resto):
    while resto > 0:
        base, resto = decomp(resto)
        yield base


def escalas(base):
    while base > 0:
        base, resto = divmod(base, 1000)
        yield resto

        
def extenso(num):
    d = {
        1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 
        6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove',
        10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze', 
        16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove',
        20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 
        60: 'sessenta', 70: 'setenta', 80: 'oitenta', 90: 'noventa',
        100: 'cento', 200: 'duzentos', 300: 'trezentos', 400: 'quatrocentos',
        500: 'quinhentos', 600: 'seissentos', 700: 'setecentos', 800: 'oitocentos', 
        900: 'novecentos',
    }
    
    g = {0: '', 1: ' mil',}

    if num == 0:
        return 'zero'

    def _extenso(num):
        if num == 100:
            return 'cem'

        return ' e '.join((d[r] for r in radicais(num)))

    res = []
    l = [e for e in escalas(num)]
    for i, a in enumerate(l):
        if a > 0:
            res.append(_extenso(a) + g[i])
    res = res[::-1]
    
    return ' e '.join(r for r in res)

if __name__ == '__main__':
    assert extenso(0) == 'zero'
    assert extenso(1) == 'um'
    assert extenso(2) == 'dois'
    assert extenso(3) == 'três'
    assert extenso(4) == 'quatro'
    assert extenso(5) == 'cinco'
    assert extenso(6) == 'seis'
    assert extenso(7) == 'sete'
    assert extenso(8) == 'oito'
    assert extenso(9) == 'nove'

    assert extenso(10) == 'dez'
    assert extenso(11) == 'onze'
    assert extenso(14) == 'quatorze'
    assert extenso(17) == 'dezessete'

    assert extenso(20) == 'vinte'
    assert extenso(21) == 'vinte e um'
    assert extenso(23) == 'vinte e três'
    assert extenso(27) == 'vinte e sete'

    assert extenso(90) == 'noventa'
    assert extenso(95) == 'noventa e cinco'
    assert extenso(99) == 'noventa e nove'

    assert extenso(100) == 'cem'
    assert extenso(101) == 'cento e um'
    assert extenso(121) == 'cento e vinte e um'
    assert extenso(174) == 'cento e setenta e quatro'
    assert extenso(463) == 'quatrocentos e sessenta e três'
    assert extenso(983) == 'novecentos e oitenta e três'
    
    assert extenso(1000) == 'um mil'
    assert extenso(1001) == 'um mil e um'
    assert extenso(1002) == 'um mil e dois'

    assert extenso(2000) == 'dois mil'
    assert extenso(2485) == 'dois mil e quatrocentos e oitenta e cinco'

    assert extenso(3000) == 'três mil'
    assert extenso(3485) == 'três mil e quatrocentos e oitenta e cinco'

    assert extenso(10000) == 'dez mil'
    assert extenso(100000) == 'cem mil'
    assert extenso(194567) == 'cento e noventa e quatro mil e quinhentos e sessenta e sete'

    print('fim')