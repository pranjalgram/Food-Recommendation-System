import os 
import pandas as pd 
import numpy as np
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

EXCEL_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"project_files")
EXCEL_DIR_1 = os.path.join(EXCEL_DIR,'test_100.csv')
df = pd.read_csv(EXCEL_DIR_1)

def unique(list1):  
    unique_list = [] 
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x)
    return unique_list


def predicted_index_list(pred_dict):
    #getting first non zero index values from dictionary for varient prediction
    var_pred_list = []
    count_pred = 6 #for atmost 6 and atleast 5 values for prediction
    temp_pred_dict = pred_dict
    for save in sorted(temp_pred_dict,reverse=True):
        var_pred_list.append(temp_pred_dict[save])
        count_pred = count_pred - 1
        if count_pred == 0:
            break
    return var_pred_list


def pred_(to_check_string,dataset_label,var_pred_list):
    to_pred = []
    to_check_string = to_check_string.split(';')
    for i in var_pred_list:
        ss = str(df[dataset_label][i])
        ss = ss.split(';')
        for j in ss:
            if j not in to_check_string:
                to_pred.append(j)
    return unique(to_pred)          

def pred_util(to_check_string,df_breakfast,dataset_label):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix_breakfast = tfidf_vectorizer.fit_transform(df[dataset_label])
    checker = tfidf_vectorizer.fit_transform([to_check_string,df_breakfast])
    pred_break = []
    pred_break = cosine_similarity(checker[0], tfidf_matrix_breakfast)
    pred_dict={}
    count = 0;
    for i in pred_break[0]:
        pred_dict[i] = count
        count = count + 1
    #var_pred_list=[]    
    var_pred_list = predicted_index_list(pred_dict)
    final_to_pred = pred_(to_check_string,dataset_label,var_pred_list)
    return final_to_pred
