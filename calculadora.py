def calcular():
    while True:
        operacao = input('''
Por favor digite a operação que você deseja completar:
    + para adição
    - para subtração
    / para divisão
    * para multiplicação
''')

        try:
            numero_1 = int(input('Insira um número: '))
            numero_2 = int(input('Insira mais um número: '))
        except ValueError:
            print("Entrada inválida. Por favor insira números inteiros.")
            continue

        if operacao == '+':
            print(numero_1 + numero_2)
            print('{} + {} = {}'.format(numero_1, numero_2, numero_1 + numero_2))

        elif operacao == '-':
            print(numero_1 - numero_2)
            print('{} - {} = {}'.format(numero_1, numero_2, numero_1 - numero_2))

        elif operacao == '/':
            try:
                resultado = numero_1 / numero_2
                print('{} / {} = {}'.format(numero_1, numero_2, resultado))
            except ZeroDivisionError:
                print("Erro! Não é possível dividir por zero.")

        elif operacao == '*':
            print(numero_1 * numero_2)
            print('{} * {} = {}'.format(numero_1, numero_2, numero_1 * numero_2))

        else:
            print('Você não inseriu uma operação valida.')

        calcular_novamente = input('''
Deseja calcular novamente?
Aperte S para SIM, ou, N para NÃO.
''')
        if calcular_novamente.upper() == "N":
            print('Até logo!')
            break


calcular()
