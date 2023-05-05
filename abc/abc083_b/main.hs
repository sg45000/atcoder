-- 問題文
-- 1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。

-- 制約
-- 1≤N≤10 
-- 4
 
-- 1≤A≤B≤36
-- 入力はすべて整数である
-- 入力
-- 入力は以下の形式で標準入力から与えられる。

-- N A B
-- 出力
-- 1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を出力せよ。

main = do
  [n, a, b] <- map read . words <$> getLine
  print $ sum $ filter (\x -> f x a b) [1..n]

f x a b = (let s = sum [read [c] | c <- show x] in a <= s && s <= b)
