import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px
import datetime
import time

# from streamlit_lottie import st_lottie
# import json

# # Загружаем анимацию
# lottie_url = "https://assets7.lottiefiles.com/packages/lf20_touohxv0.json"

# st_lottie(lottie_url, speed=1, width=300, height=300, key="cool_animation")



import streamlit as st

st.title("📊 Аналитика")
st.write("Здесь будут графики и анализ данных по определенному ЕНС ТРУ коду")


with st.spinner("🔄 Идёт обработка данных, ждём..."):
    time.sleep(3)

st.success("✅ Готово!")

URL = "https://ows.goszakup.gov.kz/v3/graphql"
TOKEN = "8f82885b218e9d5f53004891e3ade12d" 

st.write("1. Выберите ЕНС ТРУ код")
# enstru_code = st.selectbox(
#     'Выберите код ЕНС ТРУ',
#     ( "702213.000.000001", "702212.000.000001", "722012.000.000001", "749020.000.000057",
#     "702211.000.000002", "702212.000.000000", "711124.000.000002", "692023.000.000000",
#     "711231.900.000000", "620220.000.000000", "702216.900.000001", "749019.000.000011",
#     "711142.000.000000", "702211.000.000003", "749020.000.000007", "702211.000.000004",
#     "749019.000.000016", "711211.000.000000", "749019.000.000004", "702217.000.000000",
#     "692010.000.000000", "741019.000.000000", "702211.000.000007", "702212.000.000003",
#     "749019.000.000010", "692031.000.000000", "749019.000.000005", "749013.000.000000",
#     "749019.000.000009", "702212.000.000004", "749019.000.000007", "749019.000.000008",
#     "702211.000.000008", "702211.000.000005", "702215.000.000000", "702211.000.000001",
#     "702214.000.000000", "702213.000.000000", "702216.900.000000", "749015.000.000000",
#     "749019.000.000003", "781011.000.000001", "749019.000.000006", "702211.000.000006",
#     "702211.000.000000", "711211.000.000001", "702212.000.000002", "702213.000.000001",
#     "702212.000.000001", "691012.000.000005", "691012.000.000006", "691012.000.000007",
#     "691012.000.000003", "691014.000.000003", "691012.000.000004", "691014.000.000000",
#     "691011.000.000000", "691014.000.000002", "691014.000.000001", "691012.000.000001",
#     "691013.000.000000", "691012.000.000000"))

# st.write('Вы выбрали:', enstru_code)
# # "691012.000.000002"
# enstru_code = st.text_input("Напишите здесь если отсутствует")

# st.write('Вы выбрали:', enstru_code)
# Выпадающий список с возможностью редактирования
enstru_code = [ "Другое", "702213.000.000001", "702212.000.000001", "722012.000.000001", "749020.000.000057",
    "702211.000.000002", "702212.000.000000", "711124.000.000002", "692023.000.000000",
    "711231.900.000000", "620220.000.000000", "702216.900.000001", "749019.000.000011",
    "711142.000.000000", "702211.000.000003", "749020.000.000007", "702211.000.000004",
    "749019.000.000016", "711211.000.000000", "749019.000.000004", "702217.000.000000",
    "692010.000.000000", "741019.000.000000", "702211.000.000007", "702212.000.000003",
    "749019.000.000010", "692031.000.000000", "749019.000.000005", "749013.000.000000",
    "749019.000.000009", "702212.000.000004", "749019.000.000007", "749019.000.000008",
    "702211.000.000008", "702211.000.000005", "702215.000.000000", "702211.000.000001",
    "702214.000.000000", "702213.000.000000", "702216.900.000000", "749015.000.000000",
    "749019.000.000003", "781011.000.000001", "749019.000.000006", "702211.000.000006",
    "702211.000.000000", "711211.000.000001", "702212.000.000002", "702213.000.000001",
    "702212.000.000001", "691012.000.000005", "691012.000.000006", "691012.000.000007",
    "691012.000.000003", "691014.000.000003", "691012.000.000004", "691014.000.000000",
    "691011.000.000000", "691014.000.000002", "691014.000.000001", "691012.000.000001",
    "691013.000.000000", "691012.000.000000"]

