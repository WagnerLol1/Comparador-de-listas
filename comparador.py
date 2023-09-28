# Ler o conteúdo da Lista A e Lista B
with open('Seguir editando.txt', 'r', encoding='utf-8') as arquivo_a, open('teste.txt', 'r', encoding='utf-8') as arquivo_b:
    lista_completa = arquivo_a.read()
    lista_vazia = arquivo_b.read()

# Dividir os parágrafos em ambas as listas
lista_completa = lista_completa.split('\n\n')
lista_vazia = lista_vazia.split('\n\n')

resgitros_novos={}
for p in lista_completa:
    info = p.split('CPF')
    try:
        news = info[1]
        olds = info[0]
        index = 0
        if len(olds.split(',')[1].split(' ')[5]) == 11:
            index = 5
        else:
            index = 4
        resgitros_novos[f"{olds.split(',')[0]},{olds.split(',')[1].split(' ')[index]}"] = news
    except:
        continue
    # olds.split(',')[0]},

resgitros_velhos={}
for n,p in enumerate(lista_vazia):
    info = p.split(',')
    nome = info[0]
    lista = info[1].split(' ')
    for i in lista:
        if len(i) == 11:
            cnh = i
    key = f'{nome},{cnh}'
    resgitros_velhos[n] = key

concat = []
for key, item in resgitros_velhos.items():
        print(item)
        concat.append(key, resgitros_novos[item])
    #except:
        continue

for item in concat:
    lista_vazia[item[0]].append(item[1])

texto = ''
for item in lista_vazia:
    texto += item+'\n\n'

# Unir os parágrafos e salvar a nova Lista B

with open('teste cheio.txt', 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(texto)
