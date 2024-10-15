# Importando bibliotecas
from PIL import Image

# Converte uma string para binário usando codificação ASCII
def textToBinary(text):
    return ''.join((format(ord(i), 'b')).zfill(8) for i in text)

# Solicitando ao usuário o arquivo de imagem para abrir
print('Digite o nome do arquivo de imagem para abrir:')
imgIn = input()
print('Digite o texto para codificar:')
textIn = input()
print('Digite o nome do arquivo de imagem para salvar:')
imgOut = input()

# Convertendo nossa mensagem para binário
messageBin = textToBinary(textIn)

# Carregando os dados dos pixels de uma imagem
img_pre = Image.open(imgIn)
width, height = img_pre.size
pixels = img_pre.load()

# Alterando o bit menos significativo de cada pixel para corresponder a cada bit da nossa mensagem codificada
currBit = 0
for x in range(0, width):
    if (currBit >= len(messageBin)):
        break

    # Obtendo o pixel atual
    currPix = pixels[x, 0]
    print('[%d, %d]: [%d, %d, %d]'%(x, 0, currPix[0], currPix[1], currPix[2]))

    # Alterando os valores r, g e b do pixel
    newPix = list(currPix)
    for c in range(0, 3):
        if (currBit >= len(messageBin)):
            break
        colorBin = list(format(currPix[c], 'b').zfill(8))
        colorBin[7] = messageBin[currBit]
        colorBin = ''.join(colorBin)
        newPix[c] = int(colorBin, 2)

        currBit += 1

    # Sobrescrevendo o pixel antigo
    currPix = tuple(newPix)
    pixels[x, 0] = currPix

    # Exibindo o pixel modificado
    print('  -> [%d, %d, %d]'%(currPix[0], currPix[1], currPix[2]))
    print('  (%c, %c, %c)'%(messageBin[currBit-3], messageBin[currBit-2], messageBin[currBit-1]))

# Reescrevendo os dados dos pixels da imagem para uma nova imagem
img_pre.save(imgOut)