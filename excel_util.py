#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pandas as pd
import xlrd
import json


def excel_to_df(file_path, header=1):
    headers = [i for i in range(header)]
    excel_dict = {}
    random_color_dict = {}
    data = xlrd.open_workbook(file_path)
    for sheet in data.sheets():
        sheet_name = sheet.name
        df = pd.read_excel(file_path, sheet_name, header=headers)
        excel_dict[sheet_name] = df

    return excel_dict, random_color_dict


def df_to_json(df, orient='records'):
    return json.loads(df.to_json(orient=orient))


def run():
    result = []
    excel_dict, _ = excel_to_df('111111.xlsx')
    df = excel_dict.get('Sheet4')
    office_list = df['办事处'].unique()
    for office in office_list:
        office_df = df[df['办事处'] == office]
        province_set = set()
        province_code_list = office_df['门店编码'].astype('str').tolist()
        for province_code in province_code_list:
            province_set.add(province_code)
        city_set = set()
        city_code_list = office_df['编码'].astype('str').tolist()
        for city_code in city_code_list:
            if city_code == 'nan':
                continue
            city_set.add(city_code[:6])
        result.append({office: {'province_id': list(province_set), 'city_id': list(city_set)}})
    return result


if __name__ == '__main__':
    res = run()
    print(res)
