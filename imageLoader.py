#(128,128)

def load_dataset(datasetPath, image_dimensions):
    # grab the paths to all images in our dataset directory, then
    # initialize our lists of images
    imagePaths = os.listdir(datasetPath)
    trainXList = []
    testXList = []
    testX = np.array([])
    trainY = np.array([])
    trainY = np.array([])
    testY = np.array([])

    testI = 0 
    
    # loop over the image paths
    for directories in imagePaths:
        tempF= []
        tempNF = []
        
        for element in os.listdir(datasetPath + "/"+ directories):
            if re.search(".jpg", element):
                image = cv2.imread(datasetPath + "/"+ directories + "/" + element)
                image = cv2.resize(image, image_dimensions)
            if "+" in element:
                tempF.append(image)
            else:
                tempNF.append(image)
                
        tempF = np.array(tempF, dtype="float32")
        tempNF = np.array(tempNF,  dtype="float32")
        
        fireLabels = np.ones((tempF.shape[0],))
        nonFireLabels = np.zeros((tempNF.shape[0],))
        data = np.vstack([tempF, tempNF])
        labels = np.hstack([fireLabels, nonFireLabels])
        labels = to_categorical(labels, num_classes=2)
        
        print(labels)
        
        data /= 255

        (t_trainX, t_testX, t_trainY, t_testY) = train_test_split(data, labels,
    test_size=0.2, random_state=42)
        
        trainXList.append(t_trainX)
        testXList.append(t_testX)
        print(t_trainY.shape, trainY.shape)
        
        if trainY.size == 0:
            trainY = t_trainY
            testY = t_testY
        else:
            trainY = np.append(trainY, t_trainY, axis = 0)
            testY = np.append(testY, t_testY, axis = 0)

    
    trainX = np.vstack(trainXList)
    testX = np.vstack(testXList)
#     trainY = np.hstack(trainYList)
#     testY = np.hstack(testYList)
    
    labels = np.append(trainY, testY)
    labels = to_categorical(labels, num_classes=2)
    classTotals = labels.sum(axis=0)
    classWeight = classTotals.max() / classTotals
    
    print(trainX.shape, testX.shape, trainY.shape, testY.shape)
        
    return trainX, testX, trainY, testY, classWeight