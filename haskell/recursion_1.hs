
takeIn :: Int -> [a] -> [a]
takeIn 1 (x:xs) = [x]
takeIn n (x:xs) = x : takeIn (n-1) xs

takeN :: Int -> [a] -> [a]
takeN 0 _ = []
takeN _ [] = []
takeN n (x:xs) = x : takeN (n-1) xs

lastElem :: [a] -> a
lastElem xs | length xs == 1 = head xs
            | otherwise = lastElem (tail xs)

join :: Char -> [String] -> String
-- first version > join 'x' ["a", "b"] --> "xaxb"
-- join c (x:xs) = [c] ++ x ++ join c xs
join c [] = ""
join c [s] = s
join c (x:xs) = x ++ [c] ++ join c xs

odds :: [a] -> [a]
odds [] = []
odds [x] = [x]
odds (x:y:rest) = x : odds rest

oddsG :: [a] -> [a]
oddsG xs | length xs == 0 = []
         | length xs == 1 = [head xs]
         | otherwise = [head xs] ++ oddsG (tail (tail xs))

sumEven :: [Int] -> Int
sumEven [] = 0
sumEven (x:xs) = x * ((x + 1) `mod` 2) + sumEven xs

sumEvenG :: [Int] -> Int
sumEvenG xs | length xs == 0 = 0
            | head xs `mod` 2 == 0 = head xs + sumEvenG (tail xs)
            | otherwise = sumEvenG (tail xs)

-- Sum version 1 - what people would normally write, NOT tail recursive
sum1 :: [Int] -> Int
sum1 [] = 0
sum1 (x:xs) = x + sum1 xs

-- Sum version 2 - tail recursive
sum2 :: [Int] -> Int
sum2 xs = sumHelper 0 xs

sumHelper :: Int -> [Int] -> Int
sumHelper acc [] = acc
sumHelper acc (x:xs) = sumHelper (acc + x) xs
