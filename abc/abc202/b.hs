main = do
    s <- getLine
    putStrLn $ reverse s

reverse :: String -> String
reverse [] = ""
reverse ('0': s) = '0' `mappend` s