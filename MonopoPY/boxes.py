from settings import Box

kinds = ['regular', 'tax', 'jail', 'chance', 'chest', 'start', 'freestop', 'train', 'service']

colors = [None, 'brown', 'cyan', 'pink', 'orange', 'red', 'yellow', 'green', 'blue']

#    def __init__(self, name, cost, color, kind, place, owner):
box_1 = Box('INICIO', 0, colors[0], kinds[5], 1, None) #edge
box_2 = Box('AVENIDA MEDITERRÁNEO', 1, colors[1], kinds[0], 2, None)
box_3 = Box('ARCA COMUNAL', 1, colors[0], kinds[4], 3, None)
box_4 = Box('AVENIDA BÁLTICA', 1, colors[1], kinds[0], 4, None)
box_5 = Box('IMPUESTOS SOBRE INGRESOS', 1, colors[0], kinds[1], 5, None)
box_6 = Box('FERROCARRIL READING', 1, colors[0], kinds[7], 6, None)
box_7 = Box('AVENIDA ORIENTAL', 1, colors[2], kinds[0], 7, None)
box_8 = Box('FORTUNA', 1, colors[0], kinds[3], 8, None)
box_9 = Box('AVENIDA VERMONT', 1, colors[2], kinds[0], 9, None)
box_10 = Box('AVENIDA CONNETICUT', 1, colors[2], kinds[0], 10, None)

box_11 = Box('DE VISITA', 0, colors[0], kinds[6], 11, None) #edge
box_12 = Box('PLAZA SAN CARLOS', 0, colors[3], kinds[0], 12, None)
box_13 = Box('COMPAÑIA DE ELECTRICIDAD', 0, colors[0], kinds[8], 13, None)
box_14 = Box('AVENIDA ESTADOS ', 0, colors[3], kinds[0], 14, None)
box_15 = Box('AVENIDA VIRGINIA', 0, colors[3], kinds[0], 15, None)
box_16 = Box('FERRICARRIL PENNSYLVANIA', 0, colors[0], kinds[7], 16, None)
box_17 = Box('PLAZA ST. JAMES', 0, colors[4], kinds[0], 17, None)
box_18 = Box('ARCA COMUNAL', 0, colors[0], kinds[4], 18, None)
box_19 = Box('AVENIDA TENNESSE', 0, colors[4], kinds[0], 19, None)
box_20 = Box('AVENIDA NUEVA YORK', 0, colors[4], kinds[0], 20, None)

box_21 = Box('FREE STOP', 0, colors[0], kinds[6], 21, None) #edge
box_22 = Box('AVENIDA KENTUCKY', 0, colors[5], kinds[0], 22, None)
box_23 = Box('FORTUNA', 0, colors[0], kinds[8], 23, None)
box_24 = Box('AVENIDA INDIANA', 0, colors[5], kinds[0], 24, None)
box_25 = Box('AVENIDA ILLINOIS', 0, colors[5], kinds[0], 25, None)
box_26 = Box('FERROCARRIL B&O', 0, colors[0], kinds[7], 26, None)
box_27 = Box('AVENIDA ATLANTICO', 0, colors[6], kinds[0], 27, None)
box_28 = Box('AVENIDA VENTNOR', 0, colors[6], kinds[0], 28, None)
box_29 = Box('COMPAÑIA DE AGUA', 0, colors[0], kinds[8], 29, None)
box_30 = Box('JARDINES MAVEN', 0, colors[6], kinds[0], 30, None)

#jail has place 21 bc of the effect of going back in the board 
box_31 = Box('A LA CÁRCEL', 0, colors[0], kinds[2], 21, None) #edge 
box_32 = Box('AVENIDA PACIFICO', 0, colors[7], kinds[0], 32, None)
box_33 = Box('AVENIDA CAROLINA DEL NORTE', 0, colors[7], kinds[8], 33, None)
box_34 = Box('ARCA COMUNAL', 0, colors[0], kinds[4], 34, None)
box_35 = Box('AVENIDA PENNSYLVANIA', 0, colors[7], kinds[0], 35, None)
box_36 = Box('FERROCARRIL VIA RÁPIDA', 0, colors[0], kinds[7], 36, None)
box_37 = Box('FORTUNA', 0, colors[0], kinds[3], 37, None)
box_38 = Box('PLAZA PARK', 0, colors[8], kinds[0], 38, None)
box_39 = Box('IMPUESTOS SOBRE POSESIONES DE LUJO', 0, colors[0], kinds[1], 39, None)
box_40 = Box('EL MUELLE', 0, colors[8], kinds[0], 40, None)