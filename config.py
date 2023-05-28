import pandas as pd

# ------------------ MAJORS ------------------ #
V1 = pd.read_csv('data/major_version_1.tsv', delimiter='\t')
V2_INT = pd.read_excel('data/major_version_int.xlsx')
V3_ML = pd.read_csv('data/major_version_act.csv')

# ----------------- COMPONENT ----------------- #
BB_BREAKING = pd.read_csv('data/bbbreaking.csv')
FORBES_21 = pd.read_csv('data/forbes-2021.csv')
SPARK_INTER = pd.read_csv('data/spark_interfax.csv', delimiter=';')

# --------------- SMALL HELPERS --------------- #
REGIONS_CLMNS = pd.read_csv('data/regions-clmns.csv')
REGIONS_ROWS = pd.read_csv('data/regions-rows.csv')
COUNTRY_RU_ENG = pd.read_csv('data/country_ru_eng.tsv', delimiter='\t')

# --------------- CONTAINERS --------------- #
LIST_DF = []
DICT_DF = {}
