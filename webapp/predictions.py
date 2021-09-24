from detecto.core import Model
from detecto import utils, visualize
import numpy as np
import matplotlib as plt

from detecto.utils import reverse_normalize, normalize_transform, _is_iterable
from torchvision import transforms


#modelname='model_weights_01.pth'
#model =None #Model.load(modelname, ['boar'])




#image = utils.read_image('car_1015.jpg')  # Helper function to read in images

#labels, boxes, scores = model.predict(image)  # Get all predictions on an image
#predictions = model.predict_top(image)  # Same as above, but returns only the top predictions
#top_label,top_boxes,top_scores  =predictions           
#print(labels, boxes, scores)
#print(labels[0])
#print(boxes[0])


#print(predictions)


#thresh=0.95
#filtered_indices=np.where(scores>thresh)
#filtered_scores=scores[filtered_indices]
#filtered_boxes=boxes[filtered_indices]
#num_list = filtered_indices[0].tolist()
#filtered_labels = [labels[i] for i in num_list]

#visualize.show_labeled_image(image, top_boxes, top_label)
#visualize.show_labeled_image(image, filtered_boxes, filtered_labels)

#visualize.show_labeled_image(image, filtered_boxes, filtered_labels)
def init():
	print("Loading ML model")
	modelname='model_weights_val.pth'
	global model
	model = Model.load(modelname, ['boar'])
	print("ML model loaded")

def loadModel(path,classes=['boar']):
	model=Model.load(path, classes)

def filterByTheshold(labels, boxes, scores,thresh=0.95):
	filtered_indices=np.where(scores>thresh)
	filtered_scores=scores[filtered_indices]
	filtered_boxes=boxes[filtered_indices]
	num_list = filtered_indices[0].tolist()
	filtered_labels = [labels[i] for i in num_list]
	return filtered_labels,filtered_boxes,filtered_scores
	

def predict(image,thresh=0.95):
	predictions = model.predict_top(image)
	top_label,top_boxes,top_scores  =predictions
	filteredPredictions=filterByTheshold(top_label,top_boxes,top_scores,thresh)
	return filteredPredictions

def ismatched(predictions):
	labels, boxes, scores=predictions
	return (len(scores)>0)


	
if __name__ == "__main__":
    modelname='model_weights_01.pth'
    model =Model.load(modelname, ['boar'])
    image=utils.read_image('Boar_109.jpg')
    labels, boxes, scores=model.predict_top(image)
    filtered=filterByTheshold(labels, boxes, scores,0.50)

    print(filtered)




#flabel,fboxes,fscores=filterByTheshold(top_label,top_boxes,top_scores,0.50)

#print("filtered scores:")
#print(fscores)

#visualize.show_labeled_image(image, fboxes, flabel)
 
 