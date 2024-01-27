import Data.List

boolStr condition = if condition then "TRUE" else "FALSE"

main = do
	putStrLn (boolStr ("worl" `isInfixOf` "hello world"))
--main = putStrLn "Hello World"
