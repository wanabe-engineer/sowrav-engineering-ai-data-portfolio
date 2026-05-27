DSCH 2.7a
VERSION 10/29/2022 1:35:08 PM
BB(31,-15,179,95)
SYM  #nmos
BB(70,40,90,60)
TITLE 85 45  #nmos
MODEL 901
PROP   2u 1u                                                                                                                                                                                                        
REC(71,45,19,15,r)
VIS 2
PIN(90,60,0.000,0.000)s
PIN(70,50,0.000,0.000)g
PIN(90,40,0.030,0.280)d
LIG(80,50,70,50)
LIG(80,56,80,44)
LIG(82,56,82,44)
LIG(90,44,82,44)
LIG(90,40,90,44)
LIG(90,56,82,56)
LIG(90,60,90,56)
VLG   nmos nmos(drain,source,gate);
FSYM
SYM  #pmos
BB(50,0,70,20)
TITLE 65 5  #pmos
MODEL 902
PROP   2.0u 1u                                                                                                                                                                                                        
REC(51,5,19,15,r)
VIS 2
PIN(70,0,0.000,0.000)s
PIN(50,10,0.000,0.000)g
PIN(70,20,0.030,0.280)d
LIG(50,10,56,10)
LIG(58,10,58,10)
LIG(60,16,60,4)
LIG(62,16,62,4)
LIG(70,4,62,4)
LIG(70,0,70,4)
LIG(70,16,62,16)
LIG(70,20,70,16)
VLG   pmos pmos(drain,source,gate);
FSYM
SYM  #pmos
BB(130,15,150,35)
TITLE 145 20  #pmos
MODEL 902
PROP   2.0u 1u                                                                                                                                                                                                        
REC(131,20,19,15,r)
VIS 2
PIN(150,15,0.000,0.000)s
PIN(130,25,0.000,0.000)g
PIN(150,35,0.030,0.140)d
LIG(130,25,136,25)
LIG(138,25,138,25)
LIG(140,31,140,19)
LIG(142,31,142,19)
LIG(150,19,142,19)
LIG(150,15,150,19)
LIG(150,31,142,31)
LIG(150,35,150,31)
VLG   pmos pmos(drain,source,gate);
FSYM
SYM  #button4
BB(31,66,40,74)
TITLE 35 70  #button
MODEL 59
PROP                                                                                                                                                                                                            
REC(32,67,6,6,r)
VIS 1
PIN(40,70,0.000,0.000)in4
LIG(39,70,40,70)
LIG(31,74,31,66)
LIG(39,74,31,74)
LIG(39,66,39,74)
LIG(31,66,39,66)
LIG(32,73,32,67)
LIG(38,73,32,73)
LIG(38,67,38,73)
LIG(32,67,38,67)
FSYM
SYM  #pmos
BB(85,0,105,20)
TITLE 100 5  #pmos
MODEL 902
PROP   2.0u 1u                                                                                                                                                                                                        
REC(86,5,19,15,r)
VIS 2
PIN(105,0,0.000,0.000)s
PIN(85,10,0.000,0.000)g
PIN(105,20,0.030,0.280)d
LIG(85,10,91,10)
LIG(93,10,93,10)
LIG(95,16,95,4)
LIG(97,16,97,4)
LIG(105,4,97,4)
LIG(105,0,105,4)
LIG(105,16,97,16)
LIG(105,20,105,16)
VLG   pmos pmos(drain,source,gate);
FSYM
SYM  #light1
BB(173,20,179,34)
TITLE 175 34  #light
MODEL 49
PROP                                                                                                                                                                                                            
REC(174,21,4,4,r)
VIS 1
PIN(175,35,0.000,0.000)out1
LIG(178,26,178,21)
LIG(178,21,177,20)
LIG(174,21,174,26)
LIG(177,31,177,28)
LIG(176,31,179,31)
LIG(176,33,178,31)
LIG(177,33,179,31)
LIG(173,28,179,28)
LIG(175,28,175,35)
LIG(173,26,173,28)
LIG(179,26,173,26)
LIG(179,28,179,26)
LIG(175,20,174,21)
LIG(177,20,175,20)
FSYM
SYM  #nmos
BB(130,35,150,55)
TITLE 145 40  #nmos
MODEL 901
PROP   2u 1u                                                                                                                                                                                                        
REC(131,40,19,15,r)
VIS 2
PIN(150,55,0.000,0.000)s
PIN(130,45,0.000,0.000)g
PIN(150,35,0.030,0.140)d
LIG(140,45,130,45)
LIG(140,51,140,39)
LIG(142,51,142,39)
LIG(150,39,142,39)
LIG(150,35,150,39)
LIG(150,51,142,51)
LIG(150,55,150,51)
VLG   nmos nmos(drain,source,gate);
FSYM
SYM  #nmos
BB(70,60,90,80)
TITLE 85 65  #nmos
MODEL 901
PROP   2u 1u                                                                                                                                                                                                        
REC(71,65,19,15,r)
VIS 2
PIN(90,80,0.000,0.000)s
PIN(70,70,0.000,0.000)g
PIN(90,60,0.030,0.070)d
LIG(80,70,70,70)
LIG(80,76,80,64)
LIG(82,76,82,64)
LIG(90,64,82,64)
LIG(90,60,90,64)
LIG(90,76,82,76)
LIG(90,80,90,76)
VLG   nmos nmos(drain,source,gate);
FSYM
SYM  #vss
BB(115,87,125,95)
TITLE 119 92  #vss
MODEL 0
PROP                                                                                                                                                                                                            
REC(115,85,0,0,b)
VIS 0
PIN(120,85,0.000,0.000)vss
LIG(120,85,120,90)
LIG(115,90,125,90)
LIG(115,93,117,90)
LIG(117,93,119,90)
LIG(119,93,121,90)
LIG(121,93,123,90)
FSYM
SYM  #vdd
BB(115,-15,125,-5)
TITLE 118 -9  #vdd
MODEL 1
PROP                                                                                                                                                                                                            
REC(0,0,0,0,)
VIS 0
PIN(120,-5,0.000,0.000)vdd
LIG(120,-5,120,-10)
LIG(120,-10,115,-10)
LIG(115,-10,120,-15)
LIG(120,-15,125,-10)
LIG(125,-10,120,-10)
FSYM
SYM  #button3
BB(31,6,40,14)
TITLE 35 10  #button
MODEL 59
PROP                                                                                                                                                                                                            
REC(32,7,6,6,r)
VIS 1
PIN(40,10,0.000,0.000)in3
LIG(39,10,40,10)
LIG(31,14,31,6)
LIG(39,14,31,14)
LIG(39,6,39,14)
LIG(31,6,39,6)
LIG(32,13,32,7)
LIG(38,13,32,13)
LIG(38,7,38,13)
LIG(32,7,38,7)
FSYM
CNC(90 20)
CNC(105 -5)
CNC(90 30)
CNC(130 30)
CNC(60 70)
LIG(150,35,175,35)
LIG(90,40,90,30)
LIG(130,25,130,30)
LIG(90,20,105,20)
LIG(70,20,90,20)
LIG(150,15,150,-5)
LIG(150,-5,105,-5)
LIG(70,-5,70,0)
LIG(105,0,105,-5)
LIG(105,-5,70,-5)
LIG(130,30,90,30)
LIG(90,30,90,20)
LIG(130,30,130,45)
LIG(150,55,150,85)
LIG(150,85,90,85)
LIG(90,85,90,80)
LIG(50,10,40,10)
LIG(70,50,50,50)
LIG(50,50,50,10)
LIG(85,10,75,10)
LIG(75,10,75,40)
LIG(75,40,60,40)
LIG(60,40,60,70)
LIG(60,70,70,70)
LIG(60,70,40,70)
TEXT 33 75  #B
TEXT 35 19  #A
FFIG C:\Users\sowra\Downloads\AND GATE LR1.sch
