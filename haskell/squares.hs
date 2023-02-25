
type Square = (Int,Int,Int,[Char])

drawSquares :: [Square] -> IO ()
drawSquares _ = putStr result
  where
    result = ".....\n.+++.\n.+-+.\n.+++.\n.....\n"

drawSquare :: Square -> IO ()
drawSquare (sx, sy, size, [b, f]) = putStr result
  where
    -- result = render (sx, sy, size, [b, f]) (size * size - 1) size
    result = render (sx, sy, size, [b, f]) 96 12

-- render square idx rowLength
render :: Square -> Int -> Int -> [Char]
-- render (sx, sz, size, [b, f]) idx rowLength =
render square idx _ | idx < 0 = ""
render square idx rowLength = init ++ cur : nl
  where
    x = mod idx rowLength
    y = div idx rowLength
    init = (render square (idx - 1) rowLength)
    nl = if x == rowLength - 1 then "\n" else ""
    cur = if isOnBorder square x y then getBorderChar square else '.'
-- render width*height-1
-- render 3 "4\n"
-- render 2 "3"
-- render 1 "2\n"
-- render 0 "1"

isOnBorder :: Square -> Int -> Int -> Bool
isOnBorder (sx, sy, size, _) x y = isTop || isBottom || isLeft || isRight
  where
    isLeft = x == sx && y >= sy && y < sy + size
    isRight = x == sx + size - 1 && y >= sy && y < sy + size
    isTop = y == sy && x >= sx && x < sx + size
    isBottom = y == sy + size - 1 && x >= sx && x < sx + size

--isOnBorder :: Square -> Int -> Int -> Bool
--isOnBorder (sx, sy, size, _) x y
--  | x == sx && y >= sy && y < sy + size = True
--  | x == sx + size - 1 && y >= sy && y < sy + size = True
--  | y == sy && x >= sx && x < sx + size = True
--  | y == sy + size - 1 && x >= sx && x < sx + size = True
--  | otherwise = False

getBorderChar :: Square -> Char
getBorderChar (_, _, _, [b, _]) = b

getFillChar :: Square -> Char
getFillChar (_, _, _, [_, f]) = f
