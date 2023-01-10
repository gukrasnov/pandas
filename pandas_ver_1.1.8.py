import os
import pandas
import openpyxl

def update_spreadsheet( path: str, _df, starcol: int = 1, startrow: int = 1, sheet_name: str = 'ToUpdate' ):
    wb = openpyxl.load_workbook( path )
    for ir in range( 0, len( _df ) ):
        for ic in range( 0, len( _df.iloc[ ir ] ) ) :
            wb[ sheet_name ].cell( startrow + ir, starcol + ic ).value = _df.iloc[ ir ][ ic ]
    wb.save( path)

if __name__ == "__main__":
    print( 'GO!' )

sheet_work_1 = pandas.read_excel( 'test_0.xlsx', sheet_name = 'Лист2')
df_1 = pandas.DataFrame( sheet_work_1 )
xlsx_path = os.path.dirname(__file__) + r'\test_00.xlsx'

#update_spreadsheet( xlsx_path, df_1, sheet_name = 'Лист 6 !!!', starcol = 2, startrow = 2 )

with pandas.ExcelWriter( xlsx_path, mode = 'a', if_sheet_exists = 'overlay' ) as writer:
    df_1.to_excel( writer, sheet_name = 'Лист 6 !!!', index = False, header = False, startcol = 0, startrow = 1 )