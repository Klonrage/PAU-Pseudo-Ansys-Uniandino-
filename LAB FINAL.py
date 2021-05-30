import pandas as pd
import math
import numpy as np

from pandas.core.frame import DataFrame

def calcular_fuerzas_miembros(F:float)->DataFrame:
    dataframe_primitivo={}
    dataframe_primitivo["F_dj"]=0

    """
Todo esto es del corte 2
    """
    F_lk=(-(F/2)*(250/6))/150
    #AL ser simetrico, podemos asignar ese valor al otro lado
    F_hi=F_lk
    dataframe_primitivo["F_lk"]=[F_lk]
    dataframe_primitivo["F_hi"]=[F_hi]
    #Ahora calculamos F_bk
    angulo = math.atan(18/5)
    F_bk=(-F/2)/math.sin(angulo)
    F_fi = F_bk
    dataframe_primitivo["F_bk"]=[F_bk]
    dataframe_primitivo["F_fi"]=[F_fi]
    #Ahora calculamos F_bc
    F_bc=-F_bk*math.cos(angulo)-F_lk
    F_fe=F_bc
    dataframe_primitivo["F_bc"]=[F_bc]
    dataframe_primitivo["F_fe"]=[F_fe]
    #Ahora resolvemos por nodos el pin A para tener F_al y F_ab
    F_al=(-F/2)/math.sin(angulo)
    F_gh=F_al
    F_ab=-F_al*math.cos(angulo)
    F_gf = F_ab
    dataframe_primitivo["F_ab"]=[F_ab]
    dataframe_primitivo["F_gf"]=[F_gf]
    dataframe_primitivo["F_al"]=[F_al]
    dataframe_primitivo["F_gh"]=[F_gh]
    #Ahora mirando el Pin L, resolvemos para F_lb
    F_lb = -(F_al)*math.sin(angulo)
    F_hf = F_lb
    dataframe_primitivo["F_lb"]=[F_lb]
    dataframe_primitivo["F_hf"]=[F_hf]

    """
    Esto es el corte 1
    """

    F_kj =(-(F/2)*(250/3))/150
    F_ij = F_kj
    dataframe_primitivo["F_kj"]=[F_kj]
    dataframe_primitivo["F_ij"]=[F_ij]
    F_cj = (-F/2)/math.sin(angulo)
    F_ej = F_cj
    dataframe_primitivo["F_cj"]=[F_cj]
    dataframe_primitivo["F_ej"]=[F_ej]
    F_cd=-F_cj*math.cos(angulo)-F_kj
    F_ed=F_cd
    dataframe_primitivo["F_cd"]=[F_cd]
    dataframe_primitivo["F_ed"]=[F_ed]
    #Calculamos F_kc
    F_kc = -(F_bk)*math.sin(angulo)
    F_ie = F_kc
    dataframe_primitivo["F_kc"]=[F_kc]
    dataframe_primitivo["F_ie"]=[F_ie]

    result=pd.DataFrame(dataframe_primitivo,columns=list(dataframe_primitivo.keys()))

    return result

def buscar_maximo():
    lista_de_cargas = np.linspace(0,1000,1000)
    for carga in lista_de_cargas:
        resultado = calcular_fuerzas_miembros(carga)
        carga_mas_grande=resultado["F_al"].iloc[0]*-1.
        estres = carga_mas_grande/(3.1415926535*(0.003**2))
        if estres>3200000:
            return carga
print(buscar_maximo())

check = True
while check == True:
    print("Bienvenido a Ansys(Andes Version)")
    print("Si desea salir, simplemente escriba 'salir'")
    carga = (input("Coloque la carga que se le quiere aplicar a la celosía Howe :)"))
    if carga == "salir":
        check = False
    else:
        carga = float(carga)
        pd.set_option('display.max_columns', None)
        print(calcular_fuerzas_miembros(carga))








