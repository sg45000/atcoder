data Set = Set {c :: Char, i :: Int}

main = do
  line <- getLine
  let sets = foldl fold' [] line
  putStrLn $ foldl (\acc s -> acc ++ [c s] ++ show (i s)) "" sets

fold' :: [Set] -> Char -> [Set]
fold' [] x = [Set x 1]
fold' acc x =
  if c l == x
    then init acc ++ [l{i = i l + 1}]
    else acc ++ [Set x 1]
 where
  l = last acc
