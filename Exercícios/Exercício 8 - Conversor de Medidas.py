m = float(input("Digite uma distância em metros: "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print("{}m em quilômetros = {}km".format(m, km))
print("{}m em hectômetros = {}hm".format(m, hm))
print("{}m em decâmetros = {}dam".format(m, dam))
print("{}m em decímetros = {:.0f}dm".format(m, dm))
print("{}m em centímetros = {:.0f}cm".format(m, cm))
print("{}m em milímetros = {:.0f}mm".format(m, mm))