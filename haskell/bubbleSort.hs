import Control.Arrow (Arrow (arr))
import Control.Monad
import Control.Monad.ST
import Data.Array.ST
import Data.Array.Unboxed (UArray, bounds, elems, listArray)

bubbleSort :: UArray Int Int -> UArray Int Int
bubbleSort arr = runSTUArray $ do
    stArr <- thaw arr
    let end = (snd . bounds) arr
    forM_ [1 .. end] $ \i -> do
        forM_ [0 .. end - i] $ \j -> do
            val <- readArray stArr j
            nextVal <- readArray stArr (j + 1)
            when (val > nextVal) $ do
                writeArray stArr j nextVal
                writeArray stArr (j + 1) val
    return stArr

listToArray :: [Int] -> UArray Int Int
listToArray myList = listArray (0, length myList - 1) myList
