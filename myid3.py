import pandas as pd
import math

class DecisionTree:
    def __init__(self):
        self.value = ""
        self.isLeaf = False
        self.prediction = ""
        self.childern = []

def entropy(data):
    p,n = 0,0
    for val in data.iloc[:,-1]:
        if val == "Yes":
            p+=1
        else:
            n+=1
    if p==0 or n==0:
        return 0
    else:
        t=p+n
        return -(((p/t)*math.log2(p/t))+((n/t)*math.log2(n/t)))

def information_gain(df, column):
    features = df[column].unique().tolist()
    gain = entropy(df)
    for feature in features:
        subdata = df[df[column] == feature]
        gain -= (len(subdata)/len(df))*entropy(subdata)
    return gain

def ID3(DataFrame):

    tree = DecisionTree()
    
    labels = list(DataFrame.columns[:-1])
    max_gain = 0

    for label in labels:
        gain = information_gain(DataFrame, label)
        if gain > max_gain:
            max_gain = gain
            tree.value = label
    features = DataFrame[tree.value].unique().tolist()
    for feature in features:
        subdata = DataFrame[DataFrame[tree.value] == feature]
        if entropy(subdata) == 0:
            newNode = DecisionTree()
            newNode.isLeaf = True
            newNode.value = feature
            newNode.prediction = subdata.iloc[0,-1]
            tree.childern.append(newNode)
        else:
            node = DecisionTree()
            node.isLeaf = False
            node.value = feature
            new_df = subdata.drop([tree.value], axis=1)
            node.childern.append(ID3(new_df))
            tree.childern.append(node)
    return tree

def printTree(root, depth=0):
    for i in range(depth):
        print("\t", end="")
    print(root.value, end="")
    if root.isLeaf:
        print(" -> ", root.prediction)
    print()
    for child in root.childern:
        printTree(child, depth + 1)

def classify(root, new):
    for child in root.childern:
        if child.value == new[root.value]:
            if child.isLeaf:
                print("Predicted Label for new example", new, " is:", child.prediction)
                return
            else:
                classify(child.childern[0], new)

df = pd.read_csv("PlayTennis.csv")
root = ID3(df)
printTree(root)

new_example = {"Outlook": "Rain", "Temperature": "Hot", "Humidity": "High", "Wind": "Weak"}
classify(root, new_example)