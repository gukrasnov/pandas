import time
import pandas
import datetime

start_time = time.monotonic()

#[ 'ID', 'ID_CODE', 'Дата предложения', 'Цена предложения', 'Цена за кв.м.', 'Площадь', 'Кад. номер', 'Район', 'Город', 'Внутр. район', 'НП', 'Улица', 'Доп. элемент', 'Доп. доп. элемента', 'N дома', 'N строения', 'Кол-во этажей', 'ВРИ', 'Год ввода в эксплуатацию', 'Год завершения строительства', 'Ссылка', 'Текст объявления', 'Сегмент' ]

work_sheet = pandas.read_excel( 'A/Выгрузки Зданий и Помещений2.xlsx', sheet_name = 0 )
df = pandas.DataFrame( work_sheet )

df_max = df[ df ['Площадь' ] == df[ 'Площадь' ].max() ]
df_min = df[ df ['Площадь' ] == df[ 'Площадь' ].min() ]
df_max[ 'Цена за кв.м.' ] = 'MAX = '
df_min[ 'Цена за кв.м.' ] = 'MIN = '
df = df.append( df_max[ [ 'ID', 'Цена за кв.м.', 'Площадь' ] ], ignore_index = True )
df = df.append( df_min[ [ 'ID', 'Цена за кв.м.', 'Площадь' ] ], ignore_index = True )

print( df[[ 'ID', 'Цена за кв.м.', 'Площадь' ]] )

path_xlsx = 'A/Выгрузки Зданий и Помещений (MAX MIN).xlsx'

if path_xlsx == True:
    with pandas.ExcelWriter( path_xlsx, mode = 'a', engine = 'openpyxl', if_sheet_exists = 'overlay' ) as writer:
        df.to_excel( writer, sheet_name = 'Лист1', index = False, header = False, startrow = 1 )
else:
    with pandas.ExcelWriter( path_xlsx, engine = 'xlsxwriter' ) as writer:
        df.to_excel( writer, sheet_name = 'Лист1', index = False, header = True )
        work_sheet = writer.sheets[ 'Лист1' ]
        work_sheet.set_row_pixels( 0, 100 )
        work_sheet.autofilter( 0, 0, 0, len( df.columns ) - 1 )

end_time = time.monotonic()
print( 'Время выполнения кода: ', datetime.timedelta( seconds = end_time - start_time ) )