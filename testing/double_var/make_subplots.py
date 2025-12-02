import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img1 = mpimg.imread("2_turb.png")
img2 = mpimg.imread("results_heatmap.png")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].imshow(img1)
axes[0].set_title("Zone 3 with 2 turbines")
axes[0].axis("off")

axes[1].imshow(img2)
axes[1].set_title("Effect of third turbine")
axes[1].axis("off")

plt.tight_layout()
plt.show()
