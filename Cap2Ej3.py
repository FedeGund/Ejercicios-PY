# el import msvcrt es para que el programa no se cierre
import msvcrt
horas = int(input("Ingrese cantidad de horas a la semana: "))
paga = float(input("Ingrese pago por hora: "))
pago_neto = horas * paga * 4
print("Pago del mes: ", pago_neto)

msvcrt.getch()
#Este ultimo es para que no cierre el programa