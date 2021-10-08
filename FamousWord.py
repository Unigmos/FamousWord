from selenium import webdriver
import time
import csv

#入力ファイルと出力ファイルの設定
input_path = 'input/input.txt'
output_path = 'output/output.txt'
csv_output_path = 'output/output.csv'

#ChromeDriverのパス指定
chrome_driver_path = 'chromedriver_win32/chromedriver.exe'

#入力ファイルの読み込み
with open(input_path, "r") as file:
    datas = file.readlines()

#結果表示用の辞書定義
dictionary = {}

for data in datas:
    data = data.replace("\n","")
    #ドライバー指定
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get('https://www.google.com/')
    #検索(入力欄を探す→文字列の入力→検索実行)
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(data)
    search_box.submit()

    #検索結果数取得
    result_box = driver.find_elements_by_id("result-stats")
    for searched_number in result_box:
        numbers = searched_number.text #この時点で約〇〇件(〇〇秒)が表示
        #文字列の調整(「,」や文字列の削除)
        numbers = int(numbers.removeprefix('約 ').partition(' 件')[0].replace(',', ''))

    #辞書に検索文字と検索結果数の追加
    dictionary.setdefault(data, numbers)

    time.sleep(2)
    #アクティブブラウザを閉じる
    driver.close()

#辞書のvalueを比較(降順)
sort_dictionary = sorted(dictionary.items(), key=lambda i: i[1], reverse=True)

#メモに検索結果数の降順で保存
with open(output_path, "w", encoding = "utf-8") as write_file:
    for file_writer in sort_dictionary:
        write_file.write(file_writer[0] + ":" + str(file_writer[1]) + "\n")

#csvに検索結果数の降順で出力
with open(csv_output_path, "w") as csv_write_file:
    csv_writer = csv.writer(csv_write_file,lineterminator='\n')
    csv_writer.writerows(sort_dictionary)