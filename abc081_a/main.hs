-- main = getLine >>= print . foldl (\acc x -> if x == '1' then acc ++ (read x :: Int) else acc) 0
main = getLine >>= print . length . filter (=='1')