# FamousWord<br>
検索結果数の多いものを調べるアルゴリズム

## 機能<br>
input.txtに入っているキーワードをGoogleで検索し検索結果数を出力するプログラムです。<br>

![2021-10-17_19h49_50](https://user-images.githubusercontent.com/77985354/137624032-ad1f8dd0-e952-4aa8-b53c-490f54db9421.png)

上の画像はcsv出力例<br>
左が検索文字、右が検索結果数を表示

※time.sleep()を用いている理由は、これをしないと相手サーバーに過負荷をかけてしまうためです。<br>
　集中アクセスを避けるためにtime.sleep()にて処理を遅延させています。<br>

## ざっくりとした仕組み<br>
input.txtを読み込む<br>
↓<br>
seleniumで検索<br>
↓<br>
出力を「output.txt」「output.csv」に書き込む

## 動かない場合<br>
・実行できない！<br>
→Python実行環境がない可能性があります。Pythonの実行環境を用意してください。<br>

```diff
- 注意！
このプログラムではChromeDriverが必要です。
ですので、使用する場合は「ChromeDriverの入れ方.md」を参照しながらインストールしてプログラム内変数「chrome_driver_path」のパスを書き換えてください。
```

## お問い合わせ<br>
何かございましたら「shaneron@sumahotektek.com」まで連絡ください。反応は非常に遅いです。<br>

### 変更履歴<br>
Ver1.0:初期バージョン
