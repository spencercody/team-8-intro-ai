import pandas as pd

def read_and_parse_label_file(path_to_label_file: str)-> pd.DataFrame:
    
    df = pd.read_csv(path_to_label_file, 
                 sep = '\x09',
                 header = 6,
                index_col = False
                )
    
    # cutting off header detail row and the last row
    trimmed_df = df[1:-1].copy()
    
    trim_cols = list(trimmed_df.columns)[1:] # excluding the #fields column name
    
    data = trimmed_df.iloc[:, :-1].copy() # excluding the last column
    
    # creating a dictionary to rename the columns
    rename_cols_dic = {}

    for old_col, new_col in zip(data.columns, trim_cols):
        rename_cols_dic[old_col] = new_col
        
    # renaming the columns
    data = data.rename(columns = rename_cols_dic).copy()
    
    
    # splitting this column into three new columns
    last_cols = data['tunnel_parents   label   detailed-label'].str.split('  ', expand = True)
    
    # renaming the newly split columns
    last_cols.rename(columns = {0:'tunnel_parents', 1:'label', 2: 'detailed-label'}, inplace = True)
    
    # merging the newly split columns onto the main df
    
    merge_df = data.merge(last_cols, left_index = True, right_index = True)
    
    # dropping the columns that was used to split into three
    
    final_df = merge_df.drop(columns = ['tunnel_parents   label   detailed-label']).copy()
    
    return final_df