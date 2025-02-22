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



st.title("🏠 Главная страница")

st.title("Анализ закупок и тендеров")




st.page_link("/Users/alina/Desktop/feb_22/pages/single.py", label="📊 Аналитика по определенному ЕНС ТРУ коду")
st.page_link("/Users/alina/Desktop/feb_22/pages/several.py", label="📊 Сравнительная аналитика по нескольким ЕНС ТРУ кодам")

# st.page_link("pages/contacts.py", label="📞 Контакты")



with st.spinner("🔄 Идёт обработка данных, ждём..."):
    time.sleep(3)

st.success("✅ Готово!")

# URL = "https://ows.goszakup.gov.kz/v3/graphql"
# TOKEN = "8f82885b218e9d5f53004891e3ade12d" 

# # enstru_code = st.selectbox(
# #     'Выберите код ЕНС ТРУ',
# #     ( "702213.000.000001", "702212.000.000001", "722012.000.000001", "749020.000.000057",
# #     "702211.000.000002", "702212.000.000000", "711124.000.000002", "692023.000.000000",
# #     "711231.900.000000", "620220.000.000000", "702216.900.000001", "749019.000.000011",
# #     "711142.000.000000", "702211.000.000003", "749020.000.000007", "702211.000.000004",
# #     "749019.000.000016", "711211.000.000000", "749019.000.000004", "702217.000.000000",
# #     "692010.000.000000", "741019.000.000000", "702211.000.000007", "702212.000.000003",
# #     "749019.000.000010", "692031.000.000000", "749019.000.000005", "749013.000.000000",
# #     "749019.000.000009", "702212.000.000004", "749019.000.000007", "749019.000.000008",
# #     "702211.000.000008", "702211.000.000005", "702215.000.000000", "702211.000.000001",
# #     "702214.000.000000", "702213.000.000000", "702216.900.000000", "749015.000.000000",
# #     "749019.000.000003", "781011.000.000001", "749019.000.000006", "702211.000.000006",
# #     "702211.000.000000", "711211.000.000001", "702212.000.000002", "702213.000.000001",
# #     "702212.000.000001", "691012.000.000005", "691012.000.000006", "691012.000.000007",
# #     "691012.000.000003", "691014.000.000003", "691012.000.000004", "691014.000.000000",
# #     "691011.000.000000", "691014.000.000002", "691014.000.000001", "691012.000.000001",
# #     "691013.000.000000", "691012.000.000000"))

# # st.write('Вы выбрали:', enstru_code)
# # # "691012.000.000002"
# # enstru_code = st.text_input("Напишите здесь если отсутствует")

# # st.write('Вы выбрали:', enstru_code)
# # Выпадающий список с возможностью редактирования
# enstru_code = [ "Другое", "702213.000.000001", "702212.000.000001", "722012.000.000001", "749020.000.000057",
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
#     "691013.000.000000", "691012.000.000000"]

# # Dropdown для выбора
# selected = st.selectbox("Выберите или введите своё значение", enstru_code)

# # Если выбрано "Другое", показываем текстовое поле
# if selected == "Другое":
#     manual_input = st.text_input("Введите своё значение")
#     final_value = manual_input if manual_input else selected
# else:
#     final_value = selected

# enstru_code = final_value
# st.write("Вы выбрали:", enstru_code)

# with st.spinner("🔄 Идёт обработка данных, ждём..."):
#     time.sleep(3)

# st.success("✅ Готово!")

# #------------------------------------------------------------------------------------------

# from_date = str(st.date_input("Выберите изначальную дату ", datetime.date.today()))
# st.write("Вы выбрали:", from_date)

# with st.spinner("🔄 Идёт обработка данных, ждём..."):
#     time.sleep(3)

# st.success("✅ Готово!")

