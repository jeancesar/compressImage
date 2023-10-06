from PIL import Image

folder = 'src/images/'
file = 'carro.jpg'

def getArrayFromString(value, splitValue):
      return value.split(splitValue)

def getNewFilename(image:Image) -> str: 
        valuesFilename = getArrayFromString(image.filename, "/")
        tempFilename = valuesFilename[len(valuesFilename)-1]
        valuesTempFilename = getArrayFromString(tempFilename, ".")
        newFilename = valuesTempFilename[0]+'-new.jpg'
        return folder+newFilename

def compressImage():
    # Abra a imagem
    sourceImage = Image.open(folder+file)
    # Copie a imagem para remover os metadados
    newImage = sourceImage.copy()
    # Remova os metadados
    newImage.info = {}
    # Especifique a qualidade desejada (0 a 100, onde 100 é a melhor qualidade)
    qualidade = 50
    if sourceImage.format != 'JPEG':
        newImage = newImage.convert("RGB")

    # Salve a imagem comprimida em um novo arquivo
    newImage = newImage.resize(sourceImage.size, Image.LANCZOS)
    newImage.save(getNewFilename(sourceImage), 'JPEG', optimize=True, quality=qualidade)
    # Feche a imagem original e nova
    sourceImage.close()
    newImage.close()

compressImage()