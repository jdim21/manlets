from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS

def drawBaseType(im, colorPrimary, colorShade, colorLight, colorBrows, isGhost=False):
    imNew = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    colorBlack = colorsDict["black"]
    colorWhite = colorsDict["white"]
    colorTongue = colorsDict["tongue"]
    if isGhost:
        colorBlack = (0, 0, 0, 128)
        colorWhite = (255, 255, 255, 128)
        colorTongue = colorsDict["tongue"] + (128,)


    imNew.putpixel((14, 10), colorBlack)
    imNew.putpixel((15, 10), colorBlack)
    imNew.putpixel((16, 10), colorBlack)
    imNew.putpixel((17, 10), colorBlack)

    imNew.putpixel((12, 11), colorBlack)
    imNew.putpixel((13, 11), colorBlack)
    imNew.putpixel((14, 11), colorShade)
    imNew.putpixel((15, 11), colorShade)
    imNew.putpixel((16, 11), colorShade)
    imNew.putpixel((17, 11), colorShade)
    imNew.putpixel((18, 11), colorBlack)
    imNew.putpixel((19, 11), colorBlack)

    imNew.putpixel((11, 12), colorBlack)
    imNew.putpixel((12, 12), colorShade)
    imNew.putpixel((13, 12), colorShade)
    imNew.putpixel((14, 12), colorPrimary)
    imNew.putpixel((15, 12), colorPrimary)
    imNew.putpixel((16, 12), colorPrimary)
    imNew.putpixel((17, 12), colorPrimary)
    imNew.putpixel((18, 12), colorShade)
    imNew.putpixel((19, 12), colorShade)
    imNew.putpixel((20, 12), colorBlack)

    imNew.putpixel((10, 13), colorBlack)
    imNew.putpixel((11, 13), colorShade)
    imNew.putpixel((12, 13), colorPrimary)
    imNew.putpixel((13, 13), colorPrimary)
    imNew.putpixel((14, 13), colorPrimary)
    imNew.putpixel((15, 13), colorPrimary)
    imNew.putpixel((16, 13), colorLight)
    imNew.putpixel((17, 13), colorLight)
    imNew.putpixel((18, 13), colorPrimary)
    imNew.putpixel((19, 13), colorPrimary)
    imNew.putpixel((20, 13), colorShade)
    imNew.putpixel((21, 13), colorBlack)

    imNew.putpixel((9, 14), colorBlack)
    imNew.putpixel((10, 14), colorShade)
    imNew.putpixel((11, 14), colorPrimary)
    imNew.putpixel((12, 14), colorPrimary)
    imNew.putpixel((13, 14), colorPrimary)
    imNew.putpixel((14, 14), colorPrimary)
    imNew.putpixel((15, 14), colorLight)
    imNew.putpixel((16, 14), colorLight)
    imNew.putpixel((17, 14), colorLight)
    imNew.putpixel((18, 14), colorLight)
    imNew.putpixel((19, 14), colorPrimary)
    imNew.putpixel((20, 14), colorPrimary)
    imNew.putpixel((21, 14), colorShade)
    imNew.putpixel((22, 14), colorBlack)

    imNew.putpixel((9, 15), colorBlack)
    imNew.putpixel((10, 15), colorShade)
    imNew.putpixel((11, 15), colorPrimary)
    imNew.putpixel((12, 15), colorWhite)
    imNew.putpixel((13, 15), colorBlack)
    imNew.putpixel((14, 15), colorPrimary)
    imNew.putpixel((15, 15), colorLight)
    imNew.putpixel((16, 15), colorLight)
    imNew.putpixel((17, 15), colorLight)
    imNew.putpixel((18, 15), colorWhite)
    imNew.putpixel((19, 15), colorBlack)
    imNew.putpixel((20, 15), colorPrimary)
    imNew.putpixel((21, 15), colorShade)
    imNew.putpixel((22, 15), colorBlack)

    imNew.putpixel((8, 16), colorBlack)
    imNew.putpixel((9, 16), colorShade)
    imNew.putpixel((10, 16), colorPrimary)
    imNew.putpixel((11, 16), colorPrimary)
    imNew.putpixel((12, 16), colorBlack)
    imNew.putpixel((13, 16), colorBlack)
    imNew.putpixel((14, 16), colorPrimary)
    imNew.putpixel((15, 16), colorPrimary)
    imNew.putpixel((16, 16), colorLight)
    imNew.putpixel((17, 16), colorLight)
    imNew.putpixel((18, 16), colorBlack)
    imNew.putpixel((19, 16), colorBlack)
    imNew.putpixel((20, 16), colorPrimary)
    imNew.putpixel((21, 16), colorPrimary)
    imNew.putpixel((22, 16), colorShade)
    imNew.putpixel((23, 16), colorBlack)

    imNew.putpixel((8, 17), colorBlack)
    imNew.putpixel((9, 17), colorShade)
    imNew.putpixel((10, 17), colorPrimary)
    imNew.putpixel((11, 17), colorPrimary)
    imNew.putpixel((12, 17), colorBlack)
    imNew.putpixel((13, 17), colorBlack)
    imNew.putpixel((14, 17), colorPrimary)
    imNew.putpixel((15, 17), colorPrimary)
    imNew.putpixel((16, 17), colorPrimary)
    imNew.putpixel((17, 17), colorPrimary)
    imNew.putpixel((18, 17), colorBlack)
    imNew.putpixel((19, 17), colorBlack)
    imNew.putpixel((20, 17), colorPrimary)
    imNew.putpixel((21, 17), colorPrimary)
    imNew.putpixel((22, 17), colorShade)
    imNew.putpixel((23, 17), colorBlack)

    imNew.putpixel((8, 18), colorBlack)
    imNew.putpixel((9, 18), colorShade)
    imNew.putpixel((10, 18), colorPrimary)
    imNew.putpixel((11, 18), colorsDict["blobBlush"])
    imNew.putpixel((12, 18), colorsDict["blobBlush"])
    imNew.putpixel((13, 18), colorPrimary)
    imNew.putpixel((14, 18), colorPrimary)
    imNew.putpixel((15, 18), colorPrimary)
    imNew.putpixel((16, 18), colorPrimary)
    imNew.putpixel((17, 18), colorPrimary)
    imNew.putpixel((18, 18), colorPrimary)
    imNew.putpixel((19, 18), colorsDict["blobBlush"])
    imNew.putpixel((20, 18), colorsDict["blobBlush"])
    imNew.putpixel((21, 18), colorPrimary)
    imNew.putpixel((22, 18), colorShade)
    imNew.putpixel((23, 18), colorBlack)

    imNew.putpixel((8, 19), colorBlack)
    imNew.putpixel((9, 19), colorShade)
    imNew.putpixel((10, 19), colorPrimary)
    imNew.putpixel((11, 19), colorPrimary)
    imNew.putpixel((12, 19), colorPrimary)
    imNew.putpixel((13, 19), colorPrimary)
    imNew.putpixel((14, 19), colorPrimary)
    imNew.putpixel((15, 19), colorBlack)
    imNew.putpixel((16, 19), colorBlack)
    imNew.putpixel((17, 19), colorPrimary)
    imNew.putpixel((18, 19), colorPrimary)
    imNew.putpixel((19, 19), colorPrimary)
    imNew.putpixel((20, 19), colorPrimary)
    imNew.putpixel((21, 19), colorPrimary)
    imNew.putpixel((22, 19), colorShade)
    imNew.putpixel((23, 19), colorBlack)

    imNew.putpixel((9, 20), colorBlack)
    imNew.putpixel((10, 20), colorShade)
    imNew.putpixel((11, 20), colorPrimary)
    imNew.putpixel((12, 20), colorPrimary)
    imNew.putpixel((13, 20), colorPrimary)
    imNew.putpixel((14, 20), colorPrimary)
    imNew.putpixel((15, 20), colorPrimary)
    imNew.putpixel((16, 20), colorPrimary)
    imNew.putpixel((17, 20), colorPrimary)
    imNew.putpixel((18, 20), colorPrimary)
    imNew.putpixel((19, 20), colorPrimary)
    imNew.putpixel((20, 20), colorPrimary)
    imNew.putpixel((21, 20), colorShade)
    imNew.putpixel((22, 20), colorBlack)

    imNew.putpixel((10, 21), colorBlack)
    imNew.putpixel((11, 21), colorShade)
    imNew.putpixel((12, 21), colorShade)
    imNew.putpixel((13, 21), colorShade)
    imNew.putpixel((14, 21), colorShade)
    imNew.putpixel((15, 21), colorShade)
    imNew.putpixel((16, 21), colorShade)
    imNew.putpixel((17, 21), colorShade)
    imNew.putpixel((18, 21), colorShade)
    imNew.putpixel((19, 21), colorShade)
    imNew.putpixel((20, 21), colorShade)
    imNew.putpixel((21, 21), colorBlack)

    imNew.putpixel((11, 22), colorBlack)
    imNew.putpixel((12, 22), colorBlack)
    imNew.putpixel((13, 22), colorBlack)
    imNew.putpixel((14, 22), colorBlack)
    imNew.putpixel((15, 22), colorBlack)
    imNew.putpixel((16, 22), colorBlack)
    imNew.putpixel((17, 22), colorBlack)
    imNew.putpixel((18, 22), colorBlack)
    imNew.putpixel((19, 22), colorBlack)
    imNew.putpixel((20, 22), colorBlack)

    if colorPrimary == colorsDict["blobRose"]:
        imNew.putpixel((11, 18), colorsDict["blobRoseBlush"])
        imNew.putpixel((12, 18), colorsDict["blobRoseBlush"])
        imNew.putpixel((19, 18), colorsDict["blobRoseBlush"])
        imNew.putpixel((20, 18), colorsDict["blobRoseBlush"])
    # imNew.putpixel((5, 6), colorBlack)
    # imNew.putpixel((6, 6), colorsDict[colorPrimary])
    # imNew.putpixel((7, 6), colorBlack)
    # imNew.putpixel((16, 6), colorBlack)
    # imNew.putpixel((17, 6), colorsDict[colorPrimary])
    # imNew.putpixel((18, 6), colorBlack)

    # imNew.putpixel((5, 7), colorBlack)
    # imNew.putpixel((6, 7), colorsDict[colorLight])
    # imNew.putpixel((7, 7), colorsDict[colorPrimary])
    # imNew.putpixel((8, 7), colorBlack)
    # imNew.putpixel((10, 7), colorBlack)
    # imNew.putpixel((11, 7), colorBlack)
    # imNew.putpixel((12, 7), colorBlack)
    # imNew.putpixel((13, 7), colorBlack)
    # imNew.putpixel((15, 7), colorBlack)
    # imNew.putpixel((16, 7), colorsDict[colorPrimary])
    # imNew.putpixel((17, 7), colorsDict[colorLight])
    # imNew.putpixel((18, 7), colorBlack)

    # imNew.putpixel((5, 8), colorBlack)
    # imNew.putpixel((6, 8), colorsDict[colorLight])
    # imNew.putpixel((7, 8), colorsDict[colorPrimary])
    # imNew.putpixel((8, 8), colorBlack)
    # imNew.putpixel((9, 8), colorBlack)
    # imNew.putpixel((10, 8), colorsDict[colorPrimary])
    # imNew.putpixel((11, 8), colorsDict[colorPrimary])
    # imNew.putpixel((12, 8), colorsDict[colorPrimary])
    # imNew.putpixel((13, 8), colorsDict[colorPrimary])
    # imNew.putpixel((14, 8), colorBlack)
    # imNew.putpixel((15, 8), colorBlack)
    # imNew.putpixel((16, 8), colorsDict[colorPrimary])
    # imNew.putpixel((17, 8), colorsDict[colorLight])
    # imNew.putpixel((18, 8), colorBlack)

    # imNew.putpixel((5, 9), colorBlack)
    # imNew.putpixel((6, 9), colorsDict[colorPrimary])
    # imNew.putpixel((7, 9), colorBlack)
    # imNew.putpixel((8, 9), colorsDict[colorPrimary])
    # imNew.putpixel((9, 9), colorsDict[colorPrimary])
    # imNew.putpixel((10, 9), colorsDict[colorPrimary])
    # imNew.putpixel((11, 9), colorsDict[colorPrimary])
    # imNew.putpixel((12, 9), colorsDict[colorPrimary])
    # imNew.putpixel((13, 9), colorsDict[colorPrimary])
    # imNew.putpixel((14, 9), colorsDict[colorPrimary])
    # imNew.putpixel((15, 9), colorsDict[colorPrimary])
    # imNew.putpixel((16, 9), colorBlack)
    # imNew.putpixel((17, 9), colorsDict[colorPrimary])
    # imNew.putpixel((18, 9), colorBlack)

    # imNew.putpixel((5, 10), colorBlack)
    # imNew.putpixel((6, 10), colorBlack)
    # imNew.putpixel((7, 10), colorsDict[colorPrimary])
    # imNew.putpixel((8, 10), colorsDict[colorBrows])
    # imNew.putpixel((9, 10), colorsDict[colorPrimary])
    # imNew.putpixel((10, 10), colorsDict[colorPrimary])
    # imNew.putpixel((11, 10), colorsDict[colorPrimary])
    # imNew.putpixel((12, 10), colorsDict[colorPrimary])
    # imNew.putpixel((13, 10), colorsDict[colorPrimary])
    # imNew.putpixel((14, 10), colorsDict[colorPrimary])
    # imNew.putpixel((15, 10), colorsDict[colorBrows])
    # imNew.putpixel((16, 10), colorsDict[colorPrimary])
    # imNew.putpixel((17, 10), colorBlack)
    # imNew.putpixel((18, 10), colorBlack)

    # imNew.putpixel((5, 11), colorBlack)
    # imNew.putpixel((6, 11), colorsDict[colorPrimary])
    # imNew.putpixel((7, 11), colorsDict[colorPrimary])
    # imNew.putpixel((8, 11), colorsDict[colorPrimary])
    # imNew.putpixel((9, 11), colorsDict[colorPrimary])
    # imNew.putpixel((10, 11), colorsDict[colorPrimary])
    # imNew.putpixel((11, 11), colorsDict[colorPrimary])
    # imNew.putpixel((12, 11), colorsDict[colorPrimary])
    # imNew.putpixel((13, 11), colorsDict[colorPrimary])
    # imNew.putpixel((14, 11), colorsDict[colorPrimary])
    # imNew.putpixel((15, 11), colorsDict[colorPrimary])
    # imNew.putpixel((16, 11), colorsDict[colorPrimary])
    # imNew.putpixel((17, 11), colorsDict[colorPrimary])
    # imNew.putpixel((18, 11), colorBlack)

    # imNew.putpixel((5, 12), colorBlack)
    # imNew.putpixel((6, 12), colorsDict[colorPrimary])
    # imNew.putpixel((7, 12), colorsDict[colorPrimary])
    # imNew.putpixel((8, 12), colorWhite)
    # imNew.putpixel((9, 12), colorBlack)
    # imNew.putpixel((10, 12), colorsDict[colorPrimary])
    # imNew.putpixel((11, 12), colorsDict[colorPrimary])
    # imNew.putpixel((12, 12), colorsDict[colorPrimary])
    # imNew.putpixel((13, 12), colorsDict[colorPrimary])
    # imNew.putpixel((14, 12), colorWhite)
    # imNew.putpixel((15, 12), colorBlack)
    # imNew.putpixel((16, 12), colorsDict[colorPrimary])
    # imNew.putpixel((17, 12), colorsDict[colorPrimary])
    # imNew.putpixel((18, 12), colorBlack)

    # imNew.putpixel((4, 13), colorBlack)
    # imNew.putpixel((5, 13), colorWhite)
    # imNew.putpixel((6, 13), colorWhite)
    # imNew.putpixel((7, 13), colorsDict[colorPrimary])
    # imNew.putpixel((8, 13), colorBlack)
    # imNew.putpixel((9, 13), colorBlack)
    # imNew.putpixel((10, 13), colorsDict[colorPrimary])
    # imNew.putpixel((11, 13), colorsDict[colorPrimary])
    # imNew.putpixel((12, 13), colorsDict[colorPrimary])
    # imNew.putpixel((13, 13), colorsDict[colorPrimary])
    # imNew.putpixel((14, 13), colorBlack)
    # imNew.putpixel((15, 13), colorBlack)
    # imNew.putpixel((16, 13), colorsDict[colorPrimary])
    # imNew.putpixel((17, 13), colorWhite)
    # imNew.putpixel((18, 13), colorWhite)
    # imNew.putpixel((19, 13), colorBlack)

    # imNew.putpixel((4, 14), colorBlack)
    # imNew.putpixel((5, 14), colorWhite)
    # imNew.putpixel((6, 14), colorWhite)
    # imNew.putpixel((7, 14), colorWhite)
    # imNew.putpixel((8, 14), colorWhite)
    # imNew.putpixel((9, 14), colorWhite)
    # imNew.putpixel((10, 14), colorWhite)
    # imNew.putpixel((11, 14), colorBlack)
    # imNew.putpixel((12, 14), colorBlack)
    # imNew.putpixel((13, 14), colorWhite)
    # imNew.putpixel((14, 14), colorWhite)
    # imNew.putpixel((15, 14), colorWhite)
    # imNew.putpixel((16, 14), colorWhite)
    # imNew.putpixel((17, 14), colorWhite)
    # imNew.putpixel((18, 14), colorWhite)
    # imNew.putpixel((19, 14), colorBlack)

    # imNew.putpixel((4, 15), colorBlack)
    # imNew.putpixel((5, 15), colorWhite)
    # imNew.putpixel((6, 15), colorWhite)
    # imNew.putpixel((7, 15), colorWhite)
    # imNew.putpixel((8, 15), colorWhite)
    # imNew.putpixel((9, 15), colorBlack)
    # imNew.putpixel((10, 15), colorWhite)
    # imNew.putpixel((11, 15), colorBlack)
    # imNew.putpixel((12, 15), colorBlack)
    # imNew.putpixel((13, 15), colorWhite)
    # imNew.putpixel((14, 15), colorBlack)
    # imNew.putpixel((15, 15), colorWhite)
    # imNew.putpixel((16, 15), colorWhite)
    # imNew.putpixel((17, 15), colorWhite)
    # imNew.putpixel((18, 15), colorWhite)
    # imNew.putpixel((19, 15), colorBlack)

    # imNew.putpixel((5, 16), colorBlack)
    # imNew.putpixel((6, 16), colorWhite)
    # imNew.putpixel((7, 16), colorWhite)
    # imNew.putpixel((8, 16), colorWhite)
    # imNew.putpixel((9, 16), colorWhite)
    # imNew.putpixel((10, 16), colorBlack)
    # imNew.putpixel((11, 16), colorTongue)
    # imNew.putpixel((12, 16), colorTongue)
    # imNew.putpixel((13, 16), colorBlack)
    # imNew.putpixel((14, 16), colorWhite)
    # imNew.putpixel((15, 16), colorWhite)
    # imNew.putpixel((16, 16), colorWhite)
    # imNew.putpixel((17, 16), colorWhite)
    # imNew.putpixel((18, 16), colorBlack)

    # imNew.putpixel((6, 17), colorBlack)
    # imNew.putpixel((7, 17), colorWhite)
    # imNew.putpixel((8, 17), colorWhite)
    # imNew.putpixel((9, 17), colorWhite)
    # imNew.putpixel((10, 17), colorWhite)
    # imNew.putpixel((11, 17), colorBlack)
    # imNew.putpixel((12, 17), colorBlack)
    # imNew.putpixel((13, 17), colorWhite)
    # imNew.putpixel((14, 17), colorWhite)
    # imNew.putpixel((15, 17), colorWhite)
    # imNew.putpixel((16, 17), colorWhite)
    # imNew.putpixel((17, 17), colorBlack)

    # imNew.putpixel((7, 18), colorBlack)
    # imNew.putpixel((8, 18), colorBlack)
    # imNew.putpixel((9, 18), colorWhite)
    # imNew.putpixel((10, 18), colorWhite)
    # imNew.putpixel((11, 18), colorWhite)
    # imNew.putpixel((12, 18), colorWhite)
    # imNew.putpixel((13, 18), colorWhite)
    # imNew.putpixel((14, 18), colorWhite)
    # imNew.putpixel((15, 18), colorBlack)
    # imNew.putpixel((16, 18), colorBlack)

    # imNew.putpixel((1, 19), colorBlack)
    # imNew.putpixel((6, 19), colorBlack)
    # imNew.putpixel((7, 19), colorsDict[colorShade])
    # imNew.putpixel((8, 19), colorsDict[colorPrimary])
    # imNew.putpixel((9, 19), colorBlack)
    # imNew.putpixel((10, 19), colorBlack)
    # imNew.putpixel((11, 19), colorBlack)
    # imNew.putpixel((12, 19), colorBlack)
    # imNew.putpixel((13, 19), colorBlack)
    # imNew.putpixel((14, 19), colorBlack)

    # imNew.putpixel((0, 20), colorBlack)
    # imNew.putpixel((1, 20), colorsDict[colorPrimary])
    # imNew.putpixel((2, 20), colorBlack)
    # imNew.putpixel((5, 20), colorBlack)
    # imNew.putpixel((6, 20), colorsDict[colorShade])
    # imNew.putpixel((7, 20), colorsDict[colorPrimary])
    # imNew.putpixel((8, 20), colorsDict[colorPrimary])
    # imNew.putpixel((9, 20), colorsDict[colorPrimary])
    # imNew.putpixel((10, 20), colorsDict[colorPrimary])
    # imNew.putpixel((11, 20), colorsDict[colorPrimary])
    # imNew.putpixel((12, 20), colorsDict[colorPrimary])
    # imNew.putpixel((13, 20), colorsDict[colorPrimary])
    # imNew.putpixel((14, 20), colorsDict[colorPrimary])
    # imNew.putpixel((15, 20), colorBlack)

    # imNew.putpixel((0, 21), colorsDict[colorPrimary])
    # imNew.putpixel((1, 21), colorBlack)
    # imNew.putpixel((4, 21), colorBlack)
    # imNew.putpixel((5, 21), colorsDict[colorShade])
    # imNew.putpixel((6, 21), colorsDict[colorPrimary])
    # imNew.putpixel((7, 21), colorsDict[colorPrimary])
    # imNew.putpixel((8, 21), colorsDict[colorPrimary])
    # imNew.putpixel((9, 21), colorsDict[colorPrimary])
    # imNew.putpixel((10, 21), colorsDict[colorPrimary])
    # imNew.putpixel((11, 21), colorsDict[colorPrimary])
    # imNew.putpixel((12, 21), colorsDict[colorPrimary])
    # imNew.putpixel((13, 21), colorsDict[colorPrimary])
    # imNew.putpixel((14, 21), colorsDict[colorPrimary])
    # imNew.putpixel((15, 21), colorBlack)

    # imNew.putpixel((0, 22), colorsDict[colorPrimary])
    # imNew.putpixel((1, 22), colorBlack)
    # imNew.putpixel((3, 22), colorBlack)
    # imNew.putpixel((4, 22), colorsDict[colorShade])
    # imNew.putpixel((5, 22), colorsDict[colorPrimary])
    # imNew.putpixel((6, 22), colorsDict[colorPrimary])
    # imNew.putpixel((7, 22), colorsDict[colorPrimary])
    # imNew.putpixel((8, 22), colorsDict[colorPrimary])
    # imNew.putpixel((9, 22), colorsDict[colorPrimary])
    # imNew.putpixel((10, 22), colorsDict[colorPrimary])
    # imNew.putpixel((11, 22), colorsDict[colorPrimary])
    # imNew.putpixel((12, 22), colorsDict[colorPrimary])
    # imNew.putpixel((13, 22), colorsDict[colorPrimary])
    # imNew.putpixel((14, 22), colorsDict[colorPrimary])
    # imNew.putpixel((15, 22), colorBlack)

    # imNew.putpixel((0, 23), colorsDict[colorPrimary])
    # imNew.putpixel((1, 23), colorBlack)
    # imNew.putpixel((2, 23), colorBlack)
    # imNew.putpixel((3, 23), colorsDict[colorShade])
    # imNew.putpixel((4, 23), colorsDict[colorPrimary])
    # imNew.putpixel((5, 23), colorsDict[colorPrimary])
    # imNew.putpixel((6, 23), colorsDict[colorPrimary])
    # imNew.putpixel((7, 23), colorsDict[colorPrimary])
    # imNew.putpixel((8, 23), colorsDict[colorPrimary])
    # imNew.putpixel((9, 23), colorBlack)
    # imNew.putpixel((10, 23), colorsDict[colorShade])
    # imNew.putpixel((11, 23), colorsDict[colorShade])
    # imNew.putpixel((12, 23), colorBlack)
    # imNew.putpixel((13, 23), colorsDict[colorShade])
    # imNew.putpixel((14, 23), colorsDict[colorShade])
    # imNew.putpixel((15, 23), colorBlack)

    im.paste(imNew, (0,0), mask=imNew)
