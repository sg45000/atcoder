data PureAction a = PureAction (() -> a)

addAction :: Int -> Int -> PureAction Int
addAction x y = PureAction (\_ -> x + y)

ifIO :: Bool -> IO a -> IO a -> IO a
ifIO b act1 act2 = case b of
    True -> act1
    False -> act2

whileIO :: (a -> Bool) -> a -> (a -> IO a) -> IO ()
whileIO isEnd x0 act = go x0
  where
    go x = ifIO (isEnd x) (pure ()) (act x >>= \nx -> go nx)

-- main :: IO ()
-- main =
--     getLine >>= \loopCmd ->
--         ifIO
--             (loopCmd /= "loop")
--             (putStrLn "No Loop")
--             (whileIO (\(b, _) -> b) (False, 0) (\(_, i) -> putStrLn ("loop" ++ show i) >>= \_ -> getLine >>= \loopEndCmd -> ifIO (loopEndCmd == "end") (pure (True, i)) (pure (False, i + 1))))
