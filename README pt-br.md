# Password Generator 0.5

## Como o programa funciona

É bem simples, como o próprio nome sugere: ele gera uma senha para você! Você pode personalizar seu tamanho e escolher se deseja incluir letras e caracteres especiais.

Você pode ter uma senha com números e letras, mas sem caracteres especiais, por exemplo. Entretanto, os números são a única opção não personalizável aqui, pois são uma **PRIORIDADE**.

Também temos mais funcionalidades planejadas, como salvar senhas, mas elas ainda estão em desenvolvimento.

## Sobre o código

A primeira coisa que quero mostrar aqui é esta parte:

```python
def get_option():
    option = int(input(" +- Option: "))

    if option < 1 or option > 4:
        raise ValueError

    return option

try:
    in_option = get_option()
except ValueError:
```

Eu simplesmente percebi que estava repetindo essa lógica de validação muitas vezes, então transformei isso em uma função que faz exatamente a mesma coisa. Agora não preciso reescrever essa lógica toda vez, porque já temos uma função para isso!

Agora, vamos falar sobre a parte principal do código: a geração de senhas.

```python
# Password generation logic
def generate_password(interface):
    # Get all numbers as a string
    numbers = string.digits

    # Get lowercase and uppercase letters and merge them
    alpha_lower = string.ascii_lowercase
    alpha_upper = alpha_lower.upper()
    alpha = alpha_lower + alpha_upper

    # Get all punctuation characters as a string
    punctuations = string.punctuation

    # Put everything together
    everything = numbers

    if interface.alphabet_stats:
        everything += alpha

    if interface.punctuations_stats:
        everything += punctuations

    # Generate
    interface.set_password("".join(
        choice(everything)
        for _ in range(interface.password_size)
    ))
```

Isso foi bem simples! Importei `string` e `choice` de `secrets` (que é mais seguro para geração de senhas do que utilizar `random.choice`). Usei `string` para obter os números, caracteres de pontuação (caracteres especiais) e o alfabeto inteiro, sem precisar escrever tudo manualmente.

Depois, juntei tudo com base nas configurações de alfabeto e pontuação armazenadas na interface.

Por fim, temos a parte da geração. Eu poderia retornar a senha em vez de armazená-la diretamente na interface e salvá-la posteriormente. Isso provavelmente seria mais limpo e apropriado, já que é melhor quando uma função possui apenas uma responsabilidade clara.

```python
if in_option == 1:
    generate_password(interface)

space()
interface.display_password_generated()

try:
    in_option = get_option()
except ValueError:
    interface.display_invalid_option()
    in_option = None

if in_option != None:
    match in_option:
        case 1: # Generate
            pass
        case 2: # Copy
            pyperclip.copy(interface.password)
        case 3: # Exit
            break
        case _:
            interface.display_invalid_option()
```

Dessa vez, no menu principal, não utilizei `while True` para validar a opção. Quando a entrada gera um `ValueError`, o bloco `except` utiliza `continue` para nos enviar de volta ao início do loop. Entretanto, não precisamos disso novamente nas outras partes do código.

Para as opções, estou utilizando `match/case`. Acho que é uma escolha melhor para essa situação e deixa o código mais claro.
