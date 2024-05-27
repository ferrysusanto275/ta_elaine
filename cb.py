# import matplotlib.pyplot as plt
# import numpy as np; np.random.seed(1)

# x = np.random.rand(15)
# y = np.random.rand(15)
# names = np.array(list("ABCDEFGHIJKLMNO"))
# c = np.random.randint(1,5,size=15)

# norm = plt.Normalize(1,4)
# cmap = plt.cm.RdYlGn

# fig,ax = plt.subplots()
# sc = plt.scatter(x,y,c=c, s=100, cmap=cmap, norm=norm)

# annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
#                     bbox=dict(boxstyle="round", fc="w"),
#                     arrowprops=dict(arrowstyle="->"))
# annot.set_visible(False)

# def update_annot(ind):
    
#     pos = sc.get_offsets()[ind["ind"][0]]
#     annot.xy = pos
#     text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
#                            " ".join([names[n] for n in ind["ind"]]))
#     annot.set_text(text)
#     annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
#     annot.get_bbox_patch().set_alpha(0.4)
    

# def hover(event):
#     vis = annot.get_visible()
#     if event.inaxes == ax:
#         cont, ind = sc.contains(event)
#         if cont:
#             update_annot(ind)
#             annot.set_visible(True)
#             fig.canvas.draw_idle()
#         else:
#             if vis:
#                 annot.set_visible(False)
#                 fig.canvas.draw_idle()

# fig.canvas.mpl_connect("motion_notify_event", hover)

# plt.show()

from sklearn.cluster import AgglomerativeClustering

# Sample data (replace with your actual data)
data = [[1, 1], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]]

# Define two different threshold distances
threshold1 = 2
threshold2 = 4

# Create two AgglomerativeClustering models with different thresholds
model1 = AgglomerativeClustering(n_clusters=None, linkage='ward', distance_threshold=threshold1)
model2 = AgglomerativeClustering(n_clusters=None, linkage='ward', distance_threshold=threshold2)

# Fit the models to the data
model1.fit(data)
model2.fit(data)

# Get cluster labels for each model
cluster_labels1 = model1.labels_
cluster_labels2 = model2.labels_

# Print the results
print("Cluster labels with threshold", threshold1, ":", cluster_labels1)
print("Cluster labels with threshold", threshold2, ":", cluster_labels2)