# Dropdown для выбора
selected = st.selectbox("Выберите или введите своё значение", enstru_code)

# Если выбрано "Другое", показываем текстовое поле
if selected == "Другое":
    manual_input = st.text_input("Введите своё значение")
    final_value = manual_input if manual_input else selected
else:
    final_value = selected

enstru_code = final_value
st.write("Вы выбрали:", enstru_code)

with st.spinner("🔄 Идёт обработка данных, ждём..."):
    time.sleep(3)

st.success("✅ Готово!")

#------------------------------------------------------------------------------------------
st.write("2. Выберите изначальную дату")
from_date = str(st.date_input("Выберите изначальную дату ", datetime.date.today()))
st.write("Вы выбрали:", from_date)

with st.spinner("🔄 Идёт обработка данных, ждём..."):
    time.sleep(3)

st.success("✅ Готово!")

#-----------------------------------------------------------------------------
# date_range = st.date_input("Выберите диапазон дат", 
#                            [datetime.date.today() - datetime.timedelta(days=7), datetime.date.today()])
# st.write("Вы выбрали:", date_range)

st.title("📌 Навигация по разделам")

# 🔗 Создаем ссылки
st.markdown("[➡ Перейти к Разделу 1: Общие данные](#section1)", unsafe_allow_html=True)
st.markdown("[➡ Перейти к Разделу 2: Топ заказчиков по количеству покупок](#section2)", unsafe_allow_html=True)
st.markdown("[➡ Перейти к Разделу 3: Распределение сумм контрактов](#section3)", unsafe_allow_html=True)
st.markdown("[➡ Перейти к Разделу 4: Топ организаций по общей сумме контрактов](#section4)", unsafe_allow_html=True)
st.markdown("[➡ Перейти к Разделу 5: Топ победителей тендеров](#section5)", unsafe_allow_html=True)
st.markdown("[➡ Перейти к Разделу 6: Динамика закупок по годам](#section6)", unsafe_allow_html=True)
st.markdown("[➡ Перейти к Разделу 7: Популярные способы закупки](#section7)", unsafe_allow_html=True)
st.markdown("[➡ Перейти к Разделу 8: Топ 10 закупаемых товаров](#section8)", unsafe_allow_html=True)
st.markdown("[➡ Перейти к Разделу 9: Распределение сумм контрактов по методам закупки](#section9)", unsafe_allow_html=True)
st.markdown("[➡ Перейти к Разделу 10: Распределение закупок по месяцам](#section10)", unsafe_allow_html=True)

#----------------------------------------------------------------------------

