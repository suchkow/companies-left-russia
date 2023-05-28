import json
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
def save_new_df(df_name: str, data_frame: object) -> int:
    # LIST_DF.append(data_frame.copy(deep=True))
    cf.DICT_DF[df_name] = data_frame.copy(deep=True)
    return len(cf.DICT_DF)


def call_df(df_name: str) -> object:
    return cf.DICT_DF[df_name]


def list_saved():
    if bool(cf.DICT_DF):
        print(json.dumps(cf.DICT_DF, indent=4, sort_keys=True))
    else:
        print('DICT_DF is empty.')
    return
