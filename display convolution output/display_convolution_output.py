from numpy import expand_dims
from keras.models import Model  
# from math import ceil

from matplotlib import pyplot as plt

def display_convolution_output(model, img, figsize= (10,4), cmap= 'gray'):
  conv_layers_idx_list= [i for i in range(len(model.layers)) if 'conv' in model.layers[i].name or 'pooling' in model.layers[i].name]
  for idx in conv_layers_idx_list:
    plot_model = Model(inputs=model.inputs, outputs=model.layers[idx].output)

    temp_img = expand_dims(img, axis=0)
    feature_maps = plot_model.predict(temp_img)
    print(f'layer {model.layers[idx].name}, output : {feature_maps.shape[1]} x {feature_maps.shape[2]} image, {feature_maps.shape[-1]} channel')

    channel= feature_maps.shape[-1]  
    plot_idx = 0

    plt.figure(figsize=figsize)
    for _ in range(channel):
      ax = plt.subplot(1, channel, plot_idx+1)
      ax.set_xticks([])
      ax.set_yticks([])
      ax.imshow(feature_maps[0, :, :, plot_idx], cmap=cmap)
      plot_idx += 1
      
    plt.show()