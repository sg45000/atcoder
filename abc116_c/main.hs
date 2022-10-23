import Data.List (group)

main = do
  n <- getLine
  hs <- map read . words <$> getLine
  print $ watering hs 0

countWatering = (+ 1) . length . filter (== 0) . stripzero

decrement = map (\x -> if x == 0 then 0 else x - 1)

watering hs c =
  if all (== 0) hs
    then c
    else watering after (c + count)
  where
    after = decrement hs
    count = countWatering hs

lstrip :: [Int] -> [Int]
lstrip [] = []
lstrip all@(x : xs)
  | x == 0 = lstrip xs
  | otherwise = all

rstrip :: [Int] -> [Int]
rstrip = lstrip . reverse

stripzero :: [Int] -> [Int]
stripzero = delZero . reverse . rstrip . lstrip

delZero :: [Int] -> [Int]
delZero hs = foldl (\acc all@(x : xs) -> if length all > 1 && x == 0 then acc ++ [0] else acc ++ all) [] $ group hs