import gistools


def test():
    e, wa = gistools.convert_MCT_2_BD09(12661179.01, 4109201.16)
    print(e, wa)


test()
