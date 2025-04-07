import streamlit as st  
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.header('Уважаемые коллеги, просим пройти опрос, посвященный вовлеченности. \n Опрос анонимный.\n Прохождение опроса займет буквально 5-7 минут.\n Благодарим за уделенное время.', divider="orange")
st.subheader('Вопрос 1')
qwe_1 = st.slider("Насколько Вы доверяете компетенциям и экспертизе руководства вашего подразделения?", 1, 10) # для сбора текстового ввода
st.subheader('Вопрос 2')
qwe_2 = st.slider("Насколько Вы доверяете информации от вашего руководителя?", 1, 10)
st.subheader('Вопрос 3')
qwe_3 = st.slider("Насколько Вам безопасно и комфортно проявляться в рабочих обсуждениях?", 1, 10)
st.subheader('Вопрос 4')
qwe_4 = st.slider("Насколько Вы уверены, что Ваши временные инвестиции в рабочие задачи окупятся?", 1, 10)
st.subheader('Вопрос 5')
qwe_5 = st.slider("Легко ли Вам ориентироваться в рабочих задачах (организация в редмайн, почта и тд)?", 1, 10)
st.subheader('Вопрос 6')
qwe_6 = st.slider("Насколько доступно руководители доносят информацию?", 1, 10)
st.subheader('Вопрос 7')
qwe_7 = st.slider("Насколько понятно, как применить то, что Вы слышите на обучениях, которые проводятся?", 1, 10)
st.subheader('Вопрос 8')
qwe_8 = st.slider("Насколько понятно, к кому Вам обращаться по возникающим вопросам (понятно ли, какие задачи выполняет каждое подразделение)?", 1, 10)
st.subheader('Вопрос 9')
qwe_9 = st.slider("Насколько рабочие задачи отвечают Вашим собственным целям – личным и профессиональным?", 1, 10)
st.subheader('Вопрос 10')
qwe_10 = st.slider("Насколько интересно построены возможности обучения / повышения квалификации?", 1, 10)
st.subheader('Вопрос 11')
qwe_12 = st.slider("Насколько Вам интересно участвовать в дополнительных активностях? (конкурсы, корпоративы, посадка деревьев и тд.)", 1, 10)
st.subheader('Вопрос 12')
qwe_13 = st.slider("Насколько КОМФОРТЕН для вас рабочий график", 1, 10)
st.subheader('Вопрос 13')
qwe_14 = st.slider("Легко ли Вам проявлять активность во внерабочих темах - генерить идеи, общаться?", 1, 10)
st.subheader('Вопрос 14')
qwe_15 = st.slider("Насколько хорошо реализована возможность новых знакомств на внутрибанковский мероприятиях / встречах?", 1, 10)
st.subheader('Вопрос 15')
qwe_16 = st.slider("Насколько Вы можете влиять на то, каким образом выполнять ту или иную задачу (подходы, методы, инструменты)", 1, 10)
st.subheader('Вопрос 16')
qwe_17 = st.slider("Соответствует ли царящая на работе атмосфера Вашим ценностям? Например, если Вам важна забота, Вы ее ощущаете. Если Вам важно проявиться, Вы чувствуете поддержку. Если Вам важна безопасность, Вы чувствуете себя в безопасности.", 1, 10)
st.subheader('Вопрос 17')
qwe_19 = st.slider("Насколько Вам комфортно физически на вашем рабочем месте (удобство рабочего места, температурный режим, освещенность и пр.)", 1, 10)



def save_into_csv(qwe_1, qwe_2, qwe_3, qwe_4, qwe_5, qwe_6, qwe_7, qwe_8, qwe_9, qwe_10, qwe_12, qwe_13, qwe_14, qwe_15, qwe_16, qwe_17, qwe_19):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    google_service_account_info = st.secrets['gcp_service_account']
    creds = ServiceAccountCredentials.from_json_keyfile_dict(google_service_account_info, scope)
    client = gspread.authorize(creds)

# Open the Google Sheet using its name
    sheet = client.open('work')
    worksheet = sheet.get_worksheet(0)
    if st.button('Отправить данные'):
        worksheet.append_row([qwe_1, qwe_2, qwe_3, qwe_4, qwe_5, qwe_6, qwe_7, qwe_8, qwe_9, qwe_10, qwe_12, qwe_13, qwe_14, qwe_15, qwe_16, qwe_17, qwe_19])
        st.write('Submitted to database!')

save_into_csv(qwe_1, qwe_2, qwe_3, qwe_4, qwe_5, qwe_6, qwe_7, qwe_8, qwe_9, qwe_10, qwe_12, qwe_13, qwe_14, qwe_15, qwe_16, qwe_17, qwe_19)



