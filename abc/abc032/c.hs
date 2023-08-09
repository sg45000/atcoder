{-# LANGUAGE TypeApplications #-}

import Control.Monad (replicateM)

main = do
    [n, k] <- map read . words <$> getLine
    as <- replicateM n (readLn @Int)
    let result = if 0 `elem` as then [length as] else shakutori (\r res -> res * r <= k) (*) div 1 as
    print $ maximum result

shakutori ::
    (a -> b -> Bool) -> -- 条件 p
    (b -> a -> b) -> -- 右端を伸ばす演算 op
    (b -> a -> b) -> -- 左端を縮める演算 invOp
    b -> -- 初期値 identity
    [a] -> -- 入力リスト as
    [Int] -- 条件を満たす部分列の長さのリスト
shakutori p op invOp identity as = go as as 0 identity
  where
    -- 右端が空になったら、左端を1つ縮める
    go lls@(l : ls) [] len res = len : (go ls [] (len - 1) (invOp res l))
    go lls@(l : ls) rrs@(r : rs) len res
        -- 条件 p を満たすなら、右端を1つ伸ばす
        | p r res = go lls rs (len + 1) (op res r)
        -- 長さが0であれば、スキップする
        | len == 0 = 0 : (go ls rs 0 identity)
        -- 条件 p を満たさないなら、左端を1つ縮める
        | otherwise = len : (go ls rrs (len - 1) (invOp res l))
    go _ _ _ _ = []