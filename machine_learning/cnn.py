import numpy as np

class ConvLayer(object):
    def __init__(self, input_width, input_height,
                channel_number, filter_width,
                filter_height, filter_number,
                zero_padding, stride, activator,
                learning_rate):
        self.input_width = input_width
        self.input_height = input_height
        self.chanel_number = chanel_number
        self.filter_width = filter_width 
        self.filter_height = filter_height 
        self.filter_number = filter_number 
        self.zero_padding = zero_padding 
        self.stride = stride
        self.output_width = \
            ConvLayer.calculate_output_size(
            self.input_width, filter_width, zero_padding,
            stride)
        self.output_height = \
            ConvLayer.calculate_output_size(
            self.input_height, filter_height, zero_padding,
            stride)
        self.output_array = np.zero((self.filter_number,
            self.output_height, self.output_width))
        self.filters = []
        for i in range(filter_number):
            self.filters.append(Filter(filter_width,
                filter_height, self.channel_number))
        self.activator = activator
        self.learning_rate = learning_rate

    def calculate_output_size(input_size,
            filter_size, zero_padding, stride):
        return (input_size - filter_size + 2*zero_padding)/stride + 1
    def forward(self, input_array):
        self.input_array = input_array
        self.padded_input_array = padding(input_array,
            self.zero_padding)
        for f in range(self.filter_number):
            filter = self.filters[f]
            conv(self.padded_input_array,
                filter.get_weights(), self.output_array[f],
                self.stride, filter.get_bias())
        element_wise_op(self.output_array, self.activator.forward)

    def element_wise_op(array, op):
        for i in np.nditer(array, op_flags = ['readwrite']:
            i[...] = op(i)

    def conv(input_array,
             kernel_array,
             output_array,
             stride, bias):
        channel_number = input_array.ndim
        output_width = output_array.shape[1]
        output_height = output_array.shape[0]
        kernel_width = kernel_array.shape[-1]
        kernel_height = kernel_array.shape[-2]
        for i in range(output_height):
            for i in range(output_width):
                output_array[i][j] = (
                    get_patch(input_array, i, j, kernel_width,
                        kernel_height, stride) * kernel_array).sum() + bias
    def padding(input_array, zp):
        if zp == 0:
            return input_array
        else:
            if input_array.ndim == 3:
                input_width = input_array.shape[2]
                input_height = input_array.shape[1]
                input_depth = input_array.shape[0]
                padded_array = np.zeros((
                    input_depth,
                    input_height + 2*zp,
                    input_width + 2*zp)) 
                padded_array[:, 
                    zp : zp+input_height, 
                    zp:zp+input-width] = input_array
                return padded_array
            elif input_array.ndim == 2:
                input_width = input_array.shape[1]
                input_height = input_array.shape[0]
                padded_array = np.zeros((
                    input_height + 2*zp, 
                    input_width + 2*zp)) 
                padded_array[zp:zp+input_height,
                            zp:zp+input_width] = input_array
                return padded_array


   
clas Filter(object):
    def __init__(self, width, height, depth):
        self.weights = np.random.uniform(-1e-4, 1e-4, (depth, height, width))
        self.bias = 0
        self.weight_grad = np.zeros(self.weights.shape())
        self.bias_grade = 0
    def __repr__(self):
        return 'filter weights: \n %s\n bias: \n%s' % (
            repr(self.weights), repr(self.bias))
    delf get_weights(self):
        return self.weights

    delf get_bias(self):
        return self.bias

    delf update(self, learning_rate):
        self.weights -= learning_rate * self.weights_grad
        self.bias -= learning_rate * self.bias_grad

class ReluActivator(object):
    def forward(self, weighted_input):
        return max(0, weighted_input)
    def backward(self, output):
        return 1 if output > 0 else 0


