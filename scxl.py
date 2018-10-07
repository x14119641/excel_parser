import pandas as pd
import json
from pprint import pprint

class ReadRules():
    def __init__(self,json_rules):
        self.json_rules = json_rules
        with open(self.json_rules,'r')as js:
            self.rules=json.load(js)

    def get_file_name(self):
        return self.rules['file_name']


    def get_rules(self):
        return self.rules['rules'][0]

    def get_sheet_name(self):
        return self.rules['rules'][0]['sheet_name']

    def get_headers_position(self):
        return self.rules['rules'][0]['headers_position']

    def get_details_position(self):
        return self.rules['rules'][0]['details_position']

    def get_measures_index(self):
        return self.rules['rules'][0]['measures_index']

    def get_functions(self):
        return self.rules['rules'][0]['functions'][0]


    # def get_file_name(self):
    #     return self.rules['file_name']

# class FormatExcel():
#     def __init__()
def read_excel(excel_file):
    return pd.read_excel(excel_file,header=None,
                        skip_blank_lines=False,sheet_name=1)

def read_excel2(excel_file,headers_position,measures_index,sheet_name):
    return pd.read_excel(excel_file,header=3,
                        # skip_blank_lines=False,
                        index_col=[0,1],
                        sheet_name=1)
def get_details(df,start, end):
    return df.iloc[int(start):int(end),:]

def strip_details(df,start, end):
    return df.drop((df.index[int(start):int(end)]))

def concatenate_measure_strings(entry,start,end, fill_spaces=False):
    if fill_spaces:
        df[0]= df[0].fillna(method='ffill')
        df[0] = df[0].astype(str).str.cat(df[1].astype(str), sep=' ')
        df.drop([1],inplace=True)
        return df
    else:
        return df[df[int(start)]+df[int(end)]]
def split_table(df,start,end):
    return df.iloc[start:end,]

def split_columns(df,start,end):
    return df.iloc[:,start:end]

def get_headers(df_0,start,end):
    return df_0.iloc[start:end]

if __name__=='__main__':
    rs =ReadRules('rules.json')
    file_name = rs.get_file_name()
    details_position = rs.get_details_position().split(':')
    headers_position = rs.get_headers_position()
    sheet_name = rs.get_sheet_name()
    measures_index = rs.get_measures_index()
