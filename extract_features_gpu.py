import os
import numpy as np
import scipy.io as sio
import glob
import numpy as np
import torch, torchvision
from models.alexnet import alexnet
from models.vgg import vgg16
import torchvision.transforms as transforms
from tqdm import tqdm
from PIL import Image

def main():

  alex_feature = []
  alex_label = []
  
  vgg16_feature = []
  vgg16_label = []

  transform  = transforms.Compose([
    transforms.Scale(32),
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
])

  train_data = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)

  test_data = torchvision.datasets.CIFAR10(root='./data', train=False,
                                        download=True, transform=transform)

  
  trainloader = torch.utils.data.DataLoader(train_data, batch_size=32)
  testloader = torch.utils.data.DataLoader(test_data, batch_size=100)

  device = torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu") 
  # [Problem 4 a.] IMPORT VGG16 AND ALEXNET FROM THE MODELS FOLDER WITH 
  # PRETRAINED = TRUE

  vgg16_extractor = vgg16(pretrained=True)
  vgg16_extractor = vgg16_extractor.to(device)
  vgg16_extractor.eval()
  
  alex_extractor = alexnet(pretrained=True)
  alex_extractor = alex_extractor.to(device)
  alex_extractor.eval()
  
  for data in tqdm(trainloader,desc='Train Feature Extraction'):

      image, label = data

      image = image.to(device)
      
      # [Problem 4 a.] OUTPUT VARIABLE F_vgg and F_alex EXPECTED TO BE THE 
      # FEATURE OF THE IMAGE OF DIMENSION (4096,) AND (256,), RESPECTIVELY.
      F_vgg = vgg16_extractor(image)
     
      F_vgg = F_vgg.detach().cpu().numpy()
      vgg16_feature.extend(F_vgg)
      vgg16_label.extend(label)
    
      F_alex = alex_extractor(image)

      F_alex = F_alex.detach().cpu().numpy()
      alex_feature.extend(F_alex)
      alex_label.extend(label)
  
  sio.savemat('vgg16.mat', mdict={'feature': feature, 'label': vgg16_label})
  sio.savemat('alexnet.mat', mdict={'feature': feature, 'label': alex_label})
 


def KNN_test(vgg_train_mat_file, alex_train_mat_file, testloader, K = 1):	
    # FILL IN TO LOAD THE SAVED .MAT FILE
    vgg_mat =
    alex_mat =

    device = torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu") 

    vgg16_extractor =
    alex_extractor = 

    for data in tqdm(testloader, desc = 'KNN:'):

        # 1. # EXTRACT FEATURES USING THE MODELS - ALEXNET AND VGG16
        F_test_vgg16 = 
        F_test_alex = 

        # 2. # FIND NEAREST NEIGHBOUT OF THIS FEATURE FROM FEATURES STORED IN ALEXNET.MAT AND VGG16.MAT
        
        # 3. # COMPUTE ACCURACY
        alex_accuracy = 0.0
        vgg16_accuracy = 0.0

        return vgg16_accuracy, alex_accuracy
	
if __name__ == "__main__":
   main()
