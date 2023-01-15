import pandas
import numbers

path_xlsx = 'test_1.xlsx'
sheets_names = pandas.ExcelFile( path_xlsx ).sheet_names
df = pandas.Series( len( sheets_names ) - 1 )
i = 0
for sheet_name in sheets_names:
    sheets_name = pandas.read_excel( path_xlsx, sheet_name = sheet_name )
    df[ i ] = pandas.DataFrame( sheets_name )
    i = i + 1

path_xlsx = 'test_11.xlsx'

if path_xlsx == True:
    with pandas.ExcelWriter( path_xlsx, mode = 'a', engine = 'openpyxl', if_sheet_exists = 'overlay' ) as writer:
        df[ 0 ].to_excel( writer, sheet_name = 'Лист1', index = False, header = False, startrow = 1 )
        #dfs[ 0 ].head( 0 ).to_excel( writer, sheet_name = 'Лист1', index = False, header = True )
else:
    with pandas.ExcelWriter( path_xlsx, engine = 'xlsxwriter' ) as writer:
        df[ 0 ].to_excel( writer, sheet_name = 'Лист1', index = False, header = True )
        sheet = writer.sheets[ 'Лист1' ]
        sheet.autofilter( 0, 0, 0, len( df[ 0 ].columns ) - 1 )
        #dfs[ 1 ].head( 0 ).to_excel( writer, sheet_name = 'Лист1', index = False, header = True, startrow = 1 )