### ffmpegのインストール

cmdまたはPowerShellで下記コマンドを実行

winget install --id=Gyan.FFmpeg -e
curl -O -L https://github.com/KosukeKojima/Timelapse_comb/releases/download/test/comb.exe

ファイル構造例

<pre>
  ├──2026年
  │   ├──01月
  │   │   ├──01月01日.mp4
  │   │   ├──01月02日.mp4
  │   │   ⋮ 
  │   │   └──01月30日.mp4
  │   │
  │   ├──02月
  │   │
  │   ⋮
  │   └──XX月
  │
  ⋮
  └──XXXX年
</pre>
