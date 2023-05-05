main = interact $ show . sum . (zipWith ((max 0 .) . flip (-)) =<< (0 :)) . tail . map read . words
