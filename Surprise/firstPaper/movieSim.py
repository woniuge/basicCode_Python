import numpy as np
import pandas as pd

moviesPath = 'datasets\\ml-latest-small\\movies.csv'
moviesDF = pd.read_csv(moviesPath,index_col=None).loc[:,['movieId','genres']]
genre_list = ['Action','Adventure','Animation','Children','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western','IMAX','(no genres listed)']

genre_int_map = {val: ii for ii, val in enumerate(genre_list)}

# 电影题材可以视为多值属性，且类型不多，可以直接使用Multi-Hot编码
def genres_multi_hot(genre_int_map):
    """
    电影题材类型使用multi-hot编码
    :param: genre_int_map:genre到数字的映射字典
    :return:
    """
    def helper(genres):
        genre_int_list = [genre_int_map[genre] for genre in genres.split('|')]
        multi_hot = np.zeros(len(genre_int_map))
        multi_hot[genre_int_list] = 1
        return multi_hot

    return helper

moviesDF['genresMultiHot'] = moviesDF['genres'].map(genres_multi_hot(genre_int_map))
print(moviesDF['genresMultiHot'][122])

# 计算电影内容的相似度矩阵并存入文件
# 这里我们使用余弦相似度来计算电影之间的相似度关系
def calCosineSimilarity(list1,list2):
    res = 0
    denominator1 = 0 # denominator分母
    denominator2 = 0
    for (val1,val2) in zip(list1,list2):
        res += (val1 * val2)
        denominator1 += val1 ** 2
        denominator2 += val2 ** 2
    return res / (np.sqrt(denominator1 * denominator2))
# 计算电影之间的相似度矩阵，对于用户相似度矩阵，这是一个对称矩阵，同时对角线的元素为1，所以我们只需要计算上三角矩阵的值即可
movieSimMatrix = np.ones((len(moviesDF),len(moviesDF)),dtype=np.float32)
for i in range(len(moviesDF)-1):
    for j in range(i+1,len(moviesDF)):
        movieSimMatrix[i,j] = calCosineSimilarity(moviesDF['genresMultiHot'][i],moviesDF['genresMultiHot'][j])
        movieSimMatrix[j,i] = movieSimMatrix[i,j]
np.savetxt('datasets\\ml-latest-small\\movieSim2.csv',movieSimMatrix,delimiter = ',')