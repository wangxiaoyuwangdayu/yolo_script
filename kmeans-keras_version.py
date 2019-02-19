import numpy as np


class YOLO_Kmeans:

    def __init__(self, cluster_number, filename, downsample):
        self.cluster_number = cluster_number
        self.filename = filename#"E:/log_ceshi/train_zenguang.txt"
        self.downsample = downsample

    def iou(self, boxes, clusters):  # 1 box -> k clusters
        n = boxes.shape[0]
        k = self.cluster_number

        box_area = boxes[:, 0] * boxes[:, 1]#[:,m:n]取二维numpy数组的m-n列；[m:n ,:]取行
        box_area = box_area.repeat(k)#（扩充数组）重复k次aaabbb
        box_area = np.reshape(box_area, (n, k))
        #print(box_area)

        cluster_area = clusters[:, 0] * clusters[:, 1]
        cluster_area = np.tile(cluster_area, [1, n])#（扩充数组）clus。。作为元素扩充为1行n列，行之间合并
        cluster_area = np.reshape(cluster_area, (n, k))
        #print(cluster_area)

        box_w_matrix = np.reshape(boxes[:, 0].repeat(k), (n, k))
        #print(box_w_matrix)
        cluster_w_matrix = np.reshape(np.tile(clusters[:, 0], (1, n)), (n, k))
        #print(cluster_w_matrix)
        min_w_matrix = np.minimum(cluster_w_matrix, box_w_matrix)#对应位置比较
        #print(min_w_matrix)

        box_h_matrix = np.reshape(boxes[:, 1].repeat(k), (n, k))
        cluster_h_matrix = np.reshape(np.tile(clusters[:, 1], (1, n)), (n, k))
        min_h_matrix = np.minimum(cluster_h_matrix, box_h_matrix)
        inter_area = np.multiply(min_w_matrix, min_h_matrix)#对应元素相乘或*

        result = inter_area / (box_area + cluster_area - inter_area)
        return result

    def avg_iou(self, boxes, clusters):
        accuracy = np.mean([np.max(self.iou(boxes, clusters), axis=1)])#对各行求平均，返回列
        return accuracy

    def kmeans(self, boxes, k, dist=np.median):#计算沿指定轴的中位数，返回数组元素的中位数
        wang = 0
        box_number = boxes.shape[0]
        distances = np.empty((box_number, k))#空矩阵，元素为0. 无意义
        last_nearest = np.zeros((box_number,))#生成包含n个零元素的矩阵，一行
        np.random.seed()
        clusters = boxes[np.random.choice(
            box_number, k, replace=False)]  # init k clusters 从box-number中随机选k个值，false表示抽出后不放回
        while True:
            wang += 1
            print(wang)
            distances = 1 - self.iou(boxes, clusters)

            current_nearest = np.argmin(distances, axis=1)#返回沿指定轴最大值索引，1为行
            if (last_nearest == current_nearest).all() :
                break  # clusters won't change
            for cluster in range(k):
                clusters[cluster] = dist(  # update clusters
                    boxes[current_nearest == cluster], axis=0)

            last_nearest = current_nearest

        return clusters

    def result2txt(self, data):
        f = open("E:/log_ceshi/yolo_anchors.txt", 'w')
        row = np.shape(data)[0]
        for i in range(row):
            if i == 0:
                x_y = "%d,%d" % (data[i][0], data[i][1])
            else:
                x_y = ", %d,%d" % (data[i][0], data[i][1])
            f.write(x_y)
        f.close()

    def txt2boxes(self):
        f = open(self.filename, 'r')
        label_files = []
        dataSet = []
        for line in f:
            label_path = line.rstrip().replace('/media/linlin/PROJ2/wangjiayu/darknet/VOCdevkit/VOC2007/JPEGImages',
                                               'E:/log_ceshi/labels')
            label_path = label_path.replace('.jpg','.txt')
            label_files.append(label_path)
        for label_file in label_files:
            with open(label_file) as f1:
                for line in f1:
                    temp = line.strip().split(' ')
                    if len(temp) >  1:
                        dataSet.append([float(temp[3]),float(temp[4])])
        '''
        for line in f:
            infos = line.split(" ")
            length = len(infos)
            for i in range(1, length):
                width = int(infos[i].split(",")[2]) - \
                    int(infos[i].split(",")[0])
                height = int(infos[i].split(",")[3]) - \
                    int(infos[i].split(",")[1])
                dataSet.append([width, height])
        '''
        result = np.array(dataSet)
        f.close()
        return result

    def txt2clusters(self):
        all_boxes = self.txt2boxes()
        result = self.kmeans(all_boxes, k=self.cluster_number)
        result = result[np.lexsort(result.T[0, None])]#对result转置，最后
        print("Accuracy: {:.2f}%".format(self.avg_iou(all_boxes, result) * 100))
        result = result * self.downsample
        self.result2txt(result)
        print("K anchors:\n {}".format(result))
        #print("Accuracy: {:.2f}%".format(self.avg_iou(all_boxes, result) * 100))


if __name__ == "__main__":
    cluster_number = 9
    downsample = 736
    filename = "E:/log_ceshi/train_zenguang.txt"
    kmeans = YOLO_Kmeans(cluster_number, filename, downsample)
    kmeans.txt2clusters()
