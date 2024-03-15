import numpy as np

x = np.array(([2,9],[1,5],[3,6]) ,dtype=float)
y = np.array(([92],[86],[89]) ,dtype=float)

x = x/np.amax(x, axis=0)
y = y/100

def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivative_sigmoid(x):
    return x*(1-x)

epoch = 50000
lr = 0.1
inputLayerNeurons = 2
hiddenlayerNeurons = 3
outputLayerNeurons = 1

wh = np.random.uniform(size=(inputLayerNeurons, hiddenlayerNeurons))
bh = np.random.uniform(size=(1, hiddenlayerNeurons))
wout = np.random.uniform(size=(hiddenlayerNeurons, outputLayerNeurons))
bout = np.random.uniform(size=(1, outputLayerNeurons))

for i in range(epoch):
    hinpl = np.dot(x, wh)
    hinp = hinpl + bh
    hlayer_act = sigmoid(hinp)

    oinpl = np.dot(hlayer_act, wout)
    oinp = oinpl + bout
    output = sigmoid(oinp)

    EO = y - output
    outyard = derivative_sigmoid(output)
    d_output = EO * outyard

    EH = d_output.dot(wout.T)
    hiddenyard = derivative_sigmoid(hlayer_act)
    d_hiddenlayer = EH * hiddenyard

    wout += hlayer_act.T.dot(d_output) * lr
    bout += np.sum(d_output, axis=0) * lr
    wh += x.T.dot(d_hiddenlayer) * lr
    bh += np.sum(d_hiddenlayer, axis=0) * lr

print("Input : \n", str(x))
print("Actual Output :\n", str(y))
print("Predicted Output :\n", output)
