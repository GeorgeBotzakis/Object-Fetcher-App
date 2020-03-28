#example of loading and plotting the mnist dataset, remember handwritten digit classification
from tensorflow.keras.datasets.mnist import load_data
from matplotlib import pyplot

#load dataset
(trainx, trainy), (testx, testy) = load_data()

#summarize loaded dataset
print('Train: X=%s, y=%s' % (trainx.shape, trainy.shape))
print('Test: X=%s, y=%s' % (testx.shape, testy.shape))
#plot first few images
for i in range(25):
    #define subplot
    pyplot.subplot(5, 5, i+1)
    #plot raw pixel data
    pyplot.imshow(testx[i], cmap=pyplot.get_cmap('gray'))
#show the figure
# pyplot.show()
#save figure in image file
###pyplot.savefig("test_graph.png")

#tbc . . .