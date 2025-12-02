import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img1 = mpimg.imread("time_fidelity.png")
img2 = mpimg.imread("time_fidelity_server.png")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].imshow(img1)
axes[0].set_title("")
axes[0].axis("off")

axes[1].imshow(img2)
axes[1].set_title("")
axes[1].axis("off")

plt.suptitle('Average execution time')
plt.tight_layout()
plt.show()