# #-----------------------------------------------------------------------------
# # date_range = st.date_input("Выберите диапазон дат", 
# #                            [datetime.date.today() - datetime.timedelta(days=7), datetime.date.today()])
# # st.write("Вы выбрали:", date_range)

# #----------------------------------------------------------------------------

# QUERY = """
# query getPlans($enstru: String!, $timestamp: [String], $limit: Int, $after: Int) {
#   Plans(filter: { refEnstruCode: $enstru, timestamp: $timestamp }, limit: $limit, after: $after) {

#     # Уникальный идентификатор
#     id
#     # Ид родительского пункта плана
#     rootrecordId
#     # ИД Заказчика
#     sysSubjectsId
#     # ИД Организатора
#     sysOrganizatorId
#     # БИН/ИИН заказчика
#     subjectBiin
#     # Наименование заказчика на русском языке
#     subjectNameRu
#     # Наименование заказчика на государственном языке
#     subjectNameKz
#     # Наименование на русском языке
#     nameRu
#     # Наименование на государственном языке
#     nameKz
#     # Код способа закупки (плановый)
#     refTradeMethodsId
#     # Код единицы измерения
#     refUnitsCode
#     # Количество / объем
#     count
#     # Цена за единицу
#     price
#     # Общая сумма, утвержденная для закупки
#     amount
#     # Планируемый срок закупки
#     refMonthsId
#     # Статус пункта плана
#     refPlnPointStatusId
#     # Финансовый год в пункте плана
#     plnPointYear
#     # Код вида предмета закупки
#     refSubjectTypeId
#     # Код КТРУ
#     refEnstruCode
#     # Код источника финансирования
#     refFinsourceId
#     # Код администратора бюджетной программы
#     refAbpCode
#     # Признак субъект/не субъект ГЗ (квазисектор) 0 - субъект ГЗ, 1 - не субъект ГЗ
#     isQvazi
#     # Дата создания записи
#     dateCreate
#     # Дата изменения записи
#     timestamp
#     # Код типа пункта плана
#     refPointTypeId
#     # Краткая характеристика на русском языке
#     descRu
#     # Краткая характеристика на государственном языке
#     descKz
#     # Дополнительное описание на государственном языке
#     extraDescKz
#     # Дополнительное описание на русском языке
#     extraDescRu
#     # Планируемая сумма на 1 год
#     sum1
#     # Планируемая сумма на 2 год
#     sum2
#     # Планируемая сумма на 3 год
#     sum3
#     # Срок поставки
#     supplyDateRu
#     # Размер авансового платежа %
#     prepayment
#     # Обоснование применения способа закупки
#     refJustificationId
#     # Вид дополнительного соглашения
#     refAmendmentAgreemTypeId
#     # ИД основания создания дополнительного соглашения
#     refAmendmAgreemJustifId
#     # Номер пункта плана в договоре
#     contractPrevPointId
#     # Признаки ограничений закупки
#     disablePersonId
#     # ИД филиала (кому передано)
#     transferSysSubjectsId
#     # Тип передачи плана
#     transferType
#     # Код вида бюджета
#     refBudgetTypeId
#     # Идентификатор акта
#     createdinActId
#     # Активность
#     isActive
#     # Идентификатор активного акта
#     activeActId
#     # Объект удален
#     isDeleted
#     # ИД системы
#     systemId
#     # Дата индексации
#     indexDate
#   }
# }
# """
# HEADERS = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {TOKEN}"
# }
# # from_date = "2020-01-01"
# # enstru_code = '620220.000.000000'

# def fetch_plans(enstru_code, from_date, limit=200):
#     after = 0
#     all_results = []
#     while True:
#         variables = {"enstru": enstru_code, "timestamp": [from_date], "limit": limit, "after": after}
#         response = requests.post(URL, json={"query": QUERY, "variables": variables}, headers=HEADERS)
#         data = response.json()

#         plans = data.get("data", {}).get("Plans", [])
#         if not plans:
#             break

#         all_results.extend(plans)
#         after = plans[-1]["id"]
#     return all_results

# df = pd.DataFrame(fetch_plans(enstru_code, from_date, limit=100))



# # data = pd.read_csv("/Users/alina/Downloads/tenders.csv")
# # st.title("")
# st.subheader("Общие данные")
# st.write(df)
# with st.spinner("🔄 Идёт обработка данных, ждём..."):
#     time.sleep(3)

# st.success("✅ Готово!")


# # st.write(df.head())
# #---------------------------------------------------------------------------------------
# # Анализ заказчиков
# st.subheader("Топ заказчиков по количеству покупок")
# buyers_count = df['subjectNameRu'].value_counts().head(10)
# st.bar_chart(buyers_count)

# with st.spinner("🔄 Идёт обработка данных, ждём..."):
#     time.sleep(3)

# st.success("✅ Готово!")

# #---------------------------------------------------------------------------------------
# # Финансовый анализ
# st.subheader("Распределение сумм контрактов")
# fig = px.histogram(df, x='amount', nbins=50, title="Распределение сумм")
# st.plotly_chart(fig)

# with st.spinner("🔄 Идёт обработка данных, ждём..."):
#     time.sleep(3)

# st.success("✅ Готово!")
# #----------------------------------------------------------------------------------------
# # Организации, лидеры рынка
# st.subheader("Топ организаций по общей сумме контрактов")
# top_organizations = df.groupby('sysOrganizatorId')['amount'].sum().nlargest(10)
# # st.bar_chart(top_organizations)

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

# #---------------------------------------------------------------------------------------
# # Победители тендеров
# st.subheader("Топ победителей тендеров")

# # Предполагаем, что df уже загружен

# winners = df['sysSubjectsId'].value_counts().sort_values().head(10)

# # Фильтруем исходный DataFrame, оставляя только победителей из топ-10
# winners_2 = (
#     df[df['sysSubjectsId'].isin(winners.index)]
#     .groupby('subjectNameRu')['amount']
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )

# # Строим диаграмму
# st.bar_chart(winners_2)

# with st.spinner("🔄 Идёт обработка данных, ждём..."):
#     time.sleep(3)

# st.success("✅ Готово!")

# # st.write("Hello!")
# #--------------------------------------------------------------------
# st.subheader("Динамика закупок по годам")
# yearly_trends = df.groupby("plnPointYear")["amount"].sum()

# fig = px.line(yearly_trends, x=yearly_trends.index, y=yearly_trends.values,
#               markers=True)

# st.plotly_chart(fig)

# #----------------------------------------------------------------------------
# st.subheader("Популярные способы закупки")
# top_methods = df["refTradeMethodsId"].value_counts().nlargest(5)

# fig = px.pie(top_methods, values=top_methods.values, names=top_methods.index)
# st.plotly_chart(fig)


# #----------------------------------------------------------------------------
# st.subheader("Топ 10 закупаемых товаров")
# top_categories = df["refEnstruCode"].value_counts().nlargest(10)

# fig = px.bar(top_categories, x=top_categories.values, y=top_categories.index, orientation="h",
#              labels={"x": "Количество закупок", "y": "Код КТРУ"})

# st.plotly_chart(fig)
# #----------------------------------------------------------------------------
# st.subheader("Распределение сумм контрактов по методам закупки")
# fig = px.box(df, x="refTradeMethodsId", y="amount", points="all")

# st.plotly_chart(fig)

# #----------------------------------------------------------------------------
# st.subheader("Распределение закупок по месяцам")
# fig = px.histogram(df, x="refMonthsId", nbins=12)
# st.plotly_chart(fig)



# # chart_data = pd.DataFrame(np.random.randn(20,3), columns = ["a", "b", "c"])
# # st.bar_chart(chart_data)
# # st.line_chart(chart_data)

# # x = st.text_input("movie?")
# # st.write(f"you wrote {x}")