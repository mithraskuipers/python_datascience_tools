#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 12:36:17 2023

@author: mkuipers
"""

def getStringLineNumber(file_name, search_string):
    with open(file_name) as f:
        for i, line in enumerate(f, 1):
            if search_string in line:
                return (i)
    return (-1)


string1 = "df_all = df_all[~df_all[\"UserId\"].isin(user_list_not_useful)]"
demoloc1 = getStringLineNumber("new_data_confidence_demo.py", string1)


string2 = "_ = model_compare(model_lst, model_name_lst, data_X=X, data_y=y, name=file_name)"
demoloc2 = getStringLineNumber("new_data_confidence_demo.py", string2)