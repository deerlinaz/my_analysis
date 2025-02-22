import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import datetime
import time
def run():
    st.title("📊 Аналитика")
    st.write("Здесь будут графики и анализ данных по определенным ЕНС ТРУ кодам")

    with st.spinner("🔄 Идёт обработка данных, ждём..."):
        time.sleep(3)

    st.success("✅ Готово!")

    URL = "https://ows.goszakup.gov.kz/v3/graphql"
    TOKEN = "8f82885b218e9d5f53004891e3ade12d" 

    st.write("1. Выберите ЕНС ТРУ коды")

    # Множественный выбор кодов
    enstru_codes = st.multiselect(
        "Выберите один или несколько кодов", 
        [ "Другое", "702213.000.000001", "702212.000.000001", "722012.000.000001", "749020.000.000057",
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
        "691013.000.000000", "691012.000.000000"],
        default=["702213.000.000001"]
    )

    st.write("Вы выбрали:", enstru_codes)

    st.write("2. Выберите изначальную дату")
    from_date = str(st.date_input("Выберите изначальную дату", datetime.date.today()))
    st.write("Вы выбрали:", from_date)

    with st.spinner("🔄 Идёт обработка данных, ждём..."):
        time.sleep(3)

    st.success("✅ Готово!")

    QUERY = """
    query getPlans($enstru: String!, $timestamp: [String], $limit: Int, $after: Int) {
    Plans(filter: { refEnstruCode: $enstru, timestamp: $timestamp }, limit: $limit, after: $after) {
        id
        plnPointYear
        amount
        refEnstruCode
    }
    }
    """

    HEADERS = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

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

    # Получение данных для всех выбранных кодов
    df_list = [pd.DataFrame(fetch_plans(code, from_date, limit=100)) for code in enstru_codes]
    df = pd.concat(df_list, ignore_index=True) if df_list else pd.DataFrame()

    if not df.empty:
        # Агрегация данных по годам и кодам
        df_agg = df.groupby(["plnPointYear", "refEnstruCode"], as_index=False).agg({"amount": "sum"})
        
        # Построение графика
        fig = px.line(
            df_agg, x="plnPointYear", y="amount", color="refEnstruCode", markers=True,
            labels={"plnPointYear": "Год", "amount": "Сумма контрактов", "refEnstruCode": "ЕНС ТРУ код"},
            title="Динамика закупок по годам"
        )
        st.plotly_chart(fig)
    else:
        st.write("❌ Данные не найдены. Попробуйте выбрать другие коды или изменить дату.")
if __name__ == "__main__":
    run()