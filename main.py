import math

def task_kin(L1,L2, Q1,Q2):

    #прямая задача кин
    # L1 = int(input("введите L1 "))
    # L2 = int(input("введите L2 "))
    # Q1 = float(input("введите Q1 "))
    # Q2 = float(input("введите Q2 "))

    result_x = L1 * math.cos(Q1) + L2 * math.cos(Q1 + Q2) #координата x
    result_y = L1 * math.sin(Q1) + L2 * math.sin(Q1 + Q2) #координата y

    #обр задача кин
    B = math.sqrt(result_x ** 2 + result_y ** 2)

    q1 = math.acos(result_x / B)        #угол q1

    a = L1 ** 2 - L2 ** 2 + B ** 2      #угол q2
    b = 2 * B * L1
    q2 = math.acos(a / b)

    Q1_obr = q1 - q2                    #угол Q1

    aa = L1 ** 2 + L2 ** 2 - B ** 2     #угол_Q2
    bb = 2 * L1 * L2
    cc = math.acos(aa / bb)
    Q2_obr = math.pi - cc

    print('Координаты точки в пространстве по прямой задаче кинематики x =', result_x, 'y =', result_y)
    print('По ообратной задаче кинематики углы для того что бы попасть в координаты x, y: Q1 =', Q1_obr, 'Q2 =', Q2_obr)



L1 = int(input("введите L1 "))
L2 = int(input("введите L2 "))
Q1 = float(input("введите Q1 "))
Q2 = float(input("введите Q2 "))

task_kin(L1,L2, Q1,Q2)