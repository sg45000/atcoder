main :: IO()
main = do
    s <- getLine
    if s == ""
    then putStrLn $ "NO" 
    else putStrLn $ check s

check :: String -> String
check s 
   | (take 6 s) == "eraser" = check $ drop 6 s
   | (take 7 s) == "dreamer" = check $ drop 7 s
   | (take 5 s) == "dream" = check $ drop 5 s
   | (take 5 s) == "erase" = check $ drop 5 s
   | s == "" = "YES"
   | otherwise = "NO"
   


slice :: Int -> Int -> [a] -> [a]
slice from to xs = take (to - from + 1) (drop from xs)