# -*- coding: utf-8 -*-
import os
import StringIO

import Image
import ImageDraw
import ImageColor

places = { 'Rondônia' : (80,117),
           'Acre' : (32,110),
           'Amazonas' : (64,64),
           'Roraima' : (92,19),
           'Pará' : (159,60),
           'Amapá' : (164,28),
           'Tocantins' : (192,114),
           'Maranhão' : (220,67),
           'Piauí' : (241,84),
           'Ceará' : (260,72),
           'Rio Grande do Norte' : (283,83),
           'Paraíba' : (286,94),
           'Pernambuco' : (291,102),
           'Alagoas' : (285,113),
           'Sergipe' : (275,121),
           'Bahia' : (241,132),
           'Minas Gerais' : (221,178),
           'Espírito Santo' : (254,188),
           'Rio de Janeiro' : (238,208),
           'São Paulo' : (195,210),
           'Paraná' : (167,226),
           'Santa Catarina' : (183,246),
           'Rio Grande do Sul' : (154,263),
           'Mato Grosso' : (139,142),
           'Mato Grosso do Sul' : (144,195),
           'Goiás' : (183,162),
           'Distrito Federal' : (197,158),
}


def make_brasil_map(data, finalsize=None):
  brasil_png = os.path.join(os.path.split(__file__)[0], 'brasil.png')
  raw = Image.open(brasil_png).copy()
  mapa = Image.new('RGBA', raw.size, 'white')
  mapa.paste(raw, (0, 0))

  for k in data:
    if k in places:
      if type(data[k]) == str:
        color = ImageColor.getcolor('#'+data[k], 'RGBA')
      else:
        color = data[k]
      ImageDraw.floodfill(mapa, places[k], color)

  if finalsize:
    mapa = mapa.resize(finalsize)

  dump = StringIO.StringIO()
  mapa.save(dump, 'PNG')
  return dump.getvalue()
