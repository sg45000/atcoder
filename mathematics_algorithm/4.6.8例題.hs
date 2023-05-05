modulus :: Int
modulus = 1_000_000_007

newtype IntMod = IntMod Int deriving (Show, Eq)

instance Num IntMod where
    IntMod x + IntMod y = IntMod ((x `mod` modulus + y `mod` modulus) `mod` modulus)
    IntMod x - IntMod y = IntMod ((x `mod` modulus - y `mod` modulus) `mod` modulus)
    IntMod x * IntMod y = IntMod ((x `mod` modulus * y `mod` modulus) `mod` modulus)
    fromInteger n = IntMod (fromInteger (n `mod` fromIntegral modulus))
    abs = abs
    signum = signum

main = do
    x <- readLn
    y <- readLn
    let denominator = factorial (IntMod x) * factorial (IntMod y)
    let numerator = factorial (IntMod x + IntMod y)
    print (numerator `divIntMod` denominator)

divIntMod (IntMod a) (IntMod b) = a `div` b

factorial 1 = 1
factorial x = x * factorial x - 1