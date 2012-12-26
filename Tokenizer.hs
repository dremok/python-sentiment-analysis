module Main where
	import Data.Char
	import System.IO

	data Rating = Negative | Positive

	normalize :: String -> String
	normalize text = tokenize $ filter validChar text
		where
			validChar ch = (isAlpha ch) || (ch == ' ')

	tokenize :: String -> String
	tokenize = map blankToNewline

	blankToNewline :: Char -> Char
	blankToNewline ' ' = '\n'
	blankToNewline ch = ch

	readReviews :: Rating -> IO [String]
	readReviews rating = sequence $ map (readReview rating) [1..25]

	readReview :: Rating -> Integer -> IO String
	readReview Negative i = do
		readFile $ "./MUSIC/no" ++ (show i) ++ ".txt"
	readReview Positive i = do
		readFile $ "./MUSIC/yes" ++ (show i) ++ ".txt"

	main = do
		neg <- readReviews Negative
		pos <- readReviews Positive
		putStr $ normalize neg