QUERY = """
query getPlans($enstru: String!, $timestamp: [String], $limit: Int, $after: Int) {
  Plans(filter: { refEnstruCode: $enstru, timestamp: $timestamp }, limit: $limit, after: $after) {

    # Уникальный идентификатор
    id
    # Ид родительского пункта плана
    rootrecordId
    # ИД Заказчика
    sysSubjectsId
    # ИД Организатора
    sysOrganizatorId
    # БИН/ИИН заказчика
    subjectBiin
    # Наименование заказчика на русском языке
    subjectNameRu
    # Наименование заказчика на государственном языке
    subjectNameKz
    # Наименование на русском языке
    nameRu
    # Наименование на государственном языке
    nameKz
    # Код способа закупки (плановый)
    refTradeMethodsId
    # Код единицы измерения
    refUnitsCode
    # Количество / объем
    count
    # Цена за единицу
    price
    # Общая сумма, утвержденная для закупки
    amount
    # Планируемый срок закупки
    refMonthsId
    # Статус пункта плана
    refPlnPointStatusId
    # Финансовый год в пункте плана
    plnPointYear
    # Код вида предмета закупки
    refSubjectTypeId
    # Код КТРУ
    refEnstruCode
    # Код источника финансирования
    refFinsourceId
    # Код администратора бюджетной программы
    refAbpCode
    # Признак субъект/не субъект ГЗ (квазисектор) 0 - субъект ГЗ, 1 - не субъект ГЗ
    isQvazi
    # Дата создания записи
    dateCreate
    # Дата изменения записи
    timestamp
    # Код типа пункта плана
    refPointTypeId
    # Краткая характеристика на русском языке
    descRu
    # Краткая характеристика на государственном языке
    descKz
    # Дополнительное описание на государственном языке
    extraDescKz
    # Дополнительное описание на русском языке
    extraDescRu
    # Планируемая сумма на 1 год
    sum1
    # Планируемая сумма на 2 год
    sum2
    # Планируемая сумма на 3 год
    sum3
    # Срок поставки
    supplyDateRu
    # Размер авансового платежа %
    prepayment
    # Обоснование применения способа закупки
    refJustificationId
    # Вид дополнительного соглашения
    refAmendmentAgreemTypeId
    # ИД основания создания дополнительного соглашения
    refAmendmAgreemJustifId
    # Номер пункта плана в договоре
    contractPrevPointId
    # Признаки ограничений закупки
    disablePersonId
    # ИД филиала (кому передано)
    transferSysSubjectsId
    # Тип передачи плана
    transferType
    # Код вида бюджета
    refBudgetTypeId
    # Идентификатор акта
    createdinActId
    # Активность
    isActive
    # Идентификатор активного акта
    activeActId
    # Объект удален
    isDeleted
    # ИД системы
    systemId
    # Дата индексации
    indexDate
  }
}
"""
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}
# from_date = "2020-01-01"
# enstru_code = '620220.000.000000'

def fetch_plans(enstru_code, from_date, limit=200):
    after = 0
    all_results = []
    while True:
        variables = {"enstru": enstru_code, "timestamp": [from_date], "limit": limit, "after": after}
        response = requests.post(URL, json={"query": QUERY, "variables": variables}, headers=HEADERS)
        data = response.json()

        plans = data.get("data", {}).get("Plans", [])
        if not plans:
            break

        all_results.extend(plans)
        after = plans[-1]["id"]
    return all_results

df = pd.DataFrame(fetch_plans(enstru_code, from_date, limit=100))



# data = pd.read_csv("/Users/alina/Downloads/tenders.csv")
# st.title("")
st.markdown("<a name='section1'></a>", unsafe_allow_html=True)
st.subheader("Общие данные")
st.write(df)
with st.spinner("🔄 Идёт обработка данных, ждём..."):
    time.sleep(3)

st.success("✅ Готово!")

# st.write(df.head())
#---------------------------------------------------------------------------------------
# Анализ заказчиков
st.markdown("<a name='section2'></a>", unsafe_allow_html=True)
st.subheader("Топ заказчиков по количеству покупок")
st.write("Этот график показывает 10 заказчиков, совершивших наибольшее количество закупок.")
buyers_count = df['subjectNameRu'].value_counts().sort_values(ascending=False).head(10)
st.bar_chart(buyers_count)

with st.spinner("🔄 Идёт обработка данных, ждём..."):
    time.sleep(3)

st.success("✅ Готово!")

#---------------------------------------------------------------------------------------
# Финансовый анализ
st.markdown("<a name='section3'></a>", unsafe_allow_html=True)
st.subheader("Распределение сумм контрактов")
st.write("Гистограмма показывает, как распределены суммы контрактов в выборке.")
fig = px.histogram(df, x='amount', nbins=50, title="Распределение сумм")
st.plotly_chart(fig)

with st.spinner("🔄 Идёт обработка данных, ждём..."):
    time.sleep(3)

st.success("✅ Готово!")
#----------------------------------------------------------------------------------------
# # Организации, лидеры рынка
# st.markdown("<a name='section4'></a>", unsafe_allow_html=True)
# st.subheader("Топ организаций по общей сумме контрактов")
# st.write("Здесь представлены 3 организации, заключивших контракты на наибольшую сумму.")
# top_organizations = df.groupby('sysOrganizatorId')['amount'].sum().nlargest(10)

# # Подставляем названия организаций вместо ID
# top_organizations_named = (
#     df[['sysOrganizatorId', 'subjectNameRu']]
#     .drop_duplicates('sysOrganizatorId')
#     .set_index('sysOrganizatorId')
#     .loc[top_organizations.index]
# )

# # Объединяем суммы контрактов с названиями организаций
# top_organizations_named['amount'] = top_organizations

# # Строим диаграмму
# st.bar_chart(top_organizations_named.set_index('subjectNameRu')['amount'])

# with st.spinner("🔄 Идёт обработка данных, ждём..."):
#     time.sleep(3)

# st.success("✅ Готово!")

#---------------------------------------------------------------------------------------
# Победители тендеров
st.markdown("<a name='section5'></a>", unsafe_allow_html=True)
st.subheader("Топ заказчиков")
st.write("Этот график отображает 10 организаций, заключивших контракты на наибольшую сумму")

winners = df['sysSubjectsId'].value_counts().sort_values().head(10)

# Фильтруем исходный DataFrame, оставляя только победителей из топ-10
winners_2 = (
    df[df['sysSubjectsId'].isin(winners.index)]
    .groupby('subjectNameRu')['amount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Строим диаграмму
st.bar_chart(winners_2)

with st.spinner("🔄 Идёт обработка данных, ждём..."):
    time.sleep(3)

st.success("✅ Готово!")

# st.write("Hello!")
#--------------------------------------------------------------------
st.markdown("<a name='section6'></a>", unsafe_allow_html=True)
st.subheader("Динамика закупок по годам")
st.write("Линейный график показывает, как изменялась сумма закупок по годам.")
yearly_trends = df.groupby("plnPointYear")["amount"].sum()

fig = px.line(yearly_trends, x=yearly_trends.index, y=yearly_trends.values,
              markers=True)

st.plotly_chart(fig)

#----------------------------------------------------------------------------
st.markdown("<a name='section7'></a>", unsafe_allow_html=True)
st.subheader("Популярные способы закупки")
st.write("Круговая диаграмма отображает 5 самых распространенных методов закупки.")
top_methods = df["refTradeMethodsId"].value_counts().nlargest(5)

fig = px.pie(top_methods, values=top_methods.values, names=top_methods.index)
st.plotly_chart(fig)

#----------------------------------------------------------------------------
# st.markdown("<a name='section8'></a>", unsafe_allow_html=True)
# st.subheader("Топ 10 закупаемых товаров")
# st.write("Этот график демонстрирует 10 самых популярных товаров по количеству закупок.")

# top_categories = df["refEnstruCode"].value_counts().nlargest(10).reset_index()
# top_categories.columns = ["Код КТРУ", "Количество закупок"]

# fig = px.bar(top_categories, x="Количество закупок", y="Код КТРУ", orientation="h")
# st.plotly_chart(fig)
#----------------------------------------------------------------------------
st.markdown("<a name='section9'></a>", unsafe_allow_html=True)
st.subheader("Распределение сумм контрактов по методам закупки")
st.write("Ящик с усами позволяет увидеть медиану, распределение и выбросы сумм контрактов по разным методам закупки.")
fig = px.box(df, x="refTradeMethodsId", y="amount", points="all")

st.plotly_chart(fig)

#----------------------------------------------------------------------------
st.markdown("<a name='section10'></a>", unsafe_allow_html=True)
st.subheader("Распределение закупок по месяцам")
st.write("Гистограмма показывает, как распределены закупки по месяцам в течение года.")
fig = px.histogram(df, x="refMonthsId", nbins=12)
st.plotly_chart(fig)