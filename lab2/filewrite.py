
# coding: utf-8

# In[ ]:


def filewrite():
    out = open('out.txt', 'w')
    out.write("_________________________________________________________________________________________________________________________________\n" +
              "|  Вид функции  |     Линейная      |    Полиномиальная    |    Экспоненциальная    |      Степенная        |  Логарифмическая   |\n" +
              "|_______________|___________________|______________________|________________________|_______________________|____________________|\n" +
              "|   X   |   Y   | y = %.2fx + %.2f  | y=%.2fx^2+%.2fx+%.2f |  y = %.2f * e^(%.2fx)  |   y = %.2f * x^%.2f   | y=%.2f + %.2fln(x) |\n" % (ans[0].get('a'), ans[0].get('b'), ans[1].get('a'), ans[1].get('b'), ans[1].get('c'), ans[2].get('a'), ans[2].get('b'), ans[3].get('a'), ans[3].get('b'), ans[4].get('a'), ans[4].get('b')) +
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[0]}  |  {y[0]} |' + "       %.4f      |"%f(x[0], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[0], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[0], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[0], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[0], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[1]}  |  {y[1]} |' + "       %.4f      |"%f(x[1], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[1], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[1], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[1], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[1], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[2]}  |  {y[2]} |' + "       %.4f      |"%f(x[2], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[2], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[2], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[2], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[2], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[3]}  |  {y[3]} |' + "       %.4f      |"%f(x[3], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[3], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[3], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[3], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[3], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[4]}  |  {y[4]} |' + "       %.4f      |"%f(x[4], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[4], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[4], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[4], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[4], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[5]}  |  {y[5]} |' + "       %.4f      |"%f(x[5], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[5], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[5], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[5], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[5], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[6]}  |  {y[6]} |' + "       %.4f      |"%f(x[6], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[6], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[6], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[6], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[6], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[7]}  |  {y[7]} |' + "       %.4f      |"%f(x[7], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[7], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[7], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[7], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[7], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[8]}  |  {y[8]} |' + "       %.4f      |"%f(x[8], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[8], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[8], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[8], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[8], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[9]}  |  {y[9]} |' + "       %.4f      |"%f(x[9], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[9], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[9], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[9], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[9], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[10]}  |  {y[10]} |' + "       %.4f      |"%f(x[10], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[10], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[10], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[10], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[10], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[11]}  |  {y[11]} |' + "       %.4f      |"%f(x[11], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[11], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[11], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[11], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[11], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
             f'|  {x[12]}  |  {y[12]} |' + "       %.4f      |"%f(x[12], ans[0].get("a"), ans[0].get("b"), 0) + "        %.4f        |" % f1(x[12], ans[1].get("a"), ans[1].get("b"), ans[1].get("c")) + "         %.4f         |"%(f2(x[12], ans[2].get("a"), ans[2].get("b"), 0)) + "         %.4f        |"%(f3(x[12], ans[3].get("a"), ans[3].get("b"), 0)) +  "       %.4f       |"%(f4(x[12], ans[4].get("a"), ans[4].get("b"), 0)) +"\n"+ 
              "|_______|_______|___________________|______________________|________________________|_______________________|____________________|\n" +
              "|       S       |       %.4f      |       %.4f         |        %.4f          |        %.4f         |      %.4f        |\n"%(ans[0].get("S"), ans[1].get("S"), ans[2].get("S"), ans[3].get("S"), ans[4].get("S")) +
              "|_______________|___________________|______________________|________________________|_______________________|____________________|\n" +
              "|       s       |       %.4f      |       %.4f         |        %.4f          |        %.4f         |      %.4f        |\n"%(ans[0].get("s"), ans[1].get("s"), ans[2].get("s"), ans[3].get("s"), ans[4].get("s")) +
              "|_______________|___________________|______________________|________________________|_______________________|____________________|\n" +
              "|       a       |       %.4f      |       %.4f         |        %.4f          |        %.4f         |     %.4f         |\n"%(ans[0].get("a"), ans[1].get("a"), ans[2].get("a"), ans[3].get("a"), ans[4].get("a")) +
              "|_______________|___________________|______________________|________________________|_______________________|____________________|\n" +
              "|       b       |       %.4f      |       %.4f         |        %.4f          |        %.4f         |       %.4f       |\n"%(ans[0].get("b"), ans[1].get("b"), ans[2].get("b"), ans[3].get("b"), ans[4].get("b")) +
              "|_______________|___________________|______________________|________________________|_______________________|____________________|\n" +
              "|       c       |       --          |       %.4f         |          --            |           --          |         --         |\n"%(ans[1].get("c")) +
              "|_______________|___________________|______________________|________________________|_______________________|____________________|\n")
    out.close()

