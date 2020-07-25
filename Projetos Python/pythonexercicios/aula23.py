try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro:
    print(f'O problema encontrado foi {erro.__cause__}')

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que vc digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre!')