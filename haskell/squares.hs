type Square = (Int,Int,Int,[Char])

drawSquares :: [Square] -> IO ()
drawSquares squares = putStr result
  where
    result = render squares (1000-1) 50

-- render square idx rowLength
render :: [Square] -> Int -> Int -> [Char]
render squares idx _ | idx < 0 = ""
render squares idx rowLength = init ++ cur : nl
  where
    x = mod idx rowLength
    y = div idx rowLength
    init = (render squares (idx - 1) rowLength)
    nl = if x == rowLength - 1 then "\n" else ""
    cur = sample squares x y
-- render width*height-1
-- render 3 "4\n"
-- render 2 "3"
-- render 1 "2\n"
-- render 0 "1"

-- samples the character to render at a single x,y position
-- uses '.' as the background character
sample :: [Square] -> Int -> Int -> Char
sample squares x y = sampleWithDefault squares '.' x y

-- same as sample, but
sampleWithDefault :: [Square] -> Char -> Int -> Int -> Char
sampleWithDefault [] bg _ _ = bg
sampleWithDefault (square:rest) bg x y = sampleWithDefault rest ch x y
  where
    sqch = sampleSquare square x y
    ch = if sqch == '\0' then bg else sqch

-- returns NUL for transparent
sampleSquare :: Square -> Int -> Int -> Char
sampleSquare (sx, sy, size, [b, f]) x y
  | inBounds && x == sx = b
  | inBounds && x == sx + size - 1 = b
  | inBounds && y == sy = b
  | inBounds && y == sy + size - 1 = b
  | inBounds = if f == '#' then '\0' else f
  | otherwise = '\0'
  where
    inBounds = y >= sy && y < sy + size && x >= sx && x < sx + size
