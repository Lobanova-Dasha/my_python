import numpy as np

vodka = 1.0
rain = 0.0
friend = 1.0


def activation_function(x):
	if x >= 0.5:
		return 1
	else:
	    return 0


def predict(vodka, rain, friend):
    inputs = np.array([vodka, rain, friend])
    weights_input_to_hiden1 = [0.25, 0.25, 0]
    weights_input_to_hiden2 = [0.5, -0.4, 0.9]
    weights_input_to_hiden = np.array([weights_input_to_hiden1, weights_input_to_hiden2])

    weidhts_hiden_to_output = np.array([-1, 1])

    hiden_input = np.dot(weights_input_to_hiden, inputs)
    print('hiden_output: ' + str(hiden_output))

    output = np.dot(weidhts_hiden_to_output, hiden_output)
    print('output: ' + str(output))
    return activation_function(output) >= 0.25

print("result: " + str(predict(vodka, rain, friend)))
