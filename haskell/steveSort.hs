steveSort :: [Int] -> [Int]
steveSort [] = []
steveSort [x] = [x]
steveSort (x:xs) = steveSort smaller ++ ([x] ++ steveSort larger)
      where
        (smaller, larger) = partition xs x

partition :: [Int] -> Int -> ([Int], [Int])
partition [] _ = ([], [])
partition (x:xs) pivot | x < pivot = (x:smaller, larger)
                       | otherwise = (smaller, x:larger)
  where
    (smaller, larger) = partition xs pivot
