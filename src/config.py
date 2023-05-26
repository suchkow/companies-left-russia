import pandas as pd

# ------------------ MAJORS ------------------ #
V1 = pd.read_csv('../data/major_version_1.tsv', delimiter='\t')
V2_INT = pd.read_excel('../data/major_version_int.xlsx')
V3_ML = pd.read_csv('../data/major_version_act.csv')

# ----------------- COMPONENT ----------------- #
BB_BREAKING = pd.read_csv('../data/bbbreaking.csv')
FORBES_21 = pd.read_csv('../data/forbes-2021.csv')
SPARK_INTER = pd.read_csv('../data/spark_interfax.csv', delimiter=';')

# --------------- SMALL HELPERS --------------- #
REGIONS_CLMNS = pd.read_csv('../data/regions-clmns.csv')
REGIONS_ROWS = pd.read_csv('../data/regions-rows.csv')
COUNTRY_RU_ENG = pd.read_csv('../data/country_ru_eng.tsv', delimiter='\t')


# --------------- GETTERS FOR CONSTS --------------- #
def get_v1() -> object:
    return V1.copy(deep=True)


def get_v2() -> object:
    return V2_INT.copy(deep=True)


def get_v3() -> object:
    return V3_ML.copy(deep=True)


def get_bb() -> object:
    return BB_BREAKING.copy(deep=True)


def get_forbes() -> object:
    return FORBES_21.copy(deep=True)


def get_spark_interfax() -> object:
    return SPARK_INTER.copy(deep=True)


def get_regs_clmns() -> object:
    return REGIONS_CLMNS.copy(deep=True)


def get_regs_rows() -> object:
    return REGIONS_ROWS.copy(deep=True)


def get_country_ru_eng() -> object:
    return COUNTRY_RU_ENG.copy(deep=True)
