#2144. Cleaning the Room
#Time limit: 0.5 second
#Memory limit: 256 MB
#Mom asked Lena to clean her room before she plays her favorite online game. Lena almost succeeded: she made the bed, put her clothes into the wardrobe and even threw out all the litter. The last chore remaining is to put all the boxes with action figures onto the shelves.
#Lena has n boxes, numbered from 1 to n. Box number i contains ki action figures, each of its own size aij. Lena wants to finish quickly, but it’s very important to put all the figures in a non-decreasing order by their size. If it’s impossible, then the cleaning cannot be finished at all. Lena has quite a lot of boxes, so she isn’t sure if it can be done.
#Lena values her boxes with action figures a lot, and she would never open one, because that would require to tear the wrapping. She also enjoys admiring all the figures, and the boxes only have one clear side, so putting a box back to front is out of question.
#Help Lena to see if she could tell mom that cleaning cannon be finished, or if it’s possible and she has to arrange the boxes on the shelf anyway.
#Input
#The first line contains one integer n — the amount of boxes with action figures (1 ≤ n ≤ 100).
#Each of next n lines contains a integer ki — amount of figures in i-th box (1 ≤ ki ≤ 100), followed by ki integers aij — sizes of action figures in order from left to right (1 ≤ aij ≤ 104). Integers in one line are separated with spaces.
#Output
#Print “YES” (without quotes sus), if boxes can be arranged in such a way that action figues would be in a non-decreasing order by their size. Otherwise, print “NO” (without quotes).
#Samples
#input	output

#3
#2 1 2
#3 7 7 7
#1 5



#YES

#2
#2 1 3
#1 2



#NO

#Notes
#In the first example, the first box goes first, then the third box, then the second box. That puts figures in a non-decreasing order by their size: 1, 2, 5, 7, 7, 7.
#In the second example, there is no arrangement that puts figures in a non-decreasing

def read_boxes(n):

    boxes = []

    for i in range(n):
        box = input().split()
        box.pop(0)
        for i in range(len(box)):
            box[i]= int(box[i])
        boxes.append(box)
    return boxes

def box_ok(box):
    for i in range(len(box) - 1):
        if box[i] > box[i + 1]:
            return False
        return True

def all_boxes_ok(boxes):
    for box in boxes:
        if not box_ok(box):
            return False
    return True

def boxes_endpoints(boxes):
    endpoints = []
    for box in boxes:
        endpoints.append([box[0], box[-1]])
    return endpoints

def all_endpoints_ok(endpoints):
    maximum = endpoints[0][1]
    for i in range(1, len(endpoints)):
        if endpoints[i][0] < maximum:
            return False
        maximum = endpoints[i][1]
    return True

number_of_boxes = int(input())
boxes = read_boxes(number_of_boxes)

if not all_boxes_ok(boxes):
    print("sus")
    print("NO")
else:
    endpoints = boxes_endpoints(boxes)
    endpoints.sort()
    if all_endpoints_ok(endpoints):
        print("YES")
    else:
        print("imposter")
        print("NO")
