# Genera las Figuras 1 y 3 del reporte con el texto de las opciones de respuesta
# (catálogos de la ECENASEM 2021) en lugar de los códigos numéricos.
# Usa los mismos datos, la misma partición y el mismo modelo que el cuaderno.
import re, numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import statsmodels.api as sm, statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, roc_curve, confusion_matrix

S="conjunto_de_datos_mex_cog_2021_evaluacion_cognitiva_ecenasem_2021.csv"
raw=pd.read_csv(S,dtype=str)
V=["AGE_MXCOG_21","SEX_MXCOG_21","MC_AIVD_COMIDAS_21","MC_AIVD_COMPRAR_21","MC_AIVD_MEDICINA_21","MC_AIVD_DINERO_21","MC_COMP_MEMORIA_21","MC_AISLADO_21","MC_IGNORADO_21","MC_FALTA_COMPA_21","MC_ESTRES_21","MC_CESD_DEPRIMIDO_21"]
d=raw[V].copy()
for c in d.columns:
    d[c]=d[c].astype(str).str.strip(); d.loc[d[c].isin(["","nan","NA"]),c]=np.nan
d["AGE_MXCOG_21"]=pd.to_numeric(d["AGE_MXCOG_21"],errors="coerce")
d["SEX_MXCOG_21"]=pd.Categorical(d["SEX_MXCOG_21"].map({"1":"Hombre","2":"Mujer"}),categories=["Hombre","Mujer"])
for v in V[2:6]:
    d[v]=pd.Categorical(d[v].map({"0":"No","1":"Si"}),categories=["No","Si"])
for v in V[6:11]:
    d[v]=pd.Categorical(d[v],categories=sorted(d[v].dropna().unique()),ordered=True)
d["MC_CESD_DEPRIMIDO_21"]=pd.Categorical(d["MC_CESD_DEPRIMIDO_21"].map({"0":"No","1":"Si"}),categories=["No","Si"])
dc=d.dropna().reset_index(drop=True)
print(len(d),len(dc))
dc["y"]=(dc["MC_CESD_DEPRIMIDO_21"]=="Si").astype(int)
train,test=train_test_split(dc,test_size=0.3,random_state=123,stratify=dc["y"])
f=("y ~ AGE_MXCOG_21 + C(SEX_MXCOG_21) + C(MC_AIVD_COMIDAS_21) + C(MC_AIVD_COMPRAR_21) + C(MC_AIVD_MEDICINA_21) + C(MC_AIVD_DINERO_21) + C(MC_COMP_MEMORIA_21) + C(MC_AISLADO_21) + C(MC_IGNORADO_21) + C(MC_FALTA_COMPA_21) + C(MC_ESTRES_21)")
m=smf.glm(f,data=train,family=sm.families.Binomial()).fit()
p=m.predict(test); print("AUC",round(roc_auc_score(test["y"],p),4))
fpr,tpr,th=roc_curve(test["y"],p); u=th[np.argmax(tpr-fpr)]; print("Youden",round(u,4)); print(confusion_matrix(test["y"],(p>=u).astype(int)))
ic=m.conf_int()
t=pd.DataFrame({"OR":np.exp(m.params),"lo":np.exp(ic[0]),"hi":np.exp(ic[1]),"p":m.pvalues})
print(t.round(3))

plt.rcParams.update({"font.family":"Inter","font.size":11,"axes.spines.top":False,"axes.spines.right":False})
FREC={"1":"Nunca","2":"Pocas veces","3":"Algunas veces","4":"Con mucha\nfrecuencia"}
# Figura 1
tab=pd.crosstab(dc["MC_FALTA_COMPA_21"],dc["MC_CESD_DEPRIMIDO_21"],normalize="index")
print(tab.round(3))
fig,ax=plt.subplots(figsize=(7.4,5.3))
x=np.arange(4); w=0.5
ax.bar(x,tab["No"],w,color="#66c2a5",label="No")
ax.bar(x,tab["Si"],w,bottom=tab["No"],color="#b3b3b3",label="Si")
ax.set_xticks(x); ax.set_xticklabels([FREC[k] for k in tab.index])
ax.set_ylabel("Proporción"); ax.set_xlabel("Frecuencia con la que siente que le falta compañía",labelpad=8)
ax.set_title("Depresión (CES-D) según la falta de compañía",loc="left",fontsize=12,pad=12)
ax.yaxis.grid(True,color="#dddddd"); ax.set_axisbelow(True); ax.tick_params(length=4)
ax.legend(title="Depresión (CES-D)",frameon=False,loc="center left",bbox_to_anchor=(1.02,0.5),fontsize=10,title_fontsize=10)
fig.tight_layout(); fig.savefig("fig1_compania.png",dpi=150); plt.close(fig)

# Figura 3
NOM={"AGE_MXCOG_21":"Edad","SEX_MXCOG_21":"Sexo","MC_AIVD_COMIDAS_21":"Dificultad para preparar comidas","MC_AIVD_COMPRAR_21":"Dificultad para ir de compras","MC_AIVD_MEDICINA_21":"Dificultad para tomar medicinas","MC_AIVD_DINERO_21":"Dificultad para manejar dinero","MC_COMP_MEMORIA_21":"Cambio en la memoria","MC_AISLADO_21":"Se siente aislado","MC_IGNORADO_21":"Se siente ignorado","MC_FALTA_COMPA_21":"Le falta compañía","MC_ESTRES_21":"Estrés por la pandemia"}
F2={"2":"pocas veces","3":"algunas veces","4":"con mucha frecuencia"}
NIV={"MC_COMP_MEMORIA_21":{"2":"más o menos igual","3":"peor"},"MC_AISLADO_21":F2,"MC_IGNORADO_21":F2,"MC_FALTA_COMPA_21":F2,"MC_ESTRES_21":{"2":"poco","3":"algo","4":"mucho"},"SEX_MXCOG_21":{"Mujer":"mujer"}}
def lab(term):
    mm=re.match(r"C\((\w+)\)\[T\.(.+)\]",term)
    if mm:
        v,n=mm.groups()
        if v.startswith("MC_AIVD"): return NOM[v]
        return f"{NOM[v]}: {NIV[v][n]}"
    return NOM.get(term,term)
tp=t.drop(index="Intercept").copy(); tp["lab"]=[lab(i) for i in tp.index]; tp=tp.sort_values("OR")
fig,ax=plt.subplots(figsize=(8.2,8.0))
y=np.arange(len(tp))
ax.errorbar(tp["OR"],y,xerr=[tp["OR"]-tp["lo"],tp["hi"]-tp["OR"]],fmt="o",color="#2a78d6",ecolor="#8a8a8a",capsize=3,markersize=6,elinewidth=1.3)
ax.axvline(1,color="#d95926",ls="--",lw=1.3)
ax.set_yticks(y); ax.set_yticklabels(tp["lab"])
ax.set_xlabel("Razón de momios",labelpad=8)
ax.xaxis.grid(True,color="#dddddd"); ax.set_axisbelow(True); ax.set_ylim(-0.7,len(tp)-0.3)
fig.tight_layout(); fig.savefig("fig3_momios.png",dpi=150); plt.close(fig)
