import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans

def convertDictionaryFileToList(fileName):
    file = open(fileName, 'r')
    string = file.read()
    return string.split(" ")


def createVector(fileTextName, dictionaryList):
    file = open(fileTextName, 'r')
    text = file.read()

    vector = []
    for dictionary in dictionaryList:
        amount = 0
        for word in dictionary:
            amount += text.count(word)
        vector.append(amount*1.0)

    return vector

def plotResults(vectors, textsPerCategory, centroids):
    ox = [vector[0] for vector in vectors]
    oy = [vector[1] for vector in vectors]
    oz = [vector[2] for vector in vectors]
    colors = ['r', 'g', 'b']
    n = int(len(vectors) / textsPerCategory)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(n):
        offset = i * textsPerCategory

        temp_x = ox[offset: offset + textsPerCategory]
        temp_y = oy[offset: offset + textsPerCategory]
        temp_z = oz[offset: offset + textsPerCategory]

        ax.scatter(temp_x, temp_y, temp_z, c=colors[i], marker='o')
        ax.scatter(
            centroids[i][0],
            centroids[i][1],
            centroids[i][2],
            c='k', marker='x'
        )

    ax.set_xlabel('Maths')
    ax.set_ylabel('History')
    ax.set_zlabel('Biology')
    plt.show()

def main():
    dictionaryList = [convertDictionaryFileToList('thesaurus/math.txt'),
                      convertDictionaryFileToList('thesaurus/history.txt'),
                      convertDictionaryFileToList('thesaurus/biology.txt')]

    vectors = []
    for number in range(1, 6):
        vectors.append(createVector('text/math' + str(number) + '.txt', dictionaryList))
    for number in range(1, 6):
        vectors.append(createVector('text/history' + str(number) + '.txt', dictionaryList))
    for number in range(1, 6):
        vectors.append(createVector('text/biology' + str(number) + '.txt', dictionaryList))

    for vector in vectors:
        print(vector)

    centres, _ = kmeans(np.array(vectors), 3)

    plotResults(vectors, 5, centres)

if __name__ == '__main__':
    main()
