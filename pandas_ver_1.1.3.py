import pandas
work_sheet_1 = pandas.read_excel( 'pandas/1.xlsx', sheet_name = 'Лист1', usecols = [ 'Кадастровый номер', 'Вид покрытия' ] )
work_sheet_2 = pandas.read_excel( 'pandas/2.xlsx', sheet_name = 'Лист1' )
df_1 = pandas.DataFrame( work_sheet_1 )
df_2 = pandas.DataFrame( work_sheet_2 )
for index_1, ( iRow_1_1, iRow_1_2 ) in enumerate( zip( df_1[ 'Кадастровый номер' ], df_1[ 'Вид покрытия' ] ) ):
    for index_2, ( iRow_2_1, iRow_2_2 ) in enumerate( zip( df_2[ 'Кадастровый номер' ], df_2[ 'Вид покрытия' ] ) ):
        if iRow_1_1 == iRow_2_1:
            df_2[ 'Вид покрытия' ].iloc[ index_2 ] = iRow_1_2
            print( index_1, ': =>', iRow_1_1, iRow_1_2, ':::::::::', index_2, ': =>', iRow_2_1, iRow_1_2 )
print( df_2 )
df_2.to_excel( 'pandas/3.xlsx', sheet_name = 'Лист1', index = False )