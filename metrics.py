import pandas as pd
from duneanalytics import DuneAnalytics
import streamlit as st

@st.cache(allow_output_mutation=True)
def getdata(query_id):

    # login
    dune = DuneAnalytics('Tachikoma000', 'iZ7kUnw!B8!XUTe')
    dune.login()

    # fetch token
    dune.fetch_auth_token()

    # query
    result_id = dune.query_result_id(query_id=query_id)

    # fetch query result
    data = dune.query_result(result_id)
    result_list=data['data']['get_result_by_result_id']
    result_list_clean=[e['data'] for e in result_list ]
    d=pd.DataFrame(result_list_clean)

    #print(d)

    # # reshape and plot
    # d['Day'] = pd.to_datetime(d.Day)
    # d_=d.pivot(index='Day', columns='Name', values='Floor (Approx)')
    # d_.plot(figsize=(15,5))

    return d
