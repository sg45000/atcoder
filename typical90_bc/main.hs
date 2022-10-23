import Data.Array.Unboxed
import qualified Data.ByteString.Char8 as BS
import Data.Char (isSpace)
import Data.List (unfoldr)

getInts :: IO [Int]
getInts = unfoldr (BS.readInt . BS.dropWhile isSpace) <$> BS.getLine

main :: IO ()
main = do
  [n, p, q] <- getInts
  as <- getInts
  let as' = listArray (1, n) as :: (UArray Int Int)
  let ix =
        [ v
          | -- (i, j, k, l, m)
            i <- [1 .. n - 4],
            j <- [i + 1 .. n - 3],
            k <- [j + 1 .. n - 2],
            l <- [k + 1 .. n - 1],
            m <- [l + 1 .. n],
            let v = [(as' ! i) `mod` p, (as' ! j ) `mod` p, (as' ! k)  `mod` p, (as' ! l) `mod` p, (as' ! m) `mod` p],
            0 `elem` v
        ]
  print $ length ix