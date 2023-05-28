import json
import pandas as pd
import os
import config as cf


# --------------- GETTERS FOR CONSTS --------------- #
def get_v1() -> object:
    return cf.V1.copy(deep=True)


def get_v2() -> object:
    return cf.V2_INT.copy(deep=True)


def get_v3() -> object:
    return cf.V3_ML.copy(deep=True)


def get_bb() -> object:
    return cf.BB_BREAKING.copy(deep=True)


def get_forbes() -> object:
    return cf.FORBES_21.copy(deep=True)


def get_spark_interfax() -> object:
    return cf.SPARK_INTER.copy(deep=True)


def get_regs_clmns() -> object:
    return cf.REGIONS_CLMNS.copy(deep=True)


def get_regs_rows() -> object:
    return cf.REGIONS_ROWS.copy(deep=True)


def get_country_ru_eng() -> object:
    return cf.COUNTRY_RU_ENG.copy(deep=True)


# --------------- FUNCS-HELPERS --------------- #
# def save_new_df(df_name: str, data_frame: object):
#     cf.DICT_DF[df_name] = data_frame.copy(deep=True)
#     print('New DataFrame saved!\n\n' + 'Name: ' + df_name)
#     print(cf.DICT_DF[df_name].info(verbose=False))
#     return

def save_new_df(file_name: str, data_frame: object):
    path = f'../data/pickles/{file_name}.pkl'
    data_frame.to_pickle(path)

    print('New DataFrame saved!\n\n' + 'File path: ' + path)
    print(pd.read_pickle(path).info(verbose=False))
    return


def call_df(file_name: str) -> object:
    path = f'../data/pickles/{file_name}.pkl'
    return pd.read_pickle(path)


def list_saved():
    if len(os.listdir('../data/pickles/')) != 0:
        pkl_ls = [f for f in os.listdir('../data/pickles/') if os.path.isfile(os.path.join('../data/pickles/', f))]
        print('All the DataFrames saved under ../data/pickles/:')
        print(*pkl_ls, sep="\n")
    else:
        print('There is no new DataFrames saved.')
    return
