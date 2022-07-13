import unittest
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

# DON'T DO THE FOLLOWING IN REAL LIFE; MAKE A MODULE INSTEAD!
# This system path hack assumes you call this script from the main directory
# (i.e. at the same level as the README file). It fails if you call it from
# another directory, which is why making a module is the better approach.
import sys
sys.path.insert(1, './scripts')
# END HACK =========================

try:
    from find_max import (sort_filenames,
                          import_files_into_dataframe,
                          get_max_values,
                          )

except ImportError as import_fail:
    message = import_fail.args[0].split('(', maxsplit=1)
    item_name = import_fail.args[0].split()[3]

    item_name = item_name[:-1] + "()'"
    # pylint: disable=raise-missing-from
    raise ImportError("In your 'find_max.py' file, we can not find or"
                      f'import the function named {item_name}. Did you'
                      ' misname or forget to define it?')


class FindMaxTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_sort_filenames_by_month(self):
        input_data = ['2021-08-01_room-temp_results.txt',
                      '2021-08-02_room-temp_results.txt',
                      '2021-08-03_room-temp_results.txt',
                      '2021-10-04_room-temp_results.txt',
                      '2021-10-05_room-temp_results.txt',
                      '2021-10-06_room-temp_results.txt',
                      ]
        result_data = [['2021-08-01_room-temp_results.txt',
                        '2021-08-02_room-temp_results.txt',
                        '2021-08-03_room-temp_results.txt',
                       ],
                       ['2021-10-04_room-temp_results.txt',
                        '2021-10-05_room-temp_results.txt',
                        '2021-10-06_room-temp_results.txt',
                       ],
                      ]
        failure_msg = 'Filenames not grouped by month'
        self.assertEqual(sort_filenames(input_data), result_data, msg=failure_msg)

    @pytest.mark.task(taskno=2)
    def test_sort_filenames_across_directories(self):
        input_data = ['C_directory/2021-08-01_room-temp_results.txt',
                      'A_directory/2021-08-02_room-temp_results.txt',
                      'B_directory/2021-08-03_room-temp_results.txt',
                      'F_directory/2021-10-04_room-temp_results.txt',
                      'E_directory/2021-10-05_room-temp_results.txt',
                      'D_directory/2021-10-06_room-temp_results.txt',
                      ]
        result_data = [['C_directory/2021-08-01_room-temp_results.txt',
                        'A_directory/2021-08-02_room-temp_results.txt',
                        'B_directory/2021-08-03_room-temp_results.txt',
                       ],
                       ['F_directory/2021-10-04_room-temp_results.txt',
                        'E_directory/2021-10-05_room-temp_results.txt',
                        'D_directory/2021-10-06_room-temp_results.txt',
                       ],
                      ]
        failure_msg = 'Filenames not grouped across directories'
        self.assertEqual(sort_filenames(input_data), result_data, msg=failure_msg)

    @pytest.mark.task(taskno=3)
    def test_sort_filenames_reorders_files(self):
        input_data = ['A_directory/2021-08-01_room-temp_results.txt',
                      'B_directory/2021-08-03_room-temp_results.txt',
                      'C_directory/2021-08-02_room-temp_results.txt',
                      'D_directory/2021-10-06_room-temp_results.txt',
                      'E_directory/2021-10-04_room-temp_results.txt',
                      'F_directory/2021-10-05_room-temp_results.txt',
                      ]
        result_data = [['A_directory/2021-08-01_room-temp_results.txt',
                        'C_directory/2021-08-02_room-temp_results.txt',
                        'B_directory/2021-08-03_room-temp_results.txt',
                       ],
                       ['E_directory/2021-10-04_room-temp_results.txt',
                        'F_directory/2021-10-05_room-temp_results.txt',
                        'D_directory/2021-10-06_room-temp_results.txt',
                       ],
                      ]
        failure_msg = f'Filenames not reordered by date on sort'
        self.assertEqual(sort_filenames(input_data), result_data, msg=failure_msg)

    @pytest.mark.task(taskno=4)
    def test_import_files_into_dataframe_maintains_size(self):
        input_filenames = [['./tests/test_data/sample_data1.txt',
                            './tests/test_data/sample_data2.txt',
                           ],
                           ['./tests/test_data/sample_data3.txt',
                            './tests/test_data/sample_data4.txt',
                           ],
                          ]
        failure_msg = f'List of dataframes does not match number of sublists'
        self.assertEqual(len(import_files_into_dataframe(input_filenames)),
                         len(input_filenames), msg=failure_msg)

    @pytest.mark.task(taskno=5)
    def test_get_max_values(self):
        input_filenames = [['./tests/test_data/sample_data1.txt',
                            './tests/test_data/sample_data2.txt',
                           ],
                           ['./tests/test_data/sample_data3.txt',
                            './tests/test_data/sample_data4.txt',
                           ],
                          ]
        df_list = import_files_into_dataframe(input_filenames)
        result = pd.read_csv('./tests/test_data/expected_max_values.csv',
                             header=None)
        print(result)
        print(get_max_values(df_list))
        failure_msg = f'Max values not computed on each sublist in dataframe'
        df_equal = assert_frame_equal(get_max_values(df_list), result)
        self.assertEqual(None, df_equal, msg=failure_msg)
