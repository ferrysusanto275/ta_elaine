import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt

from app.models.isi import isiModel
from app.models.keluaran import keluaranModel
isi=isiModel()
keluaran=keluaranModel()
area=2
year=2019
df=keluaran.getDfK(area,year)
# print(df['nama'])
# df=isi.getDfAllIndikatorBobot()
data_indikator=keluaran.getAllIndikatorby_Area(area)
# data_area=keluaran.getAllInstansiby_Area(area)
# df=df[df['id'].astype('str').isin(data_area)]
# df=df[df['year']==year]

df_indikator=df[data_indikator]
transposed_df = df_indikator.T

print(transposed_df)

scaled_data = preprocessing.scale(transposed_df.T)

pca = PCA()
# pca.fit(transposed_df)
# pca_data=pca.transform(transposed_df)
pca.fit(scaled_data) # melakukan perhitungan PCA
pca_data = pca.transform(scaled_data) #mendapatkan koordinat titik

#melakukan plotting untuk melihat bobot dari setiap variansi PCA
per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
labels = ['PC' + str(x) for x in range(1, len(per_var)+1)] #labelin diagram

# plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
# plt.ylabel('Percentage of Explained Variance')
# plt.xlabel('Principal Component')
# plt.title('Scree Plot')
# plt.show()

pca_df = pd.DataFrame(pca_data, index=transposed_df.columns, columns=labels)

# plt.scatter(pca_df.PC1, pca_df.PC2, c=df['Cluster'], cmap='viridis')
# plt.title('My PCA Graph')
# plt.xlabel('PC1 - {0}%'.format(per_var[0]))
# plt.ylabel('PC2 - {0}%'.format(per_var[1]))

# for sample in pca_df.index:
#     plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))
# plt.annotate.set_visible(False)
# Create a custom patch for each point
names = np.array(df['nama'].tolist())
c = df['Cluster']

# norm = plt.Normalize(1,4)
# cmap = plt.cm.RdYlGn

fig,ax = plt.subplots()
sc = plt.scatter(pca_df.PC1, pca_df.PC2, s=100,  c=df['Cluster'], cmap='viridis')

annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    print(ind)
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text=[names[n] for n in ind["ind"]]
    # text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
                        #    " ".join([names[n] for n in ind["ind"]]))
    annot.set_text(text)
    # annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
    # annot.get_bbox_patch().set_alpha(0.4)
    

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()

# Show the plot
# plt.show()

# plt.show()

#mencari tahun komponen yang paling berpengaruh
# print()
loading_scores = pd.Series(pca.components_[0], index=data_indikator)
sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)

# mengambil data 10 biji
top_10_genes = sorted_loading_scores[0:10].index.values

print(loading_scores[top_10_genes])
