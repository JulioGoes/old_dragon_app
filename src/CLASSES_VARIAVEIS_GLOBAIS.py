from consulta_bancodedados import buscaClerigo, buscaHdA,\
                                  buscaLadrao, buscaMago

CLERIGO_PROGRESSAO, CLERIGO_AFASTAR, CLERIGO_MAGIAS = buscaClerigo()
HDA_PROGRESSAO = buscaHdA()
LADRAO_PROGRESSAO, LADRAO_TALENTOS = buscaLadrao()
MAGO_PROGRESSAO, MAGO_MAGIAS = buscaMago()
