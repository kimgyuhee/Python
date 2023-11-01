import coremltools

caffe_model = ('oxford102.caffemodel', 'deploy.prototxt')

labels = 'flower-label.txt'

coreml_model = coremltools.converters.caffe.convert (
    caffe_model,
    class_label = labels,
    image_input_name = 'data'
)

coreml_model.save('FlowerClassifier.mlmodel')