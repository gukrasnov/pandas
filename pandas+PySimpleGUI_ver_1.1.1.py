import os
import time
import pandas
import datetime
import PySimpleGUI

start_time = time.monotonic()

_combo_1_ = []

layot = [
            #[ PySimpleGUI.Table( values = df_1.values.tolist(), headings = df_1.columns.to_list(), row_height = 55, vertical_scroll_only = False, expand_x = True, expand_y = True ) ]
            [
              PySimpleGUI.T( '1 файл' ),
              PySimpleGUI.In( enable_events = True, key = '_file_1_' ),
              PySimpleGUI.FileBrowse( button_text = 'Выбрать 1 файл', target = '_file_1_' )
            ],
            [
              PySimpleGUI.T( '2 файл' ),
              PySimpleGUI.In( key = '_file_2_' ),
              PySimpleGUI.FileBrowse( button_text = 'Выбрать 2 файл', target = '_file_2_' )
            ],
            [
              PySimpleGUI.Column( [ [ PySimpleGUI.Frame( '1 файл', [ [ PySimpleGUI.Combo( [ i for i in _combo_1_ ], size = ( 21 ), key = '_combo_1_' ) ], [ PySimpleGUI.Combo( 'listbox_1', size = ( 21 ) ) ] ], key = '-FRAME_1-' ) ] ] ),
              PySimpleGUI.Column( [ [ PySimpleGUI.T( 'Сравнение' ) ], [ PySimpleGUI.T( 'Значение' ) ] ], element_justification = 'center' ),
              PySimpleGUI.Column( [ [ PySimpleGUI.Frame( '2 файл', [ [ PySimpleGUI.Combo( [], size = ( 21 ), key = '_listbox_2_' ) ], [ PySimpleGUI.Combo( 'listbox_2', size = ( 21 ) ) ] ], key = '-FRAME_2-' ) ] ] )
            ]
        ]


window = PySimpleGUI.Window( 'Excel', layot, element_justification = 'center', resizable = True, grab_anywhere = True )



while True:
  event, values = window.read()
  if event == PySimpleGUI.WIN_CLOSED or event == 'Cancel':
    break
  elif event == '_file_1_' :
    work_sheet_1 = pandas.read_excel( values[ '_file_1_' ], sheet_name = 'Лист1' )
    df_1 = pandas.DataFrame( work_sheet_1 )
    _combo_1_ = df_1.columns.to_list()
    window[ '_combo_1_' ].update( values = _combo_1_ )
  else:
    None
  print( 'Ты вошёл: ', values[ 0 ] )

window.close()

end_time = time.monotonic()
print( 'Время выполнения кода: ', datetime.timedelta( seconds = end_time - start_time ) )
