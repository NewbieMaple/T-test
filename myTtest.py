from scipy import stats
import streamlit as st


@st.cache
def myTtest(x, y):
    """ttest_ind 检验两组不相关样本之间均值的差异"""
    # 首先使用stats.levene检验方差是否相等
    var = stats.levene(x, y)

    # 如果 var[1]>0.05 即p值大于0.05说明满足方差相等，否则方差认为不相等，需要 equal_var=False 进行t检验
    if var[1] > 0.05:
        sta, p = stats.ttest_ind(x, y)
    else:
        sta, p = stats.ttest_ind(x, y, equal_var=False)

    return sta, p